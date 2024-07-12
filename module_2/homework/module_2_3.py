# Задача "Нули ничто, отрицание недопустимо!":
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
id_1 = 0
while id_1 < len(my_list):
    if my_list[id_1] < 0:
        break
    if my_list[id_1] > 0:
        print(my_list[id_1])
    id_1 += 1
