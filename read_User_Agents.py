with open('User-Agents.txt', 'r') as f:
	content = f.read()

content = content.split('\n')
print(content)