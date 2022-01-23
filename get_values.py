import requests
import json
import pandas as pd


bitstamp_URL = 'https://www.bitstamp.net/api/v2/ticker/%s/'


def create_table(value):
    r = requests.get(bitstamp_URL % value)
    file_json = json.loads(r.text)
    df = pd.DataFrame(file_json, index=[0])
    df.to_csv (r'CryptoTable.csv', index = False, header=True)
