'''
The aim of this module is to retrieve data from the bitstamp API,
convert it to a csv file, and retrieve values depending on the input
of the user
'''

import requests
import json
import pandas as pd


bitstamp_URL = 'https://www.bitstamp.net/api/v2/ticker/%s/'


def request_API(value):
    '''
    This function requests data from bitstamp API
    and returns it as a dataframe
    '''
    r = requests.get(bitstamp_URL % value)
    if r.status_code == 200:
        file_json = json.loads(r.text)
        df = pd.DataFrame(file_json, index=[0])
        return df
    return None


def create_table(df):
    '''
    This function creates a csv file using the previous dataframe.
    It checks whether the function receives a dataframe in input, 
    otherwise it returns False
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


def read_csv(input):
    '''
    This function reads CryptoTable.csv file and returns the value
    received in input by the user.
    If the input is different from the valid inputs, it returns False
    '''
    df = pd.read_csv('CryptoTable.csv')
    if input == "last":
        last_price = df._get_value(0, 'last')
        return round(last_price, 2)
    elif input == "volume":
        volume = df._get_value(0, 'volume')
        return round(volume, 2)
    elif input == "change":
        open_price = df._get_value(0, 'open')
        last_price = df._get_value(0, 'last')
        return round((last_price-open_price)/last_price*100, 2)
    else:
        print('The input typed is not supported')
        return None
