import os.path

filename ='h.py'
#filename='log.txt'

myfile = open(filename, 'w')
myfile.write('print \'hello world\'')
myfile.close()

if not os.path.isfile(filename):
	print 'File not found'
else:
	with open(filename) as file:
		contents = file.read().splitlines()

	for line in contents:
		print line