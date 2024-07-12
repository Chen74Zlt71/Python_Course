# Практическое задание по теме: "Словари и множества"
# Работа со словарями:
my_dict = {'Nastia': 1997, 'Ksenia': 1994, 'Juri': 2012}
print(my_dict)
print("Existing value:", my_dict['Ksenia'])
print("Not existing value:", my_dict.get('Gleb'))
my_dict.update({'Roma': 2000,
                'Toma': 2002})
a = my_dict.pop('Nastia')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)
# Работа с множествами:
my_set = {1, 2, 1, 'Crash', 1.0, 1, 2, 2.045}
print("Set:", my_set)
my_set.add((3, 4, 5))
my_set.add('True')
my_set.discard(1)
print('Modified set:', my_set)
