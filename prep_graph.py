import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from converter import conversion

bitstamp_URL = "https://www.bitstamp.net/api/v2/transactions/%s/"

def get_file(chosen_curr):
    out_curr = chosen_curr[-3:]
    curr = 'eur'
    n_val = chosen_curr[0:-3] + curr
    r = requests.get(bitstamp_URL % n_val)
    file_json = json.loads(r.text)
    df = pd.DataFrame(file_json)
    df.to_csv (r"Price.csv", index = False, header=True)
    price_df = pd.read_csv("Price.csv")
    price_df = price_df.sort_values(by=['date'], ascending=True)
    return price_df

def convert_table_graph(df, chosen_curr):
    output_currency = chosen_curr[-3:]
    
    if output_currency != 'eur':
        new_list = []
        for el in df['price']:
            new_el = round((conversion(el, output_currency)),2)
            new_list.append(new_el)
        df['price'] = new_list
    return df

def date_adjustment(df):
    """The dataframe expresses data and time using timestamp. We want to convert it in simply date and 
    time and put them in different columns, to better manage data."""
    dates = []
    for date in price_df["date"]:
        date = int(date)  
        date = datetime.fromtimestamp(date).strftime("%d-%m-%Y %H:%M:%S")
        dates.append(date)
    price_df["Date and time"] = dates
    price_df[['Date', 'Time']] = price_df['Date and time'].str.split(' ', n=1, expand=True)
    price_df = price_df.drop(["Date and time", "date"], axis = 1)
    return df

def get_price_chart(df, chosen_curr):
    """Since the graph will display an entire hour of variation of prices, minute by minute, we want to
    select only some important time-references to make the graph more readable."""
    timing = price_df["Time"].tolist()
    time_values =[] 
    # division for 6, we want to consider more or less every 10 minutes
    for n in range (0, len(df), int(len(df)/6)):
        time_values.append(timing[n])
    date=price_df["Date"][0]
    
    plot = plt.figure(figsize=(15, 7))
    plot = plt.plot("Time","price", data=price_df)
    plot = plt.title("Last hour " + chosen_curr.upper() + " price | "+ date)
    plot = plt.title("Price of " + value + " for "+ date)
    plot = plt.xticks(time_values, time_values)
    plot = plt.show()
    return plot