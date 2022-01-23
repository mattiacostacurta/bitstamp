import pandas as pd
from currency_converter import CurrencyConverter

def conversion(price, default_currency, output_currency):
   c = CurrencyConverter()
   default_currency = default_currency.upper() 
   output_currency = output_currency.upper()
   converted_price = c.convert(price, default_currency, output_currency)
   return converted_price

