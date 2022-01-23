""""
This module contains a single function whose goal is to show the last 
hour price graph when data is available or when not return error 
messages to the user. To do so, it exploits the functions previously 
created in the prep_graph module. 
"""

import sys
import pandas as pd
from prep_graph import request_API_txn, read_df, convert_table_graph, date_adjustment, get_price_chart

def print_graph(chosen_curr):
    """
    The function takes the combination of crypto and currency desired by
    the user and computes the prep_graph functions. The situations can 
    be 3: no graph and some type of error displayed connected to the 
    unavailability of data or the failed API request (like "No data 
    available" or "API request failed" in the get_data function), the 
    successful display of the graph (if enough data are available) and, 
    lastly,no graph, massive error and exit from the program due to the
    wrong format of the dataframe
    """ 
    response = request_API_txn(chosen_curr)
    data = read_df(response)

    # If there are unavailable data or fail requests
    if isinstance(data, str):
        print(data)
        return None

    # Dataframe is good, it is possible to proceed with the chart
    elif isinstance(data, pd.DataFrame):
        converted_df = convert_table_graph(data,chosen_curr)
        final_df = date_adjustment(converted_df)
        return get_price_chart(final_df,chosen_curr)

    # Wrong format of dataframe
    else:
        print('Error: not possible to print a chart.')
        sys.exit()