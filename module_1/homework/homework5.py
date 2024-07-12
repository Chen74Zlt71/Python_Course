# Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"
immutable_var = 25, 1, [True, False], 100, "Python", 2.1
print("Immutable tuple:", immutable_var)
# immutable_var[2] = 22 - Кортеж не поддерживает обращение по элементам.
mutable_list = [25, 1, [True, False], 100, "Python", 2.1]
mutable_list[2] = [33, 10]
print("Mutable list:", mutable_list)
