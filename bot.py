import telebot
from telebot.types import Message


TOKEN = '198894700:AAHmOku6rAG7lX-uXo7aKpnOpAdvtBBqaSM'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Привет')

@bot.message_handler(func=lambda message: True)

def upper(message: Message):
    bot.reply_to(message, message.text.upper())



bot.polling()