from course import get_course #или import course
import tkinter
from bitcoin import get_bitcoin


window = tkinter.Tk()
window.geometry("400x350")
window.title("КУРСЫ ВАЛЮТ НА ЦБРФ")

img_logo = tkinter.PhotoImage(file='C:/Users/Cанек/Documents/Projects/Lesson6/logo.png')
logo = tkinter.Label(image=img_logo)
logo.place(x=0, y=0)

lab = tkinter.Label(text="Курс валют \n САНЯ банк", fg="black", font="Arial 22")
lab.place(x=150, y=25)

usd_course = tkinter.Label(text=f"$ {get_course('R01235')}", font="Arial 16")
usd_course.place(x=90, y=150)

eur_course = tkinter.Label(text=f"€ {get_course('R01239')}", font="Arial 16")
eur_course.place(x=90, y=190) 

bit = get_bitcoin()
usd = get_course('R01239')
float_bit = float(bit)
float_usd = float(usd)

bit_course = tkinter.Label(text=f"Ƀ {float_bit * float_usd}", font="Arial 16")
bit_course.place(x=90, y=230)



window.mainloop()
