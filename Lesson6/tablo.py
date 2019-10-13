from course import get_course #или import course
import tkinter


window = tkinter.Tk()
window.geometry("400x350")
window.title("КУРСЫ ВАЛЮТ НА ЦБРФ")

img_logo = tkinter.PhotoImage(file='C:/Users/Cанек/Documents/Projects/Lesson6/logo.png')
logo = tkinter.Label(image=img_logo)
logo.place(x=0, y=0)

lab = tkinter.Label(text="Курс валют \n MAXIMUM банк", fg="black", font="Arial 22")
lab.place(x=150, y=25)



window.mainloop()

print(get_course("R01235"))