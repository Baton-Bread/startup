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