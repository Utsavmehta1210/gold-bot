import os
import yfinance as yf
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

def get_gold():
    try:
        gold = yf.Ticker("GC=F")
        data = gold.history(period="1d")
        price_oz = float(data['Close'].iloc[-1])
        price_gram = price_oz / 31.1035
        return f"Gold Live ✅\n\n1 Ounce: ${price_oz:.2f}\n1 Gram: ${price_gram:.2f}"
    except Exception as e:
        return "Gold price hamna malto nathi, thodi var pachi try karo."

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Namaste! Gold Bot Live che ✅\n/price lakho etle gold no bhav malse.")

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = get_gold()
    await update.message.reply_text(msg)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("price", price))
app.run_polling()
