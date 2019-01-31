from sys import argv
from hashlib import md5

# python main.py md5 hash.txt dict.txt

try:
	algrtm, hashfile, dictfile = argv[1], argv[2], argv[3]
except IndexError:
	print('Invalid arguments')
	raise SystemExit

with open(hashfile) as file:
	workhash = file.read()
	workhash = workhash.replace('\n', '')


def generator(string):
	for word in string:
		password = word.replace('\n', '')
		if encryption(password) == workhash:
			yield '-'*20 + '\nFIND! - ' + password
			return
		else:
			yield '[NO]' + password


def encryption(string):
	password = string.encode()
	signature = md5(password).hexdigest()
	return signature

print()
with open(dictfile, errors='ignore') as dic:
	for line in generator(dic):
		print(line)
print()