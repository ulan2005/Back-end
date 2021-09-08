def half():
	list_1 = ['name', 'age', '1', '19']
	a = list_1[:2]
	b = list_1[2:]
	a.reverse()
	b.reverse()
	lists = a + b
	print(lists)
half()