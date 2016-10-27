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


# handle /help
@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(
        chat_id=message.chat.id,
        text='Ok. Here is help to you:\n\n' +
             '/exchange - show currencies list. Then click on currency code to see exchange.'
    )


# use long poll non-stop
bot.polling(none_stop=True)
