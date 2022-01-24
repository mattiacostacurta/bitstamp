# Implementation of Bitstamp API

The Bitstamp project provides the user important information about daily
price movements and volume which can be utilized to gain insight into the
desired cryptocurrency. Data is provided by the Bitstamp API (full 
documentation at https://www.bitstamp.net/api/) and can be converted into
the available currencies.

The main functionalities include: 

- real time price;
- 24 hours average volume;
- daily % change;
- line chart of the last-hour price. 

## Installation

Use the command `git clone https://github.com/mattiacostacurta/bitstamp.git` in the command prompt of your PC in order to automatically download the whole folder containing the modules used. 
Git should have been previously installed on the machine. 
In alternative, just download manually the package from Github.

Moreover, some additional libraries/modules are required to run our project on the terminal are: 

- json
- request 
- pandas
- argparse
- csv
- matplotlib.pyplot
- currencyconverter
- datetime, 
- unittest
- sys
- os
- math

If these libraries/modules are not already installed in your pc, you can install them using the following command.

For example: 

```bash
pip install pandas
```

Pay attention some of them may require slightly different commands, search for them in their documentation.

For example: 

```bash
pip install --user currencyconverter
```

## Usage

The project's goal is to provide valuable information about the preferred cryptocurrency in order to keep the user up to date on daily price and volume fluctuations. 

Once a pair of `cryptocurrency` and `currency` is entered, the program checks if both codes are correct and present among the available currencies. If it is not, the program will kindly show the list of all the available crypto and FIAT currencies to ultimately choose among them.

The list of all the available crypto currencies is: 
```bash
['btc', 'eth', 'gbp', 'ada' , 'xrp', 'uni', 'ltc', 'link', 'matic', 'xlm', 'ftt', 'bch', 'aave', 'axs', 'algo', 'comp', 'snx', 'hbar', 'chz', 'cel', 'enj', 'bat', 'mkr', 'zrx', 'audio', 'skl', 'yfi' , 'sushi', 'alpha', 'storj', 'sxp', 'grt', 'uma', 'omg', 'knc', 'crv', 'sand', 'fet', 'rgt', 'slp', 'eurt', 'usdt', 'usdc', 'pax']
```

The list of all the availbale FIAT currencies is: 
```bash
['usd', 'jpy', 'bgn', 'cyp', 'czk', 'dkk', 'eek', 'gbp', 'huf', 'ltl', 'lvl', 'mtl', 'pln', 'rol', 'ron', 'sek', 'sit', 'skk', 'chf', 'isk', 'nok', 'hrk', 'rub', 'trl', 'try', 'aud', 'brl', 'cad', 'cny', 'hkd', 'idr', 'ils', 'inr', 'krw', 'mxn', 'myr', 'nzd', 'php', 'sgd', 'thb', 'zar']
```

In case both codes are correct, the program will perform *all* its functionalities through `main.py`. Indeed, the functions  `request_API`, `
create_table`, `read_csv` *******TO BE FIXED****** in the module `get_values.py` and all those inside the module `get_graph.py` are recalled inside it, as well as the ArgParse which stores the user inputs.  

So, if wanting the execute the program, the command should be written as follows:

```bash
python ./main.py 'cryptocurrency' 'currency'
``` 

*Please note* The program does *not* work unless the user inputs the currency codes he/she wants to convert.

For example: 

```bash
python ./main.py btc eur
```

In case the user is interested in a single data, he/she can add to the inputted currencies `-sd` or `--specific data` and the name of the specific functionality.

Using this command:

```bash
python ./main.py btc usd -sd 'functionality'
``` 

The list of all the available functionalities are: `'price'`, `'volume'`, `'change'` and `'chart'`. 

For example by writing:

```bash
python ./main.py btc eur -sd price
```

The result:

```bash
BTC EUR :  12234324,232
```

By default, if the user doesn’t specify which kind of data to get from the program, the latter returns all the possible information about the inputted cross (e.g. btc eur), included the price, the 24 hours % change and average volume, and the graph of the last hour.

For example by writing:

```bash
python ./main.py btc eur
```

The output will be:

```bash
BTC EUR
Price:  30891.74
Volume:  1460.39
Change:  -3.57  %
```

![btceur](btceur.jpg)

*Please note:* wait some seconds in order to let the program convert all values into the desired currency and ultimately return the line chart.

In case the program returns `'No data available'` or `'Not enough data to display a meaningful chart'` it means respectively that there is no data provided by the API or that there is not enough data provided by the API.


