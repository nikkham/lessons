ans = 0
for i in range(1, 78):
	temp = i
	s = bin(i)
	a = s.count('1')
	i = i * 2 + a % 2
	s = bin(i)
	a = s.count('1')
	i = i * 2 + a % 2
	if i > 77:
		ans = temp
		break
print(ans)