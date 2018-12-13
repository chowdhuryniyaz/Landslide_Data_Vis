import pandas as pd
from pandas.api.types import CategoricalDtype
import numpy as np

def load(file_path):
    column_names = ['id', 'date', 'time', 'continent_code', 'country_name', 'country_code',
    'state_or_province', 'population', 'city_or_town', 'distance', 'type_of_area',
    'latitude', 'longitude', 'geolocation', 'type_of_hazard', 'type_of_landslide',
    'size_of_landslide', 'cause_of_landslide', 'storm_name', 'injuries', 'fatalities',
    'source_name', 'source_link']

    df = pd.read_csv(file_path, index_col = 0 , names = column_names, skiprows = 1)

    to_drop = ['time', 'continent_code', 'latitude', 'longitude', 'geolocation', 'type_of_hazard', 'storm_name', 'source_name', 'source_link']

    df = dropColumn(df, to_drop)

    df['type_of_landslide'] = df['type_of_landslide'].str.capitalize()
    df['size_of_landslide'] = df['size_of_landslide'].str.capitalize()
    df['cause_of_landslide'] = df['cause_of_landslide'].str.capitalize()

    return df

def dropColumn(df, columns):
    for i in columns:
        df.drop(columns=[i], inplace = True)
    
    return df

def changeDataType(df):
    df['date'] = pd.to_datetime(df['date'])

    df['distance'] = df['distance'].fillna(0.000).round(3).astype(np.float64)

    area_types = CategoricalDtype(ordered = False, categories = ['Above river', 'Above road', 'Below road', 'Bluff', 'Burned area', 'Deforested slope',
                        'Mine construction', 'Natural slope', 'Other', 'Retaining wall' , 'Unknown', 'Urban area'])
    df['type_of_area'] = df['type_of_area'].fillna('Unknown').astype(area_types)

    landslide_types = CategoricalDtype(ordered = False, categories = ['Landslide', 'Riverbank collapse', 'Mudslide', 'Complex', 'Debris flow',
                        'Rockfall', 'Lahar', 'Creep', 'Avalanche', 'Other', 'Unknown', 'Rockslide'])
    df['type_of_landslide'] = df['type_of_landslide'].fillna('Unknown').astype(landslide_types)

    landslide_sizes = CategoricalDtype(ordered = False, categories = ['Small', 'Medium', 'Large', 'Very Large'])
    df['size_of_landslide'] = df['size_of_landslide'].fillna('Unknown').map({'Small': 'Small', 'Medium': 'Medium', 'Large': 'Large', 'Very_large': 'Very Large'}).astype(landslide_sizes)

    landslide_causes = CategoricalDtype(ordered = False, categories = ['Construction', 'Continuous rain', 'Dam embankment collapse', 'Downpour',
                            'Earthquake', 'Flooding', 'Freeze thaw', 'Mining digging', 'Other', 'Rain', 'Snowfall snowmelt', 'Tropical cyclone', 'Unknown', 'Volcano'])
    df['cause_of_landslide'] = df['cause_of_landslide'].fillna('Unknown').astype(landslide_causes)

    df['injuries'] = df['injuries'].fillna(0.0).astype(np.int64)

    df['fatalities'] = df['fatalities'].fillna(0.0).astype(np.int64)

    return df