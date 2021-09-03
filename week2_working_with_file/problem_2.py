file=open('user.txt', 'r')
a=file.read()
for i in a:
	if 'w' in i:
		print('Yes, there is "w" in text')
	else:
		print('No, there isn`t "w" in text')
