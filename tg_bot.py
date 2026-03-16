import telebot
from datetime import datetime, timedelta

TOKEN = "8709833650:AAEGkKuEoT7qohTg1C0nMJ2aSwHeLRT4Q1U"

bot = telebot.TeleBot(TOKEN)#объект бота для отправки команд
zapis = {}#тута храним готовые записи
temp_data = {}#тут храним имя пользователя


def get_time_slots():
    slots = []# пустой список для времени
    tomorrow = datetime.now() + timedelta(days=1)# берем завтрашнюю дату
    for hour in range(9, 18):#цикл орт 9 до 18
        time_str = tomorrow.strftime(f"%d.%m.%y {hour}:00")#превращаем дату в строку
        slots.append(time_str)#добавляем врямя в список
    return slots#возвращаем готовый список


@bot.message_handler(commands=['start'])#обработчик старта
def start(message):#отправляем приветствие и список доступных
    bot.send_message(message.chat.id,#
                     "Привет! Я бот для записи\n\nКоманды:\n/book - записаться\n/myrecord - моя запись\n/cancel - отмена")#


@bot.message_handler(commands=['book'])#обработчик боок
def book(message):#
    chat_id = message.chat.id#
    msg = bot.send_message(chat_id, "Введите ваше имя")#просим имя и ждем
    bot.register_next_step_handler(msg, get_name)#


def get_name(message):#получение имени
    chat_id = message.chat.id#
    name = message.text#текст сообщения от пользователя
    temp_data[chat_id] = {'name': name}#запоминаем имя
    slots = get_time_slots()#получаем список всех времен
    free_slots = []#список всехсвободных слотов

    for slot in slots:#проверяем каждый час
        if slot not in zapis:#если нет в занятом значит свободно
            free_slots.append(slot)#

    if not free_slots:#если мест нету то выходим
        bot.send_message(chat_id, "Извините, на завтра нет свободного времени")#
        return#

    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)#
    buttons = []#создаем кнопки
    for slot in free_slots[:8]:#перебираем 8 своббодных слотов
        buttons.append(telebot.types.KeyboardButton(slot))#делаем из времени кнопку
    markup.add(*buttons)#добавляем кнопки в меню

    msg = bot.send_message(chat_id, f"Приятно познакомиться, {name}!\nВыберите свободное время", reply_markup=markup)#сообщение о выборе свобдного времени
    bot.register_next_step_handler(msg, get_time)#

def get_time(message):#
    chat_id = message.chat.id#
    selected_time = message.text#то что пользователь нажал на кнопку

    if selected_time in zapis:#проверка на нажатие одновременно
        bot.send_message(chat_id, "Это время уже занято! Начните заново /book",#
                         reply_markup=telebot.types.ReplyKeyboardRemove())#
        return#

    name = temp_data[chat_id]['name']#достаем имя которое мы сохраняли
    zapis[selected_time] = name#кладем в основной список

    bot.send_message(chat_id,#подттверждаем запись
                     f"Имя: {name}\n"#
                     f"Время: {selected_time}\n\n"#
                     f"Ждем Вас!",#
                     reply_markup=telebot.types.ReplyKeyboardRemove())#
    del temp_data[chat_id]#


@bot.message_handler(commands=['myrecord'])#поиск записи
def my_record(message):#
    chat_id = message.chat.id#
    user_name = message.from_user.first_name#имя ползователя
    found = False#

    for time, name in zapis.items():#перебираем все записи
        if name == user_name:#если нашли имяя совпадающее с именим в тг
            bot.send_message(chat_id, f"Ваша запись: {time}")#отправляем сообьщение о записи
            found = True#
            break#

    if not found:#
        bot.send_message(chat_id, "У вас нет активных записей")#


@bot.message_handler(commands=['cancel'])#отмена записи
def cancel(message):#
    chat_id = message.chat.id#
    user_name = message.from_user.first_name#
    to_delete = None#

    for time, name in zapis.items():#
        if name == user_name:#
            to_delete = time#если нашли то время которое надо удалить
            break#

    if to_delete:#
        del zapis[to_delete]#стираем запись из словаря
        bot.send_message(chat_id, " Ваша запись отменена")#
    else:#
        bot.send_message(chat_id, "У вас нет активных записей")#


@bot.message_handler(commands=['all'])#просмотр всех записей
def all_records(message):#
    if message.from_user.id == 123456789:#айди админа
        if zapis:#
            text = "📋 Все записи:\n\n"#
            for time, name in sorted(zapis.items()):#сортируем по времени
                text += f"👤 {name} - {time}\n"#
            bot.send_message(message.chat.id, text)#
        else:#
            bot.send_message(message.chat.id, "Записей нет")#
    else:#
        bot.send_message(message.chat.id, "У вас нет доступа")#


print("Бот запущен...")#вывод о том что бот запущен
bot.polling(none_stop=True)#бесконечный цикл