import math
a = float(input("Введите первое число:\n"))
b = float(input("Введите второе число:\n"))
print ("Сумма введенных чисел равна:", a+b)
if a > b:
    print ("Разность введенных чисел равна:",a-b)
else:
    print ("Разность введенных чисел равна:",b-a)
s = float()
s = abs(a)+abs(b)
print ("Среднее арифметическое модуля этих чисел:", s/2)
print ("Произведение введенных чисел:\n", a*b)
if a > b:
    print ("Частное введенных чисел равна:\n",a/b)
else:
    print ("Частное введенных чисел равна:\n",b/a)

