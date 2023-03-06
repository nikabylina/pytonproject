a = [1, 2, 3, 4]
b = []
(f'first list id = {id(a)}, second list id ={id(b)}')
b = a
print(f'first list id = {id(a)}, second list id ={id(b)}')
print(b)
a.append(7)
print(a is b)
b = copy(a)
print(f'first list id = {id(a)}, second list id ={id(b)}')
