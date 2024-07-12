tuple_ = 1, 2, 3, 4
print(tuple_)  # получим (1, 2, 3, 4) это и есть кортеж(tuple), он не изменяемый
# кортеж - это не изменяемый список.
tuple_2 = (1, 2, 3, 4)
print(tuple_2)
tuple_3 = tuple([1, 2, 3, 4])
print(tuple_3)
print(type(tuple_))
tuple_ = 1, 2, 3, 4, True, "String"
print(tuple_)
print(tuple_[0])
# tuple_[0] = 200
# print(tuple_) error!!!
tuple_ = 1, 2, 3, 4, True, "String"
list_ = [1, 2, 3, 4, True, "String"]
print(tuple_.__sizeof__())
print(list_.__sizeof__())
tuple_ = ([1, 2], 0)
print(tuple_)
tuple_[0][0] = 2
print(tuple_)
tuple_ = ([1, 2], 0) + (1, 2)
print(tuple_)
tuple_ = (1, 2) * 3
print(tuple_)
