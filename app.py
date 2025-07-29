import os
import logging
from flask import Flask, request
import telegram
from telegram.ext import Dispatcher, CommandHandler

TOKEN = os.environ.get("TOKEN")
if not TOKEN:
    raise ValueError("No TOKEN provided in environment variables")

bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        dispatcher.process_update(update)
    return 'ok'

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! Your bot is now live and working.")

dispatcher = Dispatcher(bot, None, use_context=True)
dispatcher.add_handler(CommandHandler("start", start))

if __name__ == '__main__':
    app.run(debug=True)
