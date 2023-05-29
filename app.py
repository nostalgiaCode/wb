import telebot

from config import api_key
from func import searchwb

BOT_TOKEN = api_key

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    response=searchwb(message)
    bot.reply_to(message, response)
	
bot.infinity_polling()