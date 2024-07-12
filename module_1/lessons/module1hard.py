# Задание "Средний балл":
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
a = list(sorted(students))
b = grades
print({a[0]: ((sum(b[0])) / (len(b[0]))), a[1]: ((sum(b[1])) / (len(b[1]))),
       a[2]: ((sum(b[2])) / (len(b[2]))), a[3]: ((sum(b[3])) / (len(b[3]))),
       a[4]: ((sum(b[4])) / (len(b[4])))})
