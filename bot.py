import config
from telebot import TeleBot

# init bot by token from config
bot = TeleBot(config.TOKEN)

# use long poll non-stop
bot.polling(none_stop=True)
