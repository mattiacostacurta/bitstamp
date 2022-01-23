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


def create_table(df):
    '''
    This function creates a csv file to fetch 
    data from bitstamp API and store it in a table
    '''
    if df is None:
        print('Error: API request unsuccessful')
        return False
    elif df.empty:
        print('Error: No data available')
        return False
    elif df.shape != (1,9):
        print('Error: Table with different shape')
        return False
    #elif df[0]['open'] <= 0 or df[0]['last'] <= 0:
        #print('Error: Opening and last price less than zero')
        #return False
    else:
        df.to_csv (r'CryptoTable.csv', index = False, header=True)
        return True


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
