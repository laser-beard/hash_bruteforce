from sys import argv


try:
	algrtm, hashfile, dictfile = argv[1], argv[2], argv[3]
except IndexError:
	print('Invalid arguments')
	raise SystemExit