import os
import threading
import telebot
import yfinance as yf
from flask import Flask

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

def get_gold():
    try:
        gold = yf.Ticker("GC=F")
        price = gold.history(period="1d")["Close"].iloc[-1]
        return f"Gold: ${price:.2f}"
    except:
        try:
            gold = yf.Ticker("GOLD")
            price = gold.history(period="1d")["Close"].iloc[-1]
            return f"Gold: ${price:.2f}"
        except:
            return "Gold price hamna malto nathi, thodi vaar pachi try karo."

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "Namaste! Gold Bot Live che ✅\n\n/start - Start\n/price - Gold no bhav")

@bot.message_handler(commands=['price'])
def price(m):
    bot.reply_to(m, get_gold())

@bot.message_handler(func=lambda m: True)
def all_msg(m):
    bot.reply_to(m, "Gold no bhav jova mate /price lakho")

@app.route('/')
def home():
    return "GOLD-BOT LIVE HAI!"

def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
