import pickle

import sys
from time import sleep


filename = input('Drag and drop the file: ')
try:
	with open(filename, 'rb') as f:
		read = pickle.load(f)
		while True:
			ask = input('It\'s password?(y/n)\n').lower()
			if ask == 'y':
				for i in read:
					print('Extracting...')
					sleep(1)
					print(password)
				break
			elif ask == 'n':
				print(read)
				break
			else:
				print('Try again')
				continue
		input()
		sys.exit()
except:
	print('Don\'t exit file :(')
	sleep(5)
	sys.exit()