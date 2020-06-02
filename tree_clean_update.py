# -*- coding: utf-8 -*-
"""
Created on Wednesday 13 May 2020
By Joel
"""

import datetime
import arcpy
from arcgis.gis import GIS


def unique_values(table, field):
    with arcpy.da.SearchCursor(table, [field]) as cursor:
        return sorted({row[0] for row in cursor})


def main():
    """
    The main routine which processes stuff

    """
    arcpy.AddMessage("Setting up workspace and parameters.")
    arcpy.env.overwriteOutput = True
    workspace = r"in_memory"
    arcpy.env.workspace = workspace

    output_date = datetime.datetime.now().strftime("%Y%m%d")

    output = arcpy.GetParameterAsText(0)
    if output == "#" or not output:
        output = r"D:\Projects\TreeProject\TreeProject.gdb\treecrops_{}".format(output_date)

    # Set more variables
    output_fc = output.split("\\")[-1]
    output_workspace = output.split(output_fc)[0][:-1]
    print(output_fc)
    print(output_workspace)

    # Create output FC if it doesn't exist
    if arcpy.Exists(output):
        pass
    else:
        print("Creating output feature class")
        arcpy.CreateFeatureclass_management(output_workspace, output_fc, "POLYGON", spatial_reference=4283)

    # For feature service connection
    # noinspection SpellCheckingInspection
    gis = GIS("http://arcgis.com", "jmckechn_une", "Leoj270592")
    print("Credentials verified: {}".format(gis))
    rest_url = "https://services5.arcgis.com/3foZbDxfCo9kcPwP/arcgis/rest/services/" \
               "TreeCrops_Editing/FeatureServer/0"
    # Try copying editing service to local gdb
    trees = output_workspace + "\\fs_download_{}".format(output_date)
    if arcpy.Exists(trees):
        arcpy.Delete_management(trees)
        print("Removing existing {}".format(trees))
    else:
        print("Copying from service: {}".format(rest_url))
        arcpy.CopyFeatures_management(rest_url, trees)
    print("Copy successful: {}".format(trees))

    # Copy data to memory and set up feature layer
    trees_memory = r"in_memory/trees"
    trees_lyr = "trees_lyr"
    query = "(commodity IS NOT NULL AND commodity <> 'other') AND (stage IS NULL OR stage = '1' OR stage = '2')"
    print("Copying data to memory")
    arcpy.CopyFeatures_management(trees, trees_memory)
    arcpy.MakeFeatureLayer_management(trees_memory, trees_lyr, where_clause=query)

    # Remove ag_ features if they exist
    rem_list = arcpy.ListFeatureClasses("ag_*")
    for i in rem_list:
        print("Deleting {}".format(i))
        arcpy.Delete_management(workspace+r"/"+i)

    # Get unique values
    print("Getting unique attributes from fields")
    field_list = ["commodity", "source", "year"]
    com_list = []
    for i in field_list:
        if i == "commodity":
            u_list = unique_values(trees_lyr, i)
            for j in u_list:
                com_list.append(j)
        else:
            pass
    # # Remove banana for speed :) (testing)
    # print("Remove banana for speed :) (testing)")
    # com_list.remove("banana")
    print(com_list)
    update_list = []

    print("Looping through selecting unique features to aggregate")
    for c in com_list:
        print("    Working on {} features".format(c))
        print("        selecting")
        selection_query = "commodity = '{}'".format(c)
        arcpy.SelectLayerByAttribute_management(trees_lyr, "NEW_SELECTION", selection_query)
        ag_output = "ag_{}".format(c)
        print("        aggregating")
        arcpy.AggregatePolygons_cartography(trees_lyr, ag_output,
                                            "25 METERS", "1 HECTARES", "1 HECTARES", "ORTHOGONAL")
        print("        Adding and calculating field")
        arcpy.AddField_management(ag_output, "commodity", "TEXT")
        arcpy.CalculateField_management(ag_output, "commodity", "'{}'".format(c), "ARCADE")
        print("            created {}".format(ag_output))

        # Copy aggregated features to output location
        print("            copying to output location")
        arcpy.CopyFeatures_management(ag_output, output+"_{}".format(c))
        update_list.append(output+"_{}".format(c))

    # make a list of ag_... feature classes and loop update analysis tool
    print("Joining features back together with update tool")
    loop_no = len(com_list)
    update_no = 0
    update_output = output+"_update{}".format(update_no)
    print("update_list: {}".format(update_list))
    print("loop_no: {}".format(loop_no))
    print("update_no: {}".format(update_no))
    print("update_output: {}".format(update_output))
    arcpy.CopyFeatures_management(update_list[0], update_output)
    while update_no+1 <= loop_no:
        loop_name = update_list[update_no].split("{}_".format(output_fc))[-1]
        print("    {} loop ({}/{})".format(loop_name, update_no+1, loop_no))

        if update_no == 0:
            arcpy.Update_analysis(update_output, update_list[update_no], output+"_update{}".format(update_no+1))
            print("        variables: {}, {}, {}".format(update_output, update_list[update_no],
                                                         output + "_update{}".format(update_no + 1)))
        else:
            arcpy.Update_analysis(output+"_update{}".format(update_no), update_list[update_no],
                                  output+"_update{}".format(update_no+1))
            print("        variables: {}, {}, {}".format(output+"_update{}".format(update_no), update_list[update_no],
                                                         output+"_update{}".format(update_no+1)))

        update_no += 1
    arcpy.CopyFeatures_management(output+"_update{}".format(loop_no), output)

    # join attributes back to output
    print("Trying spatial join")
    arcpy.SpatialJoin_analysis(output, trees_memory, output+"_join", "JOIN_ONE_TO_ONE")

    # Add hectare field
    arcpy.AddField_management(output+"_join", "hectares", "DOUBLE")
    arcpy.CalculateGeometryAttributes_management(output+"_join", [["hectares", "AREA_GEODESIC"]],
                                                 area_unit="HECTARES", coordinate_system=4283)

    # Overwrite output
    print("Explode, and overwriting output")
    arcpy.MultipartToSinglepart_management(output+"_join", output)

    # Clean up fields
    join_field_del_list = ["Join_Count", "TARGET_FID", "comment", "other", "stage", "edit",
                           "Shape__Area", "Shape__Length", "commodity_1", "ORIG_FID",
                           "field", "review", "imagery", "industry", "uncertain"]
    print("Deleting the following fields:")
    print(join_field_del_list)
    for i in join_field_del_list:
        arcpy.DeleteField_management(output, i)

    # Assign domains
    print("Assigning domains")
    arcpy.AssignDomainToField_management(output, "source", "source_domain")
    arcpy.AssignDomainToField_management(output, "commodity", "commodity_domain")
    arcpy.AssignDomainToField_management(output, "year", "year_domain")

    arcpy.env.workspace = output_workspace

    # Delete all working features except actual output, topology and original tree data.
    print("Trying to delete unnecessary data")
    del_fc_list = arcpy.ListFeatureClasses("{}_*".format(output_fc))
    print(del_fc_list)
    for i in del_fc_list:
        print("Deleting {}".format(i))
        arcpy.Delete_management(output_workspace+"\\{}".format(i))

    # Derive points
    print("Creating points")
    arcpy.FeatureToPoint_management(output_fc, output+"_point", "INSIDE")


if __name__ == "__main__":
    start_time = datetime.datetime.now()
    main()
    finish_time = datetime.datetime.now()
    arcpy.AddMessage("Script completed. Total time: {}".format(finish_time - start_time))
