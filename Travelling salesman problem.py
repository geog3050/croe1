import arcpy

data = r"E:\MyProject\chp11data"

project = r"E:\MyProject\MyProject.gdb"

arcpy.env.workspace = project

roads_shp = data + "/roads.shp"

desc = arcpy.Describe(roads_shp)

print(desc.spatialReference.name)

arcpy.CheckOutExtension("network")

out_name = "featuredataset"

arcpy.CreateFeatureDataset_management(project, out_name, desc.spatialReference)

arcpy.CopyFeatures_management(roads_shp, project + "/featuredataset/roads")

stops_shp = data + "/stops.shp"

print(arcpy.Describe(stops_shp).spatialReference.name)

arcpy.CopyFeatures_management(stops_shp, project + "/featuredataset/stops")

arcpy.na.CreateNetworkDataset(project + "/featuredataset", "roads_ND", ["roads"])

arcpy.BuildNetwork_na("/featuredataset/roads_ND")

routeLy = arcpy.na.MakeRouteAnalysisLayer("/featuredataset/roads_ND", "myRoute", "Length", "FIND_BEST_ORDER")

routeLy = routeLy.getOutput(0)

naClasses = arcpy.na.GetNAClassNames(routeLy, "INPUT")

print(naClasses)

fieldMappings = arcpy.na.NAClassFieldMappings(routeLy, naClasses["Stops"])

fieldMappings

fieldMappings["Attr_Length"].defaultValue = 0

arcpy.na.AddLocations(routeLy, "Stops", "featuredataset/stops", fieldMappings)

arcpy.na.Solve(routeLy)


