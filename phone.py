class telephone:
	__battery=0 #accessible only in class, want to set: 
	#def __init__(self):
		#self.__battery=__battery
	def setBattery(self,battery):
		self.__battery= battery
	def getBattery(self):
		return self.__battery
	def changeBattery(self):
		self.__battery=self.__battery+1000
	def showInfo(self):
		print "Battery: " + str(self.__battery)

phone1 = telephone()
phone1.setBattery(3600)
print phone1.getBattery()
phone1.changeBattery()
phone1.showInfo()
