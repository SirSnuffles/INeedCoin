class Currency(object):
	def __init__(self, name, abrv, printRate):
		self.name = name
		self.total = 10000
		self.abrv = abrv
		#needs to be implemented at a time period
		self.printRate = printRate
		self.value = self.total/printRate
		#implement inflation?

class CryptoCurrency(object):
	def __init__(self, name, abrv, mineRate):
		self.name = name
		self.total = 100000
		self.abrv = abrv
		#needs to be implemented at a time period
		self.totalMiners = 0
		self.mineRate = mineRate
		#must hide this from players
		self.value = self.total/mineRate

	def getMineRate(self):
		return self.mineRate
