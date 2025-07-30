from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

import os

TOKEN = "8250650945:AAFr6GPfBHB-nywtrg1agcIGSG-HxvtLqq8"
WEBHOOK_PATH = f"/{TOKEN}"

app = Flask(__name__)

bot_app = Application.builder().token(TOKEN).build()

# Define a /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! Your bot is working.")

# Add handler
bot_app.add_handler(CommandHandler("start", start))

# Flask route to receive webhook
@app.route(WEBHOOK_PATH, methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot_app.bot)
    bot_app.process_update(update)
    return "ok"
