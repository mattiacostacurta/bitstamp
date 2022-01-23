import sys
import pandas as pd
from prep_graph import request_API_txn, read_df, convert_table_graph, date_adjustment, get_price_chart

def print_graph(chosen_curr):
    response = request_API_txn(chosen_curr)
    data = read_df(response)

    if isinstance(data, str):
        print(data)
        return None

    elif isinstance(data, pd.DataFrame):
        converted_df = convert_table_graph(data,chosen_curr)
        final_df = date_adjustment(converted_df)
        return get_price_chart(final_df,chosen_curr)

    else:
        print('Error: not possible to print a chart.')
        sys.exit()