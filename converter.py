'''
The aim of this module is to convert cryptocurrency values
to other currency not supported in the bitstamp API, hence to
expand the usability of the program to other countries
'''
import pandas as pd
from currency_converter import CurrencyConverter

def conversion(price, output_currency):
   '''
   This function convert values from the original 
   currency to the currency specified by the user
   '''
   c = CurrencyConverter()
   output_currency = output_currency.upper()
   converted_price = c.convert(price, output_currency)
   return converted_price

def convert_table(output_currency):
   '''
   This function uses the conversion function to convert 
   values such as opening price and last price
   '''
   df = pd.read_csv('CryptoTable.csv')
   df['last'] = conversion(df._get_value(0, 'last'), output_currency)
   df['open'] = conversion(df._get_value(0, 'open'), output_currency)
   df.to_csv (r'CryptoTable.csv', index = False, header=True)
   