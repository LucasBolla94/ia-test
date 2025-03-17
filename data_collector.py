# data_collector.py

import requests
import pandas as pd
from datetime import datetime
from config import ORCA_API_URL, SOL_USDC_POOL_ID

def get_market_data():
    url = f"{ORCA_API_URL}/{SOL_USDC_POOL_ID}"
    response = requests.get(url)
    data = response.json()
    return data

def collect_data():
    data = get_market_data()
    timestamp = datetime.now()
    price = data['price']
    volume = data['volume']
    liquidity = data['liquidity']
    return {'timestamp': timestamp, 'price': price, 'volume': volume, 'liquidity': liquidity}

def save_data(data, filename='market_data.csv'):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    market_data = []
    for _ in range(100):  # Coleta 100 pontos de dados
        data_point = collect_data()
        market_data.append(data_point)
        save_data(market_data)
