import requests
import json
import pandas as pd


bitstamp_URL = 'https://www.bitstamp.net/api/v2/ticker/%s/'


def request_API(value):
    r = requests.get(bitstamp_URL % value)
    if r.status_code == 200:
        file_json = json.loads(r.text)
        df = pd.DataFrame(file_json, index=[0])
        return df
    return None


def get_price():
    df = pd.read_csv('CryptoTable.csv')
    last_price = df._get_value(0, 'last')
    return last_price


def get_volume():
    df = pd.read_csv('CryptoTable.csv')
    volume = df._get_value(0, 'volume')
    return volume


def get_change():
    df = pd.read_csv('CryptoTable.csv')
    open_price = df._get_value(0, 'open')
    last_price = df._get_value(0, 'last')
    return (last_price-open_price)/last_price*1004
