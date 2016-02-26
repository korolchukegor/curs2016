# coding: utf-8
import os, sys

def search_word(word, dirr):
	try:
		for file in os.listdir(dirr):
			file = os.path.join(dirr, file)
			#print(file)
			#print(os.path.abspath(dirr), file, os.path.isdir(file))
			if not os.path.isdir(os.path.abspath(file)):
				if word in file:
					spis[file] = os.path.abspath(file)
				elif file.endswith('.txt'):
					for line in open(file):
						if word in line:
							spis[file] = os.path.abspath(file)
			else:
				search_word(word, dirr = os.path.abspath(file))
				if word in file:
					spis[file] = os.path.abspath(file)
	except FileNotFoundError:
		print('Совпадений не найдено')


if __name__=="__main__":
	spis = {}
	dirr = sys.argv[2]
	word = sys.argv[1]
	search_word(word, dirr)
	if len(spis) != 0:
		print(spis)	