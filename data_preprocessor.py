# data_preprocessor.py

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def load_data(filename='market_data.csv'):
    df = pd.read_csv(filename)
    return df

def preprocess_data(df):
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(df[['price', 'volume', 'liquidity']])
    X, y = [], []
    for i in range(len(scaled_data) - 60):
        X.append(scaled_data[i:i+60])
        y.append(scaled_data[i+60, 0])  # Prevendo o preço
    X, y = np.array(X), np.array(y)
    return X, y, scaler

if __name__ == "__main__":
    df = load_data()
    X, y, scaler = preprocess_data(df)
