import requests

from fastapi import HTTPException
from os import getenv

API_KEY = getenv('ALPHAVANTAGE_APIKEY')


def sync_converter(from_currency: str, to_currency: str, price: float = 1.0):
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={API_KEY}'
    try:
        response = requests.get(url)
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)
    
    data = response.json()

    if 'Realtime Currency Exchange Rate' not in data:
        return HTTPException(status_code=400, detail='Realtime Currency Exchange Rate not in response')
    
    exchange_rate = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])

    return price * exchange_rate


if __name__ == '__main__':
    converted_value = sync_converter(from_currency='USD',
                                    to_currency='BRL',
                                    price=5.5)
    print(converted_value)
