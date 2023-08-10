import telebot
from config import token, values, menu, help
from extensions import MyAPIException, CurrencyConverter

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['menu'])
def menuu(message):
    bot.send_message(message.chat.id, menu)

@bot.message_handler(commands=['start'])
def startt(message):
    bot.send_message(message.chat.id, help + '\n /menu')

@bot.message_handler(commands=['help'])
def helpp(message):
    bot.send_message(message.chat.id, help + '\n /menu')

@bot.message_handler(commands=['values'])
def valuess(message):
    bot.send_message(message.chat.id, 'ДОСТУПНЫЕ ВАЛЮТЫ:')
    for i in values:
        bot.send_message(message.chat.id, i + ' ' + values[i] )
    bot.send_message(message.chat.id, '/menu')

@bot.message_handler(content_types=['text'])
def convert_result(message: telebot.types.Message):
    try:
        val = message.text.split(' ')

        if len(val) != 3:
            raise MyAPIException('Неправльное количество параметров')

        base, quote, amount = val
        result = CurrencyConverter.convert(base, quote, amount)
    except MyAPIException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n {e}')
    except Exception as e:
        bot.reply_to(message, f'Неправильная команда.\n {e}')
    else:
        text = f'Конвертация {amount} {values[base]}({base}) в {values[quote]}({quote}): {result}, Комиссия банка: 100%'
        bot.send_message(message.chat.id, text)
        bot.send_message(message.chat.id, "/menu")

bot.infinity_polling()