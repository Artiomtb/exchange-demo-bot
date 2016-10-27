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


# handle all callback queries with data starts with 'ex-'
@bot.callback_query_handler(func=lambda query: query.data.startswith('ex-'))
def choose_exchange_callback(query):
    # get chosen currency from callback query (ex-<currency>)
    chosen_currency = query.data[3:]

    chat_id = query.message.chat.id

    # disables 'loading' state and adds 'typing' title to chat
    bot.answer_callback_query(query.id)
    bot.send_chat_action(chat_id, 'typing')

    # get data from pb_service by chosen currency
    currency_result = pb_service.get_exchange_by_currency(chosen_currency)

    base_currency = currency_result['base_ccy']
    bot.send_message(
        chat_id=chat_id,
        text='<i>Currency exchange for ' + currency_result['ccy'] + ':</i>\n\n' +
             '<b>Buy:</b> ' + currency_result['buy'] + ' ' + base_currency + '\n' +
             '<b>Sale:</b> ' + currency_result['sale'] + ' ' + base_currency,
        parse_mode='HTML'
    )


# use long poll non-stop
bot.polling(none_stop=True)
