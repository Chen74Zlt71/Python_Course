# Списки. Индексация и методы списков.
food = ["apple", "coconut", "banana"]  # "apple" is '0'
print(food)
print(food[0])
food[0] = "peach"  # Замена элемента списка
print(food)
food[0] = "apple"  # Замена элемента списка
print(food)
food[1] = "peach"  # Замена элемента списка
print(food)
food[1] = "coconut"  # Замена элемента списка
print(food)
food.append(True)  # Добавить в конец списка
print(food)
food.extend("string")  # добавляет в конец списка элемент как список, компьютер перебирает все символы, которые мы
# ему передали и добавит их в список по отдельности.
print(food)
food.extend(["string", 2])  # добавляет в список элементы, то есть попытаемся внести в наш список другой список, то
# компьютер их объединит
print(food)
food.remove("apple")  # убрать из списка
print(food)
print("coconut" in food)  # проверить наличие элемента в списке
print("coconut" not in food)  # проверить отсутствие элемента в списке
print(food[0:2])  # как в str можно использовать срезы в list
print(food[0:2:2])
