#Upload a python file (py) that creates variable buffers 
#using airports shapefile. If the value of the 
#FEATURE field in the airport shapefile is: 
#"seaplane" then create a 7,500-meter buffer 
#"airport" then create a 15,000 meter buffer.
#For other values do not create buffers. 
#Save the buffers into buffer_airports shapefile. 

import arcpy

print(arcpy.env.workspace)

folder = 'C:\\Users\\croe1\\OneDrive - University of Iowa\\Desktop\\Class Stuff\\Geospatial Programming\\Quiz 5'

arcpy.env.workspace = folder

print(arcpy.env.workspace)

fcList = arcpy.ListFeatureClasses()

print(fcList)

fcAirport = 'airports'

print(fcAirport)

fcAFields = arcpy.ListFields(fcAirport)
for field in fcAFields:
    print(field.name)

fields = ['FEATURE']

with arcpy.da.SearchCursor(fcAirport, fields) as cursor:
    for row in cursor:
       print(f'{row[0]}')

fields = ['FEATURE']
airtype = set()

count = 0
with arcpy.da.SearchCursor(fcAirport, fields) as cursor:
    for row in cursor:
        airtype.add(row[0])
print(airtype)

arcpy.management.AddField(fcAirport, 'buffer', 'LONG')

fields.append('buffer')
print(fields)

typelist = list(airtype)

print(typelist)

#"seaplane" = 7,500 meter buffer 
#"airport" = 15,000 meter buffer.
with arcpy.da.UpdateCursor(fcAirport, fields) as cursor:
    for row in cursor:   
        if row[0] in typelist[1]:
            row[1] = 7500
        else:
            row[1] = 15000
        cursor.updateRow(row)

#check that buffers got set correctly
fieldsb = ['buffer']

with arcpy.da.SearchCursor(fcAirport, fieldsb) as cursor:
    for row in cursor:
       print(f'{row[0]}')

#save buffers as buffer_airports shapefile
arcpy.conversion.ExportFeatures('airports', 'buffer_airports.shp')


