class Person:
	def walk(self):
		print "human walks with 2 legs"

class Dog:
	def walk(self):
		print "dog walks with 4 legs"

def walking(species):
	species.walk()

person = Person()
dog = Dog()

walking(person)
walking(dog)