# Условная конструкция. Операторы if, elif, else.
print(1)
print(2)
print(3)
##
#name = input('Введите ваше имя: ')
#if name == 'Urban':
#    print('Здравствуйте, администратор')  # после условия 4 отступа
#if name == 'Денис'
#    print('Здравствуйте, преподаватель')
#else:
#    print("Привет", name)
##
number = int(input('Введите число: '))  # Fizz, Buzz, FizzBuzz, "or - and"
if number % 3 == 0 and number % 5 == 0:  # самое сложное условие идёт первым
    print('FizzBuzz')
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
else:
    print('Число не подходит')
