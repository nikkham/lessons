a = 70 * '8'
while a.find('2222') != -1 or a.find('8888') != -1:
	if a.find('2222') != -1:
		a = a.replace('2222', '88', 1)
	else:
		a = a.replace('8888', '22', 1)					
print(a)
	