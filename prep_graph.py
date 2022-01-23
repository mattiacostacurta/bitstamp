""""
This module includes all the functions needed to prepare the last-hour 
pricing chart of the user's chosen cryptocurrency converted in the 
desired currency. In terms of data, we must first request and collect 
data from the API, then save them in a CSV file, and finally convert 
them into another currency if the user requests it. Once the data is 
ready, we can proceed to format them and finally return the chart 
whenever possible.
"""

import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from converter import conversion

bitstamp_URL = 'https://www.bitstamp.net/api/v2/transactions/%s/'

def request_API_txn(chosen_curr):
    """
    This function requests and collects data from the API, after 
    changing the currency in USD. It checks if the data request is 
    successful or not. If it is so, it returns the dataframe of 
    information collected, otherwise None. 
    """
    # Check of valid input, it needs to be a string
    # Even if it is already controlled by argparse
    if type(chosen_curr)!= str:
        return None

    curr = 'eur'
    n_val = chosen_curr[0:-3] + curr
    r = requests.get(bitstamp_URL % n_val)
    # Check if the request have been successful 
    # 200 means OK
    if r.status_code == 200:
        file_json = json.loads(r.text)
        df = pd.DataFrame(file_json)
        return df
    
    else:
        return None

def read_df(df):
    """
    This function checks if the passed dataframe can be valid in terms 
    of data contained to create the graph. Otherwise, it displays some 
    error messages useful for the user and for other functions. 
    """
    # Check if the passed dataframe is actually a dataframe
    if isinstance(df, pd.DataFrame): 
        # Dataframe is empty, no data to store in a CSV file
        # API has not collected information for this hour slot
        if len(df)==0:
            return 'No data available.'
        else:
            df.to_csv (r'Price.csv', index = False, header=True)
            price_df = pd.read_csv('Price.csv')
            price_df = price_df.sort_values(by=['date'], ascending=True)
            return price_df
    
    # If the previous API request is not achieved, it gives an error
    elif df is None:
        return 'API request failed.'
    
    # In any other different case, return None
    else:
        return False

def convert_table_graph(df, chosen_curr):
    """
    This function simply takes the inputted data frame and converts 
    it to the currency chosen whenever it is different from EUR. 
    """
    output_currency = chosen_curr[-3:]
    
    if output_currency != 'eur':
        new_list = []
        for el in df['price']:
            new_el = round((conversion(el, output_currency)),2)
            new_list.append(new_el)
        df['price'] = new_list
    return df

def date_adjustment(df):
    """
    Since the API expresses the date and time of data using the 
    timestamp convention, the function converts them into the normal 
    format and split them into different columns to make data more 
    manageable. 
    """
    dates = []
    for date in df['date']:
        date = int(date)  
        date = datetime.fromtimestamp(date).strftime('%d-%m-%Y %H:%M:%S')
        dates.append(date)
    df['Date and time'] = dates
    df[['Date', 'Time']] = df['Date and time'].str.split(' ', n=1, expand=True)
    df = df.drop(['Date and time', 'date'], axis = 1)
    return df

def get_price_chart(df, chosen_curr):
    """
    This function takes the inputted dataframe and chosen cryptocurrency 
    and currency and according to the length of the dataframe it decides 
    if data are enough or not to show a suitable chart. 
    """
    timing = df['Time'].tolist()
    time_values =[] 

    # Less than 15 entries in the dataframe are not enough
    if len(df)<15: 
        print('Not enough data to display a meaningful chart.')

    # Since there could be too much values in an entire hour variation 
    # we want to select only some time references for the x axis to 
    # make the graph more readable
    else:
        # Division for 6, consider more or less every 10 minutes
        for n in range (0, len(df), int(len(df)/6)):
            time_values.append(timing[n])
        date=df['Date'][0]
    
        plot = plt.figure(figsize=(15, 7))
        plot = plt.plot('Time','price', data=df)
        plot = plt.title('Last hour ' + chosen_curr.upper() + ' price | '+ date)
        plot = plt.xticks(time_values, time_values)
        plot = plt.show()
        return