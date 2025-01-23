import os
import time

print("""ГЛАЗ БОГА ТГ

надеюсь ты все сделал по инструкции...""")

def function1(message, delay):
    print(message)
    time.sleep(delay)
    os.system("clear")
    os.system("python bot.py")

function1("Запускаю бота через 2 секунды", 2)
