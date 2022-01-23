from prep_graph import get_data, convert_table_graph, date_adjustment, get_price_chart

def print_graph(chosen_curr):
    if isinstance(get_file(chosen_curr), str):
        print('No data available to print a chart')
    else:
        return get_price_chart(date_adjustment(convert_table_graph(get_file(chosen_curr),chosen_curr)),chosen_curr)
