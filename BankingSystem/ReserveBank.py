from INeedCoin.__init__ import Bank

class ReserveBank():
	def __init__(self):

		#must be abrv
		self.country = ""
		self.wallet = {}
		print("init ReserveBank")

	def printMoney(self, cur, amount):
		"""add money to wallet"""
		self.wallet[self.country] += amount

	def giveCurrency(self, to, cur, amount):
		#can only give to banks
		if isinstance(to, Bank.Bank):
			if self.wallet[cur] >= amount:
				to.wallet += amount
			else:
				print("Invalid trade RB to B")
		else:
			print("Not a bank...")

	

	def hireEmployees(self):
		pass
