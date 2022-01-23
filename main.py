from get_values import create_table, get_price, get_volume, get_change
import argparse

parser = argparse.ArgumentParser()

crypto_list = ["btc", "eth", "gbp", "ada" , "xrp", "uni", "ltc", "link", "matic", "xlm", 
                "ftt", "bch", "aave", "axs", "algo", "comp", "snx", "hbar", "chz", "cel", 
                "enj", "bat", "mkr", "zrx", "audio", "skl", "yfi" , "sushi", "alpha", "storj", 
                "sxp", "grt", "uma", "omg", "knc", "crv", "sand", "fet", "rgt", "slp", "eurt", 
                "usdt", "usdc", "dai", "pax", "eth2", "gusd"]


currency_list = [ "usd", "jpy", "bgn", "cyp", "czk", "dkk", "eek", "gbp", "huf", "ltl", "lvl", "mtl", "pln", "rol", "ron", "sek", "sit", "skk", "chf", "isk", "nok", "hrk", "rub", "trl", "try", "aud", "brl", "cad", "cny", "hkd", "idr", "ils", "inr", "krw", "mxn", "myr", "nzd", "php", "sgd", "thb", "zar"]


parser.add_argument("crypto", help="Specify the cryptocurrency code", choices = crypto_list)
parser.add_argument("currency", help="Specify the currency code", choices = currency_list)
parser.add_argument("-sd","--specific_data", help="Specify which information you want to know", choices=["price", "volume", "change", "chart"])
args = parser.parse_args()
print(args.crypto, args.currency, args.specific_data)

create_table(“btcusd”)