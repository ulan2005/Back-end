with open ("user.txt" , "w") as f:
	a = input("введи логин")
	b = input("введи пароль")
	f.write(a)
	f.write(b)
