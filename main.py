import os
import asyncio
import threading
import yfinance as yf
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

asyncio.set_event_loop(asyncio.new_event_loop())

TOKEN = os.getenv("BOT_TOKEN") or os.getenv("TELEGRAM_TOKEN")

app_flask = Flask(__name__)
@app_flask.route('/')
def home():
    return "Bot is Running!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app_flask.run(host="0.0.0.0", port=port)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Namaste! Gold price mate /price lakho.")

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.message.reply_text("Gold price lavu chu... ⏳")
        gold = yf.Ticker("GC=F")
        data = gold.history(period="1d")
        if data.empty:
            await update.message.reply_text("Price nathi malyo, fari try karo.")
            return
        p = float(data["Close"].iloc[-1])
        await update.message.reply_text(f"🪙 Gold Price: ${p:.2f} / oz")
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")

def main():
    threading.Thread(target=run_flask, daemon=True).start()
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("price", price))
    print("Bot started...")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
