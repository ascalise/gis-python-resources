from arcgis.gis import GIS
from arcgis.gis import Item
from arcgis.features import FeatureLayerCollection
class SchemaManager:
    def __init__(self,
                 feature_service: Item) -> dict:
        '''
        A class for managing feature layer with dependent views that cause
        schema locks in ArcGIS Online.
        
        ##Inputs
        1. feature_service
            - Item from ArcGIS Online that has schema lock and dependent views.
        ##Returns
        1. Class object SchemaManager.
        '''
        self.views = feature_service.view_manager.list()
        
        result = {
            'views' : self.views
        }
        
        print(result)
        
       
    def unlock_schema(self) -> dict:
        '''
        ##Return
        - A dictionary containing a status key and a props key. 
        Update status can be verified with the status key and further validation can
        be provided using the props key to review the targeted attributes.
        '''
        
        #convert item to flc to access and manipulate properties
        
        results = {}
        for item in self.views:
            flc = FeatureLayerCollection.fromitem(item)
            
            updates = {'sourceSchemaChangesAllowed' : True,
                    'hasStaticData' : False,
                    'lastEditDate' : ''}
            
            status = flc.manager.update_definition(updates)
            
            output = {'status' : status}
            self.update_props = flc.properties
            
            results[flc.properties['serviceItemId']] = output
        
        return results

    def lock_schema(self) -> dict:
        '''
        ##Return
        - A dictionary containing a status key and a props key. 
        Update status can be verified with the status key and further validation can
        be provided using the props key to review the targeted attributes.
        '''
        
        
        #convert item to flc to access and manipulate properties
        results = {}
        for item in self.views:
            flc = FeatureLayerCollection.fromitem(item)
            updates = {'sourceSchemaChangesAllowed' : False,
                    'hasStaticData' : True,
                    'lastEditDate' : ''}
            
            status = flc.manager.update_definition(updates)
            
            output = {'status' : status}
            self.update_props = flc.properties
            
            results[flc.properties['serviceItemId']] = output
        
        return results