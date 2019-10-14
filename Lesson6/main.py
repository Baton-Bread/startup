#1 WxPython
#2 PyQt
#3 Tkinter

import tkinter #библиотека графических приложении
import random #библиотека случайностей

window = tkinter.Tk()
window.title("minecraft")
window.geometry("600x500")

label = tkinter.Label(text="0", fg="black", bg ="white", font="Arial 22")
label.place(x=25, y=25)

def random_color():                       #функция рандомности цветов
    colors = ["red", "green", "blue"]     #сами цвета
    label["bg"] = random.choice(colors)

def count():
    random_color()
    num = int(label["text"])
    num = num + 1
    label["text"] = str(num)

def final():
    random_color()
    count()
    text = ["Жми еще", "Сильнее жми!", "Кнопку не сломай", "Быстрее!"]
    button["text"] = random.choice(text)

button = tkinter.Button(text="Нажми Плз :3", command = final)
button.place(x=25, y=300)

#label["text"] = "КРОТ" - обращение к тексту в переменной label
#label["bg"] = "color" - обращение к цвету label - бэкргаунда текста
#для выбора цвета можно использовать HexCode



window.mainloop()