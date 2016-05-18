class CoffeeMachine:
	name=""
	beans=0
	water=0

	def __init__(self, name, beans, water):
		self.name=name
		self.beans=beans
		self.water=water

	def addBean(self): #self is like object of that class, it holds all the value of the variable
		self.beans=self.beans+1
		self.water=self.water-1

	def removeBean(self):
		self.beans=self.beans-1

	def addWater(self):
		self.water=self.water+1

	def removeWater(self):
		self.water=self.water-1

	def demo(self):
		print "Name:"+self.name
		print "Beans:"+str(self.beans)
		print "Water:"+str(self.water)

pythonBean = CoffeeMachine("Python Bean", 83, 20)
pythonBean.demo()
print ""
pythonBean.addBean()
pythonBean.demo()



