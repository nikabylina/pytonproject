# Получить на ввод количество рублей и копеек и вывести в правильной форме, например, 3 рубля, 1 рубль 25 копеек, 3 копейки
rub = int(input('enter rubl'))
cents = int(input('enter cents'))
if (rub != 0) and (cents != 0):
    print(f'{rub} rub. {cents} cents')
elif (rub != 0) and (cents == 0):
    print(f'{rub} rub.')
else:
    print(f'{cents} cents')
