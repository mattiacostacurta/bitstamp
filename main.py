from get_values import request_API, create_table, read_csv
from converter import conversion, convert_table
import argparse
from prep_graph import request_API_txn, read_df, convert_table_graph, date_adjustment, get_price_chart
from get_graph import print_graph
import pandas as pd

parser = argparse.ArgumentParser()

crypto_list = ["btc", "eth", "gbp", "ada" , "xrp", "uni", "ltc", "link", "matic", "xlm", 
                "ftt", "bch", "aave", "axs", "algo", "comp", "snx", "hbar", "chz", "cel", 
                "enj", "bat", "mkr", "zrx", "audio", "skl", "yfi" , "sushi", "alpha", "storj", 
                "sxp", "grt", "uma", "omg", "knc", "crv", "sand", "fet", "rgt", "slp", "eurt", 
                "usdt", "usdc", "pax"]

currency_list = [ "usd", "eur", "jpy", "bgn", "cyp", "czk", "dkk", "eek", "gbp", "huf", "ltl", "lvl", "mtl", "pln", "rol", "ron", "sek", "sit", "skk", "chf", "isk", "nok", "hrk", "rub", "trl", "try", "aud", "brl", "cad", "cny", "hkd", "idr", "ils", "inr", "krw", "mxn", "myr", "nzd", "php", "sgd", "thb", "zar"]

parser.add_argument("crypto", help="Specify the cryptocurrency code", choices = crypto_list)
parser.add_argument("currency", help="Specify the currency code", choices = currency_list)
parser.add_argument("-sd","--specific_data", help="Specify which information you want to know", choices=["price", "volume", "change", "chart"])
parser.add_argument("-v","--verbose", help="Increase output verbosity", action="store_true")

args = parser.parse_args()

# This is the desired cryptocurrency+currency code of the user 
chosen_curr = args.crypto + args.currency

# For code purposes by default the chosen currency is EUR
value = args.crypto + "eur"

df = pd.DataFrame()
df = request_API(value)

if not create_table(df):
    sys.exit()
else:
    create_table(df)

if args.currency != "eur":
    convert_table(args.currency)


if args.specific_data == "price":
    if args.verbose:
        print("{} value in {} is {}".format(args.crypto.upper(), args.currency.upper(), read_csv('last')))
    else:
        print(args.crypto, args.currency, ":", read_csv('last'))
elif args.specific_data == "volume":
    if args.verbose:
        print("{} 24h volume is {}".format(args.crypto.upper(), read_csv('volume')))
    else:
        print(args.crypto.upper(), read_csv('volume'))
elif args.specific_data == "change":
    if args.verbose:
        print("{} daily change is {} %".format(args.crypto.upper(), read_csv('change')))
    else:
        print(args.crypto.upper(), read_csv('change'))
elif args.specific_data == "chart":
    if args.verbose:
        print_graph(chosen_curr)
    else:
        print_graph(chosen_curr)
else:
    if args.verbose:
        print("You have selected to see {} cryptocurrency in {}".format(args.crypto.upper(),    args.currency.upper()))
        print("{} last price in {} is {}".format(args.crypto.upper(), args.currency.upper(), read_csv('last')))
        print("{} 24h volume is {}".format(args.crypto.upper(), read_csv('volume')))
        print("{} daily change is {} %".format(args.crypto.upper(), read_csv('change')))
        print_graph(chosen_curr)
    else:
        print(args.crypto.upper(), args.currency.upper())
        print("Price: ", read_csv('last'))
        print("Volume: ", read_csv('volume'))
        print("Change: ", read_csv('change'), " %")
        print_graph(chosen_curr)
