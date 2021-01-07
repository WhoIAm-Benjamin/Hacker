import random

proxies = {}

def proxy_generator():
	global proxies
	string = []
	for i in range(0, 4):
		if i == 0 or 2:
			char = str(random.randint(100, 255))
		elif i == 1 or 3:
			char = str(random.randint(1, 100))
		string.append(char)
		string.append('.')
	char = str(random.randint(1, 10000))
	del string[-1]
	string.append(':')
	string.append(char)
	string = ''.join(string)
	proxies['https'] = string

	string = []

	for i in range(0, 4):
		if i == 0 or 2:
			char = str(random.randint(100, 255))
		elif i == 1 or 3:
			char = str(random.randint(1, 100))
		string.append(char)
		string.append('.')
	char = str(random.randint(1, 10000))
	del string[-1]
	string.append(':')
	string.append(char)
	string = ''.join(string)
	proxies['http'] = string

	return proxies

proxy = proxy_generator()
print(proxy)

a = input()