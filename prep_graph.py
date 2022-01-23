import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

bitstamp_URL = "https://www.bitstamp.net/api/v2/transactions/%s/"

def get_price_chart(value): 
    r = requests.get(bitstamp_URL % value)
    file_json = json.loads(r.text)
    df = pd.DataFrame(file_json)
    df.to_csv (r"Price.csv", index = False, header=True)
    price_df = pd.read_csv("Price.csv")
    
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
    
    """Since the graph will display an entire hour of variation of prices, minute by minute, we want to
    select only some important time-references to make the graph more readable."""
    timing = price_df["Time"].tolist()
    time_values =[] 
    # division for 6, we want to consider more or less every 10 minutes
    for n in range (0, len(price_df)+1, int(len(price_df)/6)):
        time_values.append(timing[n])
    date=price_df["Date"][0]
    
    plot = plt.figure(figsize=(15, 7))
    plot = plt.plot("Time","price", data=price_df)
    plot = plt.title("Price of " + value + " for "+ date)
    plot = plt.xticks(time_values, time_values)
    plot = plt.show()
    return plot