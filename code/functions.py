## Importing modules necessary modules for my functions
import pandas as pd
import os
import json
import requests
import numpy as np

## Creating a function that will give me the latitude and longitude when I enter the country code and city name
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

## Function to print the latitude and longitude of a country, city
def print_location_lat_lon(country, city):
    latitude, longitude = get_lat_lon(country, city)
    print(f"The latitude and longitude of {country}, {city} is ({latitude}, {longitude})")

## Creating a function that builds an API URL for historical weather data when I put in the latitude, longitude, start and end dates
def build_url(latitude: float, longitude: float, start_date:str , end_date: str):
    base_historical_url = "https://archive-api.open-meteo.com/v1/archive?"
    params_lat_long     = "latitude=" + str(latitude) + "&longitude="  + str(longitude)
    params_date         = "&start_date=" + start_date + "&end_date=" + end_date

    params_others       = "&daily=rain_sum&timezone=auto"

    final_url = base_historical_url + params_lat_long + params_date + params_others

    return final_url

## Creating a function that uses the previous functions to automatically get historical weather forecast data
def get_historical_data(country_code, city_name, start_date, end_date):

    latitude, longitude = get_lat_lon(country_code, city_name)

    url = build_url(latitude, longitude, start_date, end_date)

    response = requests.get(url)

    historical_data = response.json()
    return historical_data


def get_city_data(df, city_name):
    return df[df['city'] == city_name]