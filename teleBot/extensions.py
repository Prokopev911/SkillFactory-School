import requests
import json
from config import values
class MyAPIException(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def convert(base: str, quote: str, amount: str):

        if base == quote:
            raise MyAPIException(f'Валюты совпадают, выберите разные: {base}-{quote}')

        try:
            base_ticker = values[base]
        except KeyError:
            raise MyAPIException(f'Данная валюта не поддерживается: {base}')

        try:
            quote_ticker = values[quote]
        except KeyError:
            raise MyAPIException(f'Данная валюта не поддерживается: {quote}')

        try:
            amount = float(amount)
        except ValueError:
            raise MyAPIException(f'Не верное значение количества {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        result = json.loads(r.content)[values[quote]]
        result *= amount

        return result