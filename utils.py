from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton


def get_exchanges_keyboard(exchanges):
    keyboard = InlineKeyboardMarkup()

    for chunk in chunk_iterable(exchanges, 2):
        row_buttons = []
        for exchange in chunk:
            ccy_code = exchange['ccy']
            row_buttons.append(
                InlineKeyboardButton(
                    text=exchange['base_ccy'] + ' -> ' + ccy_code,
                    callback_data='ex-' + ccy_code
                )
            )
        keyboard.row(*row_buttons)

    return keyboard


def chunk_iterable(iterable, chunk_size):
    return [iterable[i:i + chunk_size] for i in range(0, len(iterable), chunk_size)]
