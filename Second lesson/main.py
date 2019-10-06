def get_imt(weight, height):
    imt = weight / (height * height)

    if imt < 19:
        print("У вас недовес :(")
    elif imt > 25:
        print ("У вас перевес :(")
    else:
        print("Ваш вес в норме :3")

def calc():
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


scommand = input()

if scommand == "calc":
    print(calc())
    
