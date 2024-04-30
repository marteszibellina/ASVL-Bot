import telebot
from telebot import types
from datetime import datetime
from schedule import schedule_lessons
from schedule import schedule_all


token = "6328375734:AAExzH_QttvtLmDO4X2-axYoL2TyLWAHpuA"
bot = telebot.TeleBot(token)

weekday = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
current_date = datetime.now().strftime("%d.%m.%Y")
current_weekday = weekday[datetime.now().weekday()]
current_lesson = schedule_lessons[datetime.now().weekday()]
def current_lesson(schedule_lessons, current_weekday):
    return schedule_lessons[datetime.now().weekday()]
print(current_lesson(schedule_lessons, current_weekday))
print(current_date)
print(current_weekday)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Я буду твоим помощником!")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Расписание")
    btn2 = types.KeyboardButton("Контакты")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Выберите интересующую тебя опцию", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == "Расписание":
        bot.send_message(message.chat.id, f"Сегодня: \n{current_date} \n{current_weekday}")
        bot.send_message(message.chat.id, f"Занятие: {current_lesson(schedule_lessons, current_weekday)}")
    elif message.text == "Контакты":
        bot.send_message(message.chat.id, "Контакты:"
                                          "\nАрт-студия Виталия Лещенко"
                                          "\nАдрес: г. Москва, Маломосковская ул., 16 стр. 6 (3 этаж)"
                                          "\nArtStudioVL@ASVL.ru"
                                          "\n+7(925)734-99-27")
    else:
        bot.send_message(message.chat.id, "Неизвестная команда")


bot.polling(none_stop=True, interval=0)