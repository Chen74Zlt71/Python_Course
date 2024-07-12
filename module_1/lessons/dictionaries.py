# Словари и множества.
phone_book = {'Andrey': [89218077191, 335521], 'Denis': 88005553535}
# 'Andrey' - это ключ, 89218077191 - это значение
# разделяются ":". "'Andrey': 89218077191" - это один объект.
print(phone_book)
# phone_book = {['Andrey']: 89218077191, 'Denis': 88005553535}
# Ключ не может быть неизменяемым.
print(phone_book['Andrey'])
phone_book['Andrey'] = 89222331453, 335521
print(phone_book)
phone_book['Anton'] = 89222331454  # добавляет к словарю.
# del phone_book['Denis']  # удаление из словаря.
phone_book.update({'Sasha': 89128077191,
                   'Alex': 89108077191})
print(phone_book)
print(phone_book.get('Alex'))
print(phone_book.get('Elena'))
print(phone_book.get('Elena', 'Такого ключа нет'))
print(phone_book)
phone_book.pop('Anton')  # извлекает пару из словаря в кэш
print(phone_book)
phone_book.update({'Anton': 89222331454})
print(phone_book)
a = phone_book.pop('Anton')
print(phone_book)
print(a)
list_ = [1, 2, 3]
print(list_)
list_.pop(0)
print(list_)
print(phone_book.keys())
print(phone_book.values())
print(phone_book.items())
# значение может меняться
print(phone_book)
