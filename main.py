from get_values import create_table, get_price, get_volume, get_change
from converter import conversion, convert_table
import argparse
from prep_graph import get_price_chart


parser = argparse.ArgumentParser()

crypto_list = ["btc", "eth", "gbp", "ada" , "xrp", "uni", "ltc", "link", "matic", "xlm", 
                "ftt", "bch", "aave", "axs", "algo", "comp", "snx", "hbar", "chz", "cel", 
                "enj", "bat", "mkr", "zrx", "audio", "skl", "yfi" , "sushi", "alpha", "storj", 
                "sxp", "grt", "uma", "omg", "knc", "crv", "sand", "fet", "rgt", "slp", "eurt", 
                "usdt", "usdc", "pax"]

currency_list = [ "usd", "jpy", "bgn", "cyp", "czk", "dkk", "eek", "gbp", "huf", "ltl", "lvl", "mtl", "pln", "rol", "ron", "sek", "sit", "skk", "chf", "isk", "nok", "hrk", "rub", "trl", "try", "aud", "brl", "cad", "cny", "hkd", "idr", "ils", "inr", "krw", "mxn", "myr", "nzd", "php", "sgd", "thb", "zar"]

parser.add_argument("crypto", help="Specify the cryptocurrency code", choices = crypto_list)
parser.add_argument("currency", help="Specify the currency code", choices = currency_list)
parser.add_argument("-sd","--specific_data", help="Specify which information you want to know", choices=["price", "volume", "change", "chart"])

args = parser.parse_args()

value = args.crypto + "eur"
create_table(value)

if args.currency != "eur":
    convert_table(args.currency)

if args.specific_data == "price":
    print("{} value in {} is {}".format(args.crypto, args.currency, get_price()))
elif args.specific_data == "volume":
    print("{} 24h volume is {}".format(args.crypto, get_volume()))
elif args.specific_data == "change":
    print("{} daily change is {} %".format(args.crypto, get_change()))
elif args.specific_data == "chart":
    get_price_chart(value)
else:
    print("{} value in {} is {}".format(args.crypto, args.currency, get_price()))
    print("{} 24h volume is {}".format(args.crypto, get_volume()))
    print("{} daily change is {} %".format(args.crypto, get_change()))
    get_price_chart(value)
    