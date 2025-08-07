'''
Once the .lock_schema() method is called, the feature service
fields will no longer be editable.
'''
from arcgis.gis import GIS
from .scripts.schemaLockTool import SchemaManager

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

#lock schema
managed_item.lock_schema()