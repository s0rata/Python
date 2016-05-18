import csv

with open('me.csv', 'wb') as csvfile:
	filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	filewriter.writerow(['Name','Profession'])
	filewriter.writerow(['Sorata', 'Game Design'])