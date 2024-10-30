import pandas as pd
import os
import json
import requests
import numpy as np
import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

def get_lat_lon(country_code, city):
    
    filepath = '../data/world_cities.csv'
    world_cities = pd.read_csv(filepath)

    city_data = world_cities[(world_cities['country'] == country_code) & 
                             (world_cities['name'] == city)]
    
    city_data = city_data.to_dict('records')
    
    if len(city_data) == 0:
        raise ValueError(f"No records found for {city}, {country_code} in {filepath}")

    latitude = city_data[0]['lat']
    longitude = city_data[0]['lng']

    return latitude, longitude

