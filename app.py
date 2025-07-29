from flask import Flask, request
import telegram
import os

TOKEN = os.environ.get("BOT_TOKEN")  # Make sure this variable is set in Render
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return 'MrKing Bot is running!'

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    message = update.message.text

    bot.sendMessage(chat_id=chat_id, text="You said: " + message)
    return 'ok'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
