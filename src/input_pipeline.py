import numpy as np
import pandas as pd
import requests
import json


def convert_to_datetime(df):
    df['Meldedatum'] = pd.to_datetime(df['Meldedatum'], unit='ms')
    return df

def convert_to_date(df):
    df['Meldedatum'] = pd.to_datetime(df['Meldedatum']).dt.date
    return df

def remove_nicht_erhoben(df):
    df = df[df.Bundesland != '-nicht erhoben-']
    df = df[df.Landkreis != '-nicht erhoben-']
    return df

def get_data():
    # Load data from RKI
    response = requests.get("https://opendata.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0.geojson")
    raw_data = pd.DataFrame([x['properties'] for x in json.loads(response.text)['features']])
    cleaned_data = (raw_data
                .pipe(convert_to_date)
                .pipe(remove_nicht_erhoben)
               )
    return cleaned_data