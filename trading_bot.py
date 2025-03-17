# trading_bot.py

from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.publickey import PublicKey
from solana.account import Account
from config import WALLET_ADDRESS, PRIVATE_KEY
from model import create_model
from data_preprocessor import preprocess_data, load_data
import numpy as np

def load_model(model_path='trading_model.h5'):
    model = create_model((60, 3))
    model.load_weights(model_path)
    return model

def predict_price(model, recent_data):
    recent_data = np.array(recent_data).reshape((1, 60, 3))
    predicted_price = model.predict(recent_data)
    return predicted_price

def get_wallet_balance(client, wallet_address):
    balance = client.get_balance(PublicKey(wallet_address))
    return balance['result']['value'] / 10**9  # Convert lamports to SOL

def execute_trade(action, amount, client, wallet):
    if action == "buy":
        # Lógica para comprar SOL usando USDC
        pass
    elif action == "sell":
        # Lógica para vender SOL por USDC
        pass

if __name__ == "__main__":
    client = Client("https://api.mainnet-beta.solana.com")
    wallet = Account(PRIVATE_KEY)
    model = load_model()
    df = load_data()
    X, _, scaler = preprocess_data(df)
    recent_data = X[-1]  # Dados mais recentes
    predicted_price = predict_price(model, recent_data)
    current_price = df['price'].iloc[-1]
    balance = get_wallet_balance(client, WALLET_ADDRESS)
    if predicted_price > current_price:
        execute_trade("buy", amount=balance, client=client, wallet=wallet)  # Compra com todo o saldo disponível
    else:
        execute_trade("sell", amount=balance, client=client, wallet=wallet)  # Vende todo o saldo disponível
