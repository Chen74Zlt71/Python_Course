# Практическое задание по уроку "Строки и индексация строк"
# example = a
a = str(input())
print(a[0])
print(a[-1])
b = int(len(a))
print(a[(b // 2):(int(b - 0.5))])
print(a[::-1])
print(a[1::2])
