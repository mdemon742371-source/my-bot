import os
import telebot
from flask import Flask
from threading import Thread

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "বট চালু আছে ✅")

app = Flask('')
@app.route('/')
def home(): return "Bot Running"

def run(): app.run(host='0.0.0.0', port=10000)
Thread(target=run).start()

bot.infinity_polling()
