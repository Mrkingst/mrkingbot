from flask import Flask, request
import os
import telegram
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
BOT_USERNAME = "Mrking_st_bot"

app = Flask(__name__)

# Telegram application setup
application = Application.builder().token(TOKEN).build()

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm alive and working 🚀")

# Register handler
application.add_handler(CommandHandler("start", start))

# Webhook endpoint
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.process_update(update)
    return "OK"

# Keep-alive route (optional)
@app.route("/", methods=["GET"])
def index():
    return "Bot is up"

if __name__ == "__main__":
    application.run_polling()
