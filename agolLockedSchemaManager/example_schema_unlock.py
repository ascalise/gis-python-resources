from arcgis.gis import GIS
from scripts.schemaLockTool import SchemaManager

#credential to authenticate with the arcgis python module
org_url = "https://myorg.maps.arcgis.com"
un = "username"
pw = "password"

#item id for the feature service with locked schema
feature_service_id = "12345678910"

#authenticate and create gis object to interact with content
gis = GIS(org_url, un, pw)

#gets item to pass to SchemaManager class
locked_item = gis.content.get(feature_service_id)

#initiate class
managed_item = SchemaManager(locked_item)

#unlock schema
managed_item.unlock_schema()

'''
At this point, the AGOL Feature Service you are interacting with should be
able to be interacted with. You can add to the domain of a field,
add a field, etc. If you don't immediately see the desired functions
available in the AGOL interface, make sure to refresh your browser.
'''

'''
Once you are done making the necesarry edits, you should invoke the
lock_schema() method to ensrue the service definitions are restored
to their original state. Once the metho has been invoked, you should
be able to refresh your browser and see that you can no longer
edit fields in the AGOL interface.
'''