ans = 0
for i in range(1, 17):
	temp = i
	s = bin(i)
	count = s.count('1')
	if count % 2 == 0:
		i = i * 2
		s = bin(i)
		l = len(s) - 2
		if s[3] == '1':
			i = i - 2 ** (l - 2)
	else:
		i = i * 2 + 1
		s = bin(i)
		l = len(s) - 2
		if s[3] == '0':
			i = i + 2 ** (l - 2)
	if i >= 16:
		ans = temp
		break
print(ans)