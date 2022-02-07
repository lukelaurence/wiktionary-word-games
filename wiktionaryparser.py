import re
with open('enwiktionary-latest-pages-articles-multistream.xml','r') as f:
	recording = 0
	title = ''
	for line in f:
		if line == '  <page>\n':
			recording = 1
		elif recording == 1:
			title = line
			recording = 2
		elif recording == 2:
			if line == '==English==\n':
				word = re.sub('</{0,1}title>','',title.strip(' \n'))
				if word.isalpha() and word.islower() and word.isascii():
					print(word)
				recording = 3
		elif recording == 3:
			if line[0:2] == '# ':
				# word = re.sub('\{\{lb.*?\}\}','',line)
				# word = re.sub('[\[\]\{\}#]','',word)
				# print(re.sub('\|en\|',' ',word),end='')
				recording = 0
			elif line == '----\n':
				recording = 0
		if line == '  </page>\n':
			recording = 0