import config, utils
from telebot import TeleBot
from pb_service import PBService

# init bot by token from config
bot = TeleBot(config.TOKEN)
pb_service = PBService()


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


# handle /exchange
@bot.message_handler(commands=['exchange'])
def exchange_command(message):
    bot.send_message(
        chat_id=message.chat.id,
        text='Here are available exchanges. Select one of them:',
        reply_markup=utils.get_exchanges_keyboard(pb_service.get_exchanges())
    )


# use long poll non-stop
bot.polling(none_stop=True)
