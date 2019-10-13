#1 WxPython
#2 PyQt
#3 Tkinter

import tkinter #библиотека графических приложении
import random #библиотека случайностей

window = tkinter.Tk()
window.title("minecraft")
window.geometry("600x500")

label = tkinter.Label(text="100000", fg="black", bg ="white", font="Arial 22")
label.place(x=25, y=25)

def random_color():                       #функция рандомности цветов
    colors = ["red", "green", "blue"]     #сами цвета
    label["bg"] = random.choice(colors)

def count():
    random_color()
    num = int(label["text"])
    num = num + 30000
    label["text"] = str(num)

button = tkinter.Button(text="Нажми Плз :3", command = count)
button.place(x=25, y=300)

#label["text"] = "КРОТ" - обращение к тексту в переменной label
#label["bg"] = "color" - обращение к цвету label - бэкргаунда текста
#для выбора цвета можно использовать HexCode



window.mainloop()