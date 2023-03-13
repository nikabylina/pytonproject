# Ввести строку с клавиатуры. Вернуть результат логического выражения: длина строки не меньше 8 или в строке есть “python”.
my_str = input('enter str - ')
len_str = len(my_str)
print(len_str >= 8) or ('python' in my_str)
