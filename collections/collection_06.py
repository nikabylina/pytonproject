"""Создать словарь произвольного содержания. После каждой операции выводить словарь на экран
Добавить новую пару по ключу alex. Значение - 42
Вывести на экран значение по ключу alex.
Изменить значение по ключу alex на 55.
Удалить элемент с ключом alex."""
dictt = {'a': 42, 56: 'b'}
print(dictt)
dictt['alex'] = 42
print(dictt)
print(dictt['alex'])
dictt['alex'] = 55
print(dictt)
dictt.pop('alex')
print(dictt)
