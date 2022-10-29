def getpossiblewords(input,sort=True):
	output = []
	with open('wiktionary_words.txt','r') as f2:
		words = list(map(lambda a:a[:-1],f2))
	for word in words:
		last = -1
		wordgood = True
		for letter in word:
			lettergood = False
			indicies = [x for x in range(4) if x != last]
			for index in indicies:
				if letter in input[index]:
					last = index
					lettergood = True
					break
			if lettergood:
				continue
			wordgood = False
			break
		if wordgood:
			output.append(word)
	if sort:
		a = {x:y for x,y in map(lambda x:(x,len(set(x))),words)}
		b = [x for x,y in sorted(a.items(),key=lambda p:p[1],reverse=True)]
		return b
	return output

def issuccessor(input,first,second):
	for x in input:
		if first[-1] in x and second[0] in x:
			return False
	return True

def parsetree(input,words,word):
	"""
	Finds the best next word. If the unique chars aren't getting any longer,
	moves on. Recursive.
	"""

	for x in words:
		if issuccessor(input,word,x):
			concatenation = word + x
			if len(set(concatenation)) > len(word):
				word = concatenation
				# return parsetree(input,words,concatenation)
	return word

i = (('a','b','c'),('d','e','f'),('g','h','i'),('j','k','l'))
# i = (('a','s','d'),('o','g','y'),('c','e','r'),('u','w','k'))

print(parsetree(i,getpossiblewords(i,True),"head"))

# print(solvegame(i))