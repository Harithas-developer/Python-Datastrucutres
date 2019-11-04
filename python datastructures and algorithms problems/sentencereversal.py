def rever_sen(s):
	word = []
	space = [ ' ']
	length = len(s)

	i = 0
	while i < length:
		if s[i] not in space:
			word_start = i
			while  i < length and s[i] not in space:
				i+=1
			word.append(s[word_start:i])
			print(word)
		i+=1
	return ' '.join(reversed(word))


a = ' i am hari'
b = rever_sen(a)
print(b)	
		