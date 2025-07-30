from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")  # Use Render environment variable
BOT_USERNAME = "Mrking_st_bot"  # Your bot username

app = Flask(__name__)

application = Application.builder().token(TOKEN).build()

# Define the command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Your bot is working ✅")

# Add the command to the bot
application.add_handler(CommandHandler("start", start))

# Webhook endpoint
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.update_queue.put_nowait(update)
    return "ok"

# Start webhook server when app runs
if __name__ == "__main__":
    application.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 10000)),
        webhook_url=f"https://mrkingbot.onrender.com/{TOKEN}"
    )
