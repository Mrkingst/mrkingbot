from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

import os

TOKEN = os.getenv("BOT_TOKEN")  # Make sure this is set in your Render environment
BOT_USERNAME = "Mrking_st_bot"  # Replace with your actual bot username

app = Flask(__name__)
application = Application.builder().token(TOKEN).build()

# --- Telegram Bot Handlers ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am your bot and I'm alive on Render!")

application.add_handler(CommandHandler("start", start))

# --- Webhook route for Telegram ---
@app.route(f"/{BOT_USERNAME}", methods=["POST"])
async def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    await application.process_update(update)
    return "ok"

# --- Root route for testing ---
@app.route("/", methods=["GET"])
def index():
    return "Bot is running!"

# --- Run Flask ---
if __name__ == "__main__":
    app.run(debug=True)
