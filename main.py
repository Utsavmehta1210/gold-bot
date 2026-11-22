import time
import yfinance as yf
from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "GOLD-BOT LIVE HAI!"

def run_bot():
    while True:
        try:
            df = yf.download("GC=F", period="1d", interval="5m", progress=False)
            price = float(df['Close'].iloc[-1].iloc[0]) if hasattr(df['Close'].iloc[-1], 'iloc') else float(df['Close'].iloc[-1])
            print(f"GOLD PRICE: {price}", flush=True)
        except Exception as e:
            print(f"Error: {e}", flush=True)
        time.sleep(60)

threading.Thread(target=run_bot, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
