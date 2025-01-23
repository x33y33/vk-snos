import telebot

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
API_TOKEN = '7684711444:AAE7pAbXBmE4ymYPFAMMVbMjLksg6WB2yx4' 
bot = telebot.TeleBot(API_TOKEN)

print("""Бот отправлен на тех. перерыв""")

@bot.message_handler(commands=['start'])
def start_command(message):
    response = ("😴Бот на техническом перерыве🛠")
    bot.reply_to(message, response)



# Запуск бота
bot.polling()