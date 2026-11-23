import os
import asyncio
import yfinance as yf
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Python 3.14 mate fix
asyncio.set_event_loop(asyncio.new_event_loop())

TOKEN = os.getenv("BOT_TOKEN") or os.getenv("TELEGRAM_TOKEN")

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
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("price", price))
    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
