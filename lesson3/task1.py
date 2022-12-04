a = 'abcdaabc' # задали строку
print(a.find('bcd')) # вывели позицию, начиная с которой есть подстрока 'bcd'
print(a.find('aa')) # тут будет -1, такой подстроки нет
print(a.count('a')) # посчитали число вхождений 'a'
#a = a.replace('abc', 'cda') # заменить все вхождения 'abc' на 'cda'
a = a.replace('abc', 'cda', 1) # заменить одно вхождение 'abc' на 'cda'
print(a)
