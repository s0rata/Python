
class User:
	#name=""

	def __init__(self, name):
		self.name=name

	def printName(self):
		print self.name


class Programmer(User):
	"""docstring for Programmer"""
	def __init__(self, name):
		self.name = name
	def doPython(self):
		print "Python programming"

sorata=User("Sorata")
sorata.printName()

shiina=Programmer("Shinna")
shiina.printName()
shiina.doPython()
