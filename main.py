from bitstamp import get_price

eur=get_price("btceur")
print("Last bitcoin price in EUR is: {}".format(eur))
dollar=get_price("btcusd")
print("Last bitcoin price in $ is: {}".format(dollar))


