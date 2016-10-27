from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton
import datetime


def get_exchanges_keyboard(exchanges):
    keyboard = InlineKeyboardMarkup()

    for chunk in chunk_iterable(exchanges, 2):
        row_buttons = []
        for exchange in chunk:
            ccy_code = exchange['ccy']
            row_buttons.append(
                InlineKeyboardButton(
                    text=exchange['base_ccy'] + ' -> ' + ccy_code,
                    callback_data='{"a":"ex", "c":"' + ccy_code + '"}'
                )
            )
        keyboard.row(*row_buttons)

    return keyboard


def get_exchange_update_keyboard(currency):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            text='Update',
            callback_data='{"a":"u","c":"' + currency + '"}'
        )
    )

    return keyboard


def get_exchange_text(currency_result, update=False):
    base_currency = currency_result['base_ccy']

    text = '<i>Currency exchange for ' + currency_result['ccy'] + ':</i>\n\n' + \
           '<b>Buy:</b> ' + currency_result['buy'] + ' ' + base_currency + '\n' + \
           '<b>Sale:</b> ' + currency_result['sale'] + ' ' + base_currency

    # if update action - add signature with datetime
    if update:
        text += '\n\n<i>Updated ' + datetime.datetime.now().strftime('%H:%M:%S %Y-%m-%d') + '</i>'

    return text


def chunk_iterable(iterable, chunk_size):
    return [iterable[i:i + chunk_size] for i in range(0, len(iterable), chunk_size)]
