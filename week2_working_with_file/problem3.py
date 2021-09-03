file = open('python.txt', 'r')
t_words = []
b = (file.read().split())
for i in b:
	if 't' in i:
		t_words.append(i)
	if 'T' in i:
		t_words.append(i)
print(t_words)
file.close()
