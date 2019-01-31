from sys import argv
from hashlib import md5
from datetime import datetime
import re

# python main.py md5 hash.txt dict.txt

hash_count, good, bad = 0, 0, 0
logname = datetime.now().strftime('%Y_%m_%d') + '.log'

try:
	algrtm, hashfile, dictfile = argv[1], argv[2], argv[3]
except IndexError:
	print('Invalid arguments')
	raise SystemExit


def write_result(chash, cpass):
	with open(logname, 'a') as result:
		line = str(datetime.now()) + ' - ' + chash + ':' + cpass + '\n'
		result.writelines(line)


def generator(string):
	global good
	status = '[Not Found]'
	for word in string:
		password = word.replace('\n', '')
		if encryption(password) == workhash:
			yield '[FIND]'
			good += 1
			status = password
			break
		# else:
		# 	yield '[NO]' + password
	print(workhash + ':' + status)
	return write_result(workhash, status)


def encryption(string):
	password = string.encode()
	signature = md5(password).hexdigest()
	return signature


with open(hashfile) as file:
	for workhash in file:
		hash_count += 1
		workhash = workhash.replace('\n', '')
		if re.match(r'^[0-9a-f]{32}$', workhash) is None:
			print(workhash + ':' + '[Invalid Hash]')
			write_result(workhash, cpass='[INVALID HASH]')
			bad += 1
		else:
			with open(dictfile, errors='ignore') as dic:
				for line in generator(dic):
					print(line)
	print('[Hashes]', '\nTotal:\t', hash_count, '\nFinded:\t', good, '\nInvalid:', bad)
	print('All detail results save into:', logname)