# Создать список произвольного содержания. После каждой операции выводить список на экран
# Добавить к нему строку “Hello”.
# Удалить первый элемент.
# Поменять второй элемент на строку “World”.
# Удалить элемент “World”
# Вывести на экран перевернутый список

listt = [1, 2, 3, 4, 5, 6]
listt.append('Hello')
print(listt)
listt.remove(1)
print(listt)
listt[1] = 'World'
print(listt)
listt.pop(1)
print(listt)
print(listt[:: -1])
