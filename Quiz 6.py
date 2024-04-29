#Please write a python function that takes three inputs as and achieves the task defined below.

#calculatePercentAreaOfPolygonAInPolygonB(input_geodatabase, fcPolygonA, fcPolygonB, idFieldPolygonB):

#Given an input polygon feature class, fcPolygonA (e.g., parks), and a second feature class, fcPolygonB 
#(e.g., block_groups), and the id field of fcPolygonB so final calculation can be appended back to 
#fcPolygonB. In some solutions idFieldPolygonB may not be necessary, simply delete this third parameter.

#Calculate the percentage of the area of the first polygon features (fcPolygonA ) in the second polygon 
#features (fcPolygonB), and append the percentage of fcPolygonA (e.g., park area) into a new field in 
#fcPolygonB (e.g., the block groups) feature class.
#Make sure that your area calculations are as accurate as possible. 

import arcpy
import os

folder = 'C:/Users/croe1/OneDrive - University of Iowa/Desktop/Class Stuff/Geospatial Programming/Quiz 6/quiz6.gdb'

arcpy.env.workspace = folder
arcpy.env.overwriteOutput = True

print(arcpy.env.workspace)

#create parks variable
arcpy.AddField_management("parks", "areasqm", "DOUBLE")
parks = "parks"

#create block groups variable
arcpy.AddField_management("block_groups", "areasqm", "DOUBLE")
block_groups = "block_groups"

#intersect parks and block groups
pibg = "parks_intersect_block_groups"
arcpy.Intersect_analysis([block_groups, parks], pibg)

# calculate area of block groups in parks in square miles
blarea = "block_area"
arcpy.AddField_management(pibg, blarea, "DOUBLE")
arcpy.CalculateGeometryAttributes_management(pibg, [[blarea, "AREA_GEODESIC"]], "MILES_US")

parks_dict = dict()
with arcpy.da.SearchCursor(pibg, ["FIPS", blarea]) as cursor:
    for row in cursor:
        geoid = row[0]
        if geoid in parks_dict.keys():
            parks_dict[geoid] += row[1]
        else:
            parks_dict[geoid] = row[1] 

#calculate area of parks in block group in square miles
parea = "parks_area"
arcpy.AddField_management(block_groups, parea, "DOUBLE")
arcpy.management.CalculateGeometryAttributes(block_groups, [[parea, "AREA_GEODESIC"]], "MILES_US")

#calculate area of parks in each block group
with arcpy.da.UpdateCursor(block_groups, ["FIPS", parea]) as cursor:
    for row in cursor:
        if row[0] in parks_dict.keys():
            row[1] = parks_dict[row[0]]
        else:
            row[1] = 0
        cursor.updateRow(row)

#calculate area of block groups in square miles
barea = "block_area"
arcpy.AddField_management(block_groups, barea, "DOUBLE")
arcpy.CalculateGeometryAttributes_management(block_groups, [[barea, "AREA_GEODESIC"]], "MILES_US")

#calculate percentage of block group that is park
park_pct = "park_pct"
arcpy.AddField_management(block_groups, park_pct, "DOUBLE")
arcpy.CalculateField_management(block_groups, park_pct, "!parks_area!/!block_area!", "PYTHON3")


