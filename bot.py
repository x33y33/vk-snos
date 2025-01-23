import telebot
import os
import csv


with open('token.txt') as token:
    s = token.read()


API_TOKEN = 's'
bot = telebot.TeleBot(API_TOKEN)

poisk = "Ищу..."
reklama = "Хочешь купить рекламу в этом боте? Напиши в бот - @sup_ghsbot"

print("""!!!!!!!!!!БОТ ЗАПУЩЕН!!!!!!!!!!
Доступные функции:
1 - Отправить бота на тех. перерыв""")
choice = input("input=")
if choice == "1":
    os.system("clear")
    os.system("python reboot.py")

# Функция для поиска данных в CSV-файле Telegram
def find_tg_data(message_text):
    with open('./database/tg.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if (message_text.lower() in row['id'].lower() or
                    message_text.lower() in row['phone'].lower() or
                    message_text.lower() in row['username'].lower() or
                    message_text.lower() in row['first_name'].lower() or
                    message_text.lower() in row['last_name'].lower()):
                return row
    return None

# Номер телефона;Тег
def find_gt_data(phone):
    with open('./database/getcontact.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if (phone in row.get('Номер телефона', '')):
                return row

# Поиск данных в базе данных
def find_db_data(phone):
    with open('./database/db.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if (phone in row.get('phone2', '')):
                return row
    return None

def find_vk_data(vkid):
    with open('./database/vk.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if (vkid in row['vkid'].lower()):
                return row
    return None


# Обработка команды /start
@bot.message_handler(commands=['start'])
def start_command(message):
    response = ("Привет, я бесплатный бот по пробиву телеграм\n"
                "Отправь мне username, никнейм или ID аккаунта")
    bot.reply_to(message, response)

# Обработка команды /help
@bot.message_handler(commands=['help'])
def help_command(message):
    response = "Задать вопрос или купить рекламу - @sup_ghsbot"
    bot.reply_to(message, response)

# Обработка сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    dfor = message.text
    bot.reply_to(message, poisk)  # Информируем пользователя, что идет поиск

    tg_data = find_tg_data(dfor)  # Ищем данные пользователя

    if tg_data:  # Проверяем, есть ли данные
        id1 = tg_data['id']
        fio1 = tg_data['first_name']
        fio2 = tg_data['last_name']
        phone1 = tg_data['phone']
        us1 = tg_data['username']

        gt_data = find_gt_data(phone1)
        gttag = gt_data['Тег'] if gt_data else "Нет данных"

        db_data = find_db_data(phone1)
        dbid = db_data['id2'] if db_data else "Нет данных"
        dburl = db_data['url2'] if db_data else "Нет данных"
        dbfname = db_data['fname'] if db_data else "Нет данных"
        dblname = db_data['lname'] if db_data else "Нет данных"
        dbgender = db_data['gender2'] if db_data else "Нет данных"
        dbdr = db_data['bday'] if db_data else "Нет данных"
        dbage = db_data['old'] if db_data else "Нет данных"
        dbcountry = db_data['country2'] if db_data else "Нет данных"
        dbcity = db_data['city2'] if db_data else "Нет данных"
        dbinst = db_data['inst'] if db_data else "Нет данных"

        vk_data = find_vk_data(id1)  # Используйте id1 для поиска в VK
        status1 = vk_data['status'] if vk_data else "Нет данных"
        urlphoto1 = vk_data['url_photo'] if vk_data else "Нет данных"

        # Формируем сообщение
        dosie = f"""┏ ✅ Запрос по: {dfor}
┣ 📋 ID: {id1}
┣ 📱 ФИО [TG]: {fio1} {fio2}
┣ ☎️ Номер телефона: +{phone1}
┗ 🔗 Username: @{us1}

┏ ✅ Найдено по ВКонтакте:
┣ 📋 ID: {dbid}
┣ 🖥 ВК страница: {dburl}
┣ 📱 ФИО [VK]: {dbfname} {dblname}
┣ 🕴 Пол: {dbgender}
┣ 🎂 Дата рождения: {dbdr}
┣ 📜 Возраст: {dbage}
┣ 🌎 Страна: {dbcountry}
┣ 🏙 Город: {dbcity}
┣ 📷Инстаграм: {dbinst}
┣ 🔵 Статус: {status1}
┗ 🖼️ URL фото: {urlphoto1}

┏ Остальное:
┗ Имя (GetContact.com): {gttag}

📢Реклама: {reklama}"""

        bot.reply_to(message, dosie)
    else:
        bot.reply_to(message, "❗️ Данных не найдено")

# Запуск бота
bot.polling()