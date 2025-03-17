# main.py

import schedule
import time
from data_collector import collect_data, save_data
from model import create_model
from trading_bot import execute_trade, predict_price

def job():
    data_point = collect_data()
    save_data([data_point], filename='market_data.csv')
    model = create_model((60, 3))
    model.load_weights('trading_model.h5')
    # Adicione a lógica para utilizar o modelo e executar operações aqui

# Agendar o trabalho para rodar em intervalos desejados
schedule.every(10).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
