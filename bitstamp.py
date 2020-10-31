import requests
import json


bitstamp_URL = 'https://www.bitstamp.net/api/v2/ticker/%s/'

def get_price(currency="btceur"):
    r = requests.get(bitstamp_URL % currency)
    price = float(json.loads(r.text)['last'])
    return price
