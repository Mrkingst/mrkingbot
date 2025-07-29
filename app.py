from flask import Flask, request
import telegram
import os

TOKEN = os.environ.get("TOKEN")
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route(f"/{TOKEN}", methods=["POST"])
def respond():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text

    if text == "/start":
        bot.sendMessage(chat_id=chat_id, text="👋 Hello! Your bot is now working.")
    else:
        bot.sendMessage(chat_id=chat_id, text="🤖 Sorry, I only understand /start right now.")

    return "ok"

@app.route("/")
def index():
    return "Bot backend is running."

if __name__ == "__main__":
    app.run(debug=True)
