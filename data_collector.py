# data_collector.py

import requests
import pandas as pd
from datetime import datetime
from config import ORCA_API_URL, SOL_USDC_POOL_ID

def get_market_data():
    url = f"{ORCA_API_URL}/{SOL_USDC_POOL_ID}"
    response = requests.get(url)
    if response.status_code == 200:
        try:
            data = response.json()
            return data
        except ValueError:
            print("Erro: A resposta não contém um JSON válido.")
            return None
    else:
        print(f"Erro: Requisição falhou com status code {response.status_code}")
        return None

def collect_data():
    data = get_market_data()
    if data:
        timestamp = datetime.now()
        price = data.get('price', None)
        volume = data.get('volume', None)
        liquidity = data.get('liquidity', None)
        return {'timestamp': timestamp, 'price': price, 'volume': volume, 'liquidity': liquidity}
    else:
        print("Erro: Não foi possível coletar os dados de mercado.")
        return None

def save_data(data, filename='market_data.csv'):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    market_data = []
    for _ in range(100):  # Coleta 100 pontos de dados
        data_point = collect_data()
        if data_point:
            market_data.append(data_point)
    save_data(market_data)
