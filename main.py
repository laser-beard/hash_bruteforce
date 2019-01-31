from sys import argv
from hashlib import md5
from datetime import datetime
import re

# python main.py md5 hash.txt dict.txt

try:
	algrtm, hashfile, dictfile = argv[1], argv[2], argv[3]
except IndexError:
	print('Invalid arguments')
	raise SystemExit


def write_result(chash, cpass):
	with open('result.txt', 'a') as result:
		line = str(datetime.now()) + ' - ' + chash + ':' + cpass + '\n'
		result.writelines(line)


with open(hashfile) as file:
	workhash = file.read()
	workhash = workhash.replace('\n', '')
	if re.match(r'^[0-9a-f]{32}$', workhash) is None:
		print('This hash is Invalid! -', workhash)
		write_result(workhash, cpass='[INVALID HASH]')
		raise SystemExit


def generator(string):
	status = '[Not Found]'
	for word in string:
		password = word.replace('\n', '')
		if encryption(password) == workhash:
			yield '-'*20 + '\nFIND! - ' + password
			status = password
			break
		else:
			yield '[NO]' + password
	return write_result(workhash, status)


def encryption(string):
	password = string.encode()
	signature = md5(password).hexdigest()
	return signature


print()
with open(dictfile, errors='ignore') as dic:
	for line in generator(dic):
		print(line)
print()