class Calculator:

	def calculate(self, num=None):
		if num is None:
			print "Cannot calculate"
		else:
			print num
	def calculate(self, num1=0, num2=0):
			print num1+num2

cal = Calculator()
cal.calculate()
cal.calculate(5)
cal.calculate(5,6)

#Overload is that we can call method of class as many ways as we want