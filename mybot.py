import telebot
from Config import TOKEN , keys
from utils import ConvertionException ,CriptoConverter



bot = telebot.TeleBot(TOKEN)

class ConvertionException(Exception):
    pass

@bot.message_handler(commands = ['start','help'])
def help(message:telebot.types.Message):
    text='Чтобы начать работу введите команду боту в следующем формате:\n<имя валюты> \
<в какую валюту перевести>\
<колличество переводимой валюты>\n Увидеть список всех доступных валют/values'
    bot.reply_to(message,text)


@bot.message_handler(commands=['values'])
def values(message:telebot.types.Message):
    text='Доступные валюты:'
    for key in keys. keys():
        text ='\n'.join((text, key))
    bot.reply_to(message,text)

@bot.message_handler(content_types=['text'])
def convert(message:telebot.types.Message):
    try:
        values = (message.text.lower()).split()# приведем все введенные симолы в нижний регистр для удобства обработки
        if len(values) == 2:
            values.append(1)# если колличество валюты не введено,предполагаем,что нужно узнать цену одной единицы валюты
        if len(values)== 1 or len(values)>3:
            raise ConvertionException (f'Для корректной работы бота необходимо ввести три параметра\nОбразец:доллар рубль 8')
        base, quote, amount = values
        total_base = CriptoConverter(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message,f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message,f'Не удалось обработать команду\n{e}')
    else:
        text=f'За {amount}-{quote} вы получите\n{ total_base *int(amount)}-{base}'\
            f'\nпо курсу cryptocompere.com'
        bot.send_message(message.chat.id,text)


bot.polling()





