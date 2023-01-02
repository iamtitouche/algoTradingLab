#!/usr/env/bin python3


import ccxt


API_KEY = 'qbuciCofHfXNIET2WbyQHj2orZi3IMzcBwKu2FQ7aQLOsevzlxu72fCh0irjP6W8'
API_SECRET = 'PGQKwF9TrESDGEdQlvp36diacIQhuDvkPBbPJdMhf3YBw0XGKgnAHSTrdZId7c6K'


LOGGING_INFOS = {
    'enableRateLimit': True,
    'apiKey': API_KEY,
    'secret': API_SECRET
}


binance = ccxt.binance(LOGGING_INFOS)

print(binance.fetch_balance())


