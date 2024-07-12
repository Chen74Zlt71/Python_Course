# print() - вывод информации на экран
# type() - определение типа данных
# неизменяемые, есть изменяемые
print(5)
print(type(5))  # int - integer
print(5 + 5)
print(5 - 5)
print(5 * 5)
print(5 / 5)  # деление
print(5 // 5)  # целочисленное деление
print(type(1.0))  # float - числа с плавающей точкой
print(5 % 5)  # остаток от деления
print(5 ** 5)  # возведение в степень
print(5 ** 2)
print(2.0 + 2.0)  # с float можно выполнять те же действия
print(2.0 + 2)  # всё равно получим тип float
# str - строка (string)
print('Hello, world!')
print("Hello, world!")
print(type('Hello, world!'))  # str - строка (string)
print("Hello, 'world!'")
print('Hello, "world!"')
print("Hello," + 'world!')  # concatenate - соединение
print("Hello, " + 'world!')  # пробел как отдельный символ
# print('1' + 1) - выдаст ошибку!
print('1' + '1')
print(True, False)  # bool(boolean) - логический тип данных
print(type(True), type(False))
print(5 > 10)  # False не истина
print(5 < 10)  # True истина
print(5 > 10, 5 < 10)  # print - поддерживает множественный выбор
print(1, 2.0, 3, 4.0, 'hello world', True)
print(5 <= 5)  # меньше или равно
print(5 >= 5)  # больше или равно
print(5 == 5)  # равно ли
print(5 != 5)  # не равны
print(5 != 5 and 5 < 10)  # and - строгий оператор "и". "True and True=True",
# "True and False=False", "False and True=False". Может использоваться несколько раз
print(5 != 5 or 5 < 10)  # "T or F=T", "T or T=T", "F or F=F", "F or T=T"
# хоть бы одно выражение истинно получим истину.
# смена типа данных
print('5')
print(int('5'))
print(type(int('5')))
print(type(float('5')))
print(type(str('5')))
print(type(bool('5')))  # слово в число не перевести!
