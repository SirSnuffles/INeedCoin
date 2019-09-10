# from INeedCoin.__init__ import Player, Bank, ReserveBank
from decimal import Decimal

class Player(object):
	def __init__(self, name):
		self.name = name
		#will contain a name and float value of said currency
		self.wallet = {}
		#in the form abrv:amount
		self.miners = {}

		#skills

	def addCurrency(self, abrv, amount = 0):
		self.wallet[abrv] = amount

	def makeCurrency(self, name, abrv, mineRate):
		return CryptoCurrency(name, abrv, mineRate)

	def setUpMiner(self, cur):
		# print(self.name, " added ", cur, "miner with", mineRate, "minerate")
		if cur not in self.miners:
			self.miners[cur] = 1
			# print(self.miners, self.wallet)
		elif cur in self.miners:
			self.miners[cur] += 1

	def addMinerCurrency(self, mineRate):
		# print('called', mineRate)
		for mine in self.miners:
			if mine in self.wallet:
				#cast to decimal to avoid floating point errors
				self.wallet[mine] = Decimal(str(self.wallet[mine]))
				#perform calc --- minerate * how many miners there are
				self.wallet[mine] += Decimal(str(mineRate)) * Decimal(str(self.miners[mine]))
		#set wallet currency back to a float
		self.wallet[mine] = float(self.wallet[mine])

	def giveCurrency(self, to, cur, amount):
		if self.wallet[cur] >= amount:
			#trade valid
			self.wallet[cur] -= amount
			to.wallet[cur] += amount
		else:
			print("invalid trade!")

	def takeCurrency(self, instance, cur, amount):
		#can call a method to continue
		if cur in instance.wallet:
			if instance.wallet[cur] < amount:
				amount = instance.wallet[cur]
				instance.wallet[cur] = 0
			else:
				instance.wallet[cur] -= amount

			self.wallet[cur] += amount
		else:
			return "Stolen nothing... no currency availible..."

		try:
			self.checkInstance()
		except:
			return

	def checkInstance(self):
		if isinstance(instance, ReserveBank.ReserveBank):
			newFBI = FBI(self.player)
			return "ReserveBank, stolen from, FBI initiated"
		elif isinstance(instance, Bank.Bank):
			newPolice = Police(self.player)
			return "Bank, stolen from, Police initiated"
		elif isinstance(instance, Player):
			return str("Player: " + self.name + " took " + str(amount) + ' ' + cur + " from " + instance.name)
		else:
			return "Not an instance!"