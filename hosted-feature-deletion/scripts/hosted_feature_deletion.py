from arcgis.features.layer import FeatureLayer, Table
from arcgis.gis import GIS
import pandas as pd
from pandas import DataFrame

def bulk_delete(arcgis_hosted_asset: FeatureLayer | Table,
                data_to_delete: DataFrame,
                oid_column: str = 'OBJECTID') -> dict:
    '''
    A function to iterate through large delete operations and handle them
    in batched requests of 2,000 or less.
    
    ##Inputs
    1. arcgis_hosted_asset: FeatureLayer | Table
         - The arcgis.features.layer FeatureLayer or Table object
         for the service being deleted from
    4. data_to_delete: pandas.DataFrame
         - A pandas dataframe containing all features that should
         be deleted from the hosted feature layer ot table
    5. oid_column: str
         - The column name for the objectid column on the hosted
         layer ot table. Default is 'OBJECTID'
    '''
    #resetting index to ensure 0 starting position
    features_to_delete = data_to_delete.reset_index()
    
    max_index = len(features_to_delete) - 1
    
    print(f'Identified {len(features_to_delete)} to delete.')
    
    prev_index = 0
    
    while (prev_index + 2000) < max_index:
        next_index = prev_index + 2000
        print(f'Deleting features {prev_index} - {next_index}')
        
        subset = features_to_delete.iloc[prev_index:next_index]
        oids = list(subset[oid_column])
        arcgis_hosted_asset.edit_features(deletes=oids)
        
        prev_index += 2000
        
    #while loop terminates when remaining features to delete less than 200
    print(f'Deleting features {prev_index} - {max_index}')
    subset = features_to_delete[prev_index : max_index]
    oids = list(subset[oid_column])
    arcgis_hosted_asset.edit_features(deletes=oids)
    
    print('All items deleted.')