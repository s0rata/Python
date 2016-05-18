class Human:
	def __init__ (self):
		self.name="Sorata"
		self.head= self.Head()
		self.brain=self.Brain()
	class Head:
		def talk(self):
			return "talking..."
	class Brain:
		def think(self):
			return "thinking..."

if __name__ =='__main__':
	sorata = Human()
	print sorata.name
	print sorata.head.talk()
	print sorata.brain.think()