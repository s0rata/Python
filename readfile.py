import os.path

#define var and assign path to file as its value
filename = 'h.py'
if not os.path.isfile(filename):
	print 'File not found'
else:
	with open(filename) as file:
	#content=f.readlines() 
		content = file.read().splitlines() #read without newline

	for line in content:
		print line