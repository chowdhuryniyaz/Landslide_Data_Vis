import pandas as pd
from pandas.api.types import CategoricalDtype
import numpy as np

def load(file_path):
    column_names = ['id', 'date', 'time', 'continent_code', 'country_name', 'country_code',
                    'state_or_province', 'population', 'city_or_town', 'distance', 'location',
                    'latitude', 'longitude', 'geolocation', 'type_of_hazard', 'type_of_landslide',
                    'size_of_landslide', 'cause_of_landslide', 'storm_name', 'injuries', 'fatalities',
                    'source_name', 'source_link']

    df = pd.read_csv(file_path, index_col = 0 , names = column_names, skiprows = 1)

    to_drop = ['time', 'continent_code', 'location', 'latitude', 'longitude',
                'type_of_hazard', 'storm_name', 'source_name', 'source_link']

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
    df['injuries'] = df['injuries'].fillna(0.0).astype(np.int64)

    df['fatalities'] = df['fatalities'].fillna(0.0).astype(np.int64)

    return df