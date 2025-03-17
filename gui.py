# gui.py

import tkinter as tk
from tkinter import scrolledtext
from threading import Thread
from main import train_model, start_trading

class TradingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Trading Bot Interface")

        self.log_area = scrolledtext.ScrolledText(root, width=50, height=20)
        self.log_area.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.train_button = tk.Button(root, text="Treinar", command=self.train_model)
        self.train_button.grid(row=1, column=0, padx=10, pady=10)

        self.start_button = tk.Button(root, text="Start", command=self.start_trading)
        self.start_button.grid(row=1, column=1, padx=10, pady=10)

    def log_message(self, message):
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.see(tk.END)

    def train_model(self):
        self.log_message("Iniciando treinamento do modelo...")
        thread = Thread(target=self._train_model_thread)
        thread.start()

    def _train_model_thread(self):
        train_model(self.log_message)
        self.log_message("Treinamento concluído.")

    def start_trading(self):
        self.log_message("Iniciando operações de trading...")
        thread = Thread(target=self._start_trading_thread)
        thread.start()

    def _start_trading_thread(self):
        start_trading(self.log_message)
        self.log_message("Operações de trading iniciadas.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TradingApp(root)
    root.mainloop()
