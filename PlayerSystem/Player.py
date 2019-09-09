from INeedCoin.__init__ import Player, Bank, ReserveBank
from decimal import Decimal

class Player(object):
	def __init__(self, name):
		self.ICO = False
		self.name = name
		#will contain a name and float value of said currency
		self.wallet = {}
		#in the form abrv:amount
		self.miners = {}

	def makeCurrency(self, name, abrv, mineRate):
		return CryptoCurrency(name, abrv, mineRate)

	def setUpMiner(self, cur, mineRate):
		# print(self.name, " added ", cur, "miner with", mineRate, "minerate")
		
		if cur not in self.miners:
			self.miners[cur] = 1
			print(self.miners, self.wallet)
		elif cur in self.miners:
			self.miners[cur] += 1

	def addMinerCurrency(self, mineRate):
		# print('called', mineRate)
		for mine in self.miners:
			if mine not in self.wallet:
				self.wallet[mine] = mineRate
			elif mine in self.wallet:
				self.wallet[mine] += float(mineRate) * self.miners[mine]

	def giveCurrency(self, to, cur, amount):
		if self.wallet[cur] >= amount:
			#trade valid
			self.wallet[cur] -= amount
			to.wallet[cur] += amount
		else:
			print("invalid trade!")

	def hack(self, instance):
		#can call a method to continue
		if isinstance(instance, ReserveBank.ReserveBank):
			return "ReserveBank"
		elif isinstance(instance, Bank.Bank):
			return "Bank"
		elif isinstance(instance, Player):
			return str("Player: " + self.name + " Hacked, " + instance.name)
		else:
			return "Not an instance!"