def get_num(num):
	if num == 1:
		return 1
	else:
		return num*get_num(num-1)
num = int(input('1-18'))
a = get_num(num)
print(a)