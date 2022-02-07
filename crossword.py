import random
import tkinter as tk
from functools import partial

def generategrid(width,height):
	with open('text.txt','r') as f:
		content = f.readlines()
		used = []
		remaining = width * height
		while remaining:
			# print(remaining)
			r = random.randrange(0,len(content))
			word = content[r].replace('\n','')
			if remaining - len(word) < 0:
				continue
			used.append(word)
			remaining -= len(word)
		letters = [letter for word in used for letter in word]
		random.shuffle(letters)
		print(used)
		return letters

def pushbutton(window,frame,label,grid,blurb,index,width,height):
	letter = grid[index]
	if letter.islower():
		blurb.append(letter.upper())
		grid[index] = letter.upper()
	elif blurb[-1] == letter:
		del blurb[-1]
		grid[index] = letter.lower()
	frame.destroy()
	label.destroy()
	initializegame(window,grid,blurb,width,height)

def initializegame(window,wordsearch,blurb,width,height):
	gridframe = tk.Frame(master=window)
	label = tk.Label(master=window,text=''.join(blurb))
	for x in range(height):
		# gridframe.columnconfigure(x,weight=1)
		# gridframe.rowconfigure(x,weight=1)
		for y in range(width):
			letter = wordsearch[height*x+y]
			button = tk.Button(master=gridframe,text=wordsearch[height*x+y].upper(),width=3,
			height=3,bg='white',fg='black' if letter.islower() else 'white',
			command=partial(pushbutton,window,gridframe,label,wordsearch,blurb,height*x+y,width,height))
			button.grid(row=x,column=y,sticky="nsew")
	# gridframe.pack()
	gridframe.grid(row=1,column=1)
	label.grid(row=2,column=1)
	# label.pack()
	# return gridframe

def rungame(width,height):
	wordsearch = generategrid(width,height)
	blurb = []
	# window = initializegame(wordsearch,blurb,width,height)
	window = tk.Tk()
	window.title('word search')
	window.geometry('%dx%d+%d+%d' % (300,300,300,300))
	for x in range(height):
		window.columnconfigure(x,weight=1)
		window.rowconfigure(x,weight=1)
	initializegame(window,wordsearch,blurb,width,height)
	# for x in range(height):
	# 	window.columnconfigure(x,weight=1)
	# 	window.rowconfigure(x,weight=1)
	# 	for y in range(width):
	# 		letter = wordsearch[height*x+y]
	# 		button = tk.Button(text=wordsearch[height*x+y].upper(),width=3,
	# 		height=3,bg='white',fg='black' if letter.islower() else 'white',
	# 		command=partial(pushbutton,wordsearch,blurb,height*x+y))
	# 		button.grid(row=x,column=y,sticky="nsew")
	window.mainloop()

rungame(10,10)

# class App(tk.Tk):
# 	def __init__(self,*args,**kwargs):
# 		tk.Tk.__init__(self, *args, **kwargs)
# 		self.grid = generategrid(width,height)
# 		self.blurb = []