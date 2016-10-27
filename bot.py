import config
from telebot import TeleBot

# init bot by token from config
bot = TeleBot(config.TOKEN)


# handle /start
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(
        chat_id=message.chat.id,
        text='Welcome! I\' m glad to see you!'
    )


# use long poll non-stop
bot.polling(none_stop=True)
