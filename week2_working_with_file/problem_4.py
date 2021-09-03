w = input("We are glad to welcome you on our website \n Select '1' to enter " )
if w == "1":
	file = open("database.txt" , "r") 
	f = (file.read().split())
	login = input("login : \n")
	if login in f:
		password = input('Hello'+ login + '\nPassword : ')
	if password in f:
		print("You have successfully entered the account")
	else:
		print('Wrong password!!!')
	if login not in f:
		print("Could not find your login")
	file.close()
if w == "2":
	file = open("database.txt" , "a+") 
	f = (file.read().split())
	login2 = input("new login : \n")
	if login2 in f:
		print('Such login already exists!!!')
	if login2 not in f :
		file.write(login2)
		password2 = input("new password : ")
		password3 = input('repeat password : ')	 
	if password2 == password3:
		file.write(" ")
		file.write(password2)
		print("Congratulations !!! \n You have successfully registered!!!")
	else: 
		print("wrog password!!!")
		file.close()
else:
	print("Error!!!")
