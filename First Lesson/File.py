age = 16 #int (Integeer) целое число
name = "Sasha" #str (Cтрока, в кавычках)
pi = 3.14 #float (Десятичные числа, дроби или числа с плавающей точкой)
#Математические операции
print(age * pi) #Умножение
print (age / 10) #Деление
print(age - 21) #Вычитание
print(age + age) #Сложение
var1 = age + age / pi
print(var1)

var2 = name + " Makarov"
print(var2)

var3 = var2[4:10]
print(var3)
#Логический тип данных (Bool - True/False)
var4 = age > pi
print(var4)

var5 = age < pi
print(var5)
#Условие
if age > pi:
    print("Условие верно")
else:
    print("Условие неверно")    