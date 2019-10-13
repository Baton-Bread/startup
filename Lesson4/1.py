import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://www.cbr.ru/scripts/XML_daily.asp"


response = requests.get(url)
soup = BeautifulSoup(response.content, "lxml")
def get_course(chr_code, count):
    valutes = soup.find_all("valute")
    for x in valutes:
        if x.charcode.text == chr_code:
            nominal = int(x.nominal.text)
            value = float(x.value.text.replace(",", "."))
            print(f"За {nominal*count} {chr_code} дают {nominal * value * count} деревянных.")

def calc():
    print("Добро пожаловать в Базовый консольный калькулятор Python!")
    print("Чтобы проводить операции с числами вам нужно ввести команду операции.")
    print("Эта версия калькулятора поддерживает только 5 команд: *,/,-,+,%.")
    print("* - умножение, / - деление, - -- вычитание,% - выделить остаток из деления, и + - сложение соответственно.")
    print("Удачи!")


    command = input("Введите команду: ")
    num1 = float(input("Введите 1-e число: "))
    num2 = float(input("Введите 2-e число: "))


    if command == "+":
        print(num1 + num2)
    elif command == "*":
        print(num1 * num2)
    elif command == "/":
        print(num1 / num2)
    elif command == "-":
        print(num1 - num2)
    elif command == "%":
        print(num1 % num2)
    else:
        print("Неверная команда!")


lol = input("Какую программу хотите использовать?(Введите: 'Калькулятор' или 'Конвертер': ")
if lol == "Калькулятор":
    calc()
elif lol == "Конвертер":
    charcode = str(input("Введите CharCode: "))
    how_much = int(input("Сколько вам нужно валюты?: "))
    print(get_course(charcode, how_much))
else:
    print("Такой программы нет или неправильно введена команда.")

