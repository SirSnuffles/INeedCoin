#prebuilt modules
import sys
sys.path.append("..")
import unittest

#self-built modules
from PlayerSystem import Player

class TestStringMethods(unittest.TestCase):

	def test_PlayerCheckName(self):
		self.newPlayer1 = Player.Player("player1")
		self.newPlayer2 = Player.Player("player2")
		self.assertEqual(self.newPlayer1.name, "player1")
		self.assertEqual(self.newPlayer2.name, "player2")

		self.newPlayer1.name = "12345"
		self.newPlayer2.name = "As35g3"

		self.assertEqual(self.newPlayer1.name, "12345")
		self.assertEqual(self.newPlayer2.name, "As35g3")

	def test_Wallet(self):
		self.newPlayer1 = Player.Player("player1")
		self.newPlayer2 = Player.Player("player2")		

		self.newPlayer1.addCurrency("RAN")
		self.newPlayer2.addCurrency("DOM")
		self.newPlayer1.addCurrency("RAN")

		self.assertEqual(self.newPlayer1.wallet["RAN"], 0)

		self.assertEqual(self.newPlayer2.wallet["DOM"], 0)

	def test_Miners(self):
		self.newPlayer1 = Player.Player("player1")
		self.newPlayer2 = Player.Player("player2")
		for i in range(1,11):
			#set up miner with 10 miners
			self.newPlayer1.setUpMiner("RAN")
			self.assertEqual(self.newPlayer1.miners["RAN"], i)

	def test_giveCurrency(self):
		self.newPlayer1 = Player.Player("player1")
		self.newPlayer2 = Player.Player("player2")
		self.newPlayer1.addCurrency("RAN", 10)
		self.newPlayer2.addCurrency("RAN", 0)
		self.newPlayer1.giveCurrency(self.newPlayer2, "RAN", 5)
		self.assertEqual(self.newPlayer1.wallet["RAN"], 5)
		self.assertEqual(self.newPlayer2.wallet["RAN"], 5)

	def test_takeCurrency(self):
		self.newPlayer1 = Player.Player("player1")
		self.newPlayer2 = Player.Player("player2")
		
		self.newPlayer1.addCurrency("RAN", 10)
		self.newPlayer2.addCurrency("RAN", 11)

		self.newPlayer1.takeCurrency(self.newPlayer2, "RAN", 10)
		self.assertEqual(self.newPlayer2.wallet["RAN"], 1)
		self.assertEqual(self.newPlayer1.wallet["RAN"], 20)

		self.newPlayer1.takeCurrency(self.newPlayer2, "RAN", 10)
		self.assertEqual(self.newPlayer2.wallet["RAN"], 0)
		self.assertEqual(self.newPlayer1.wallet["RAN"], 21)

		self.newPlayer1.giveCurrency(self.newPlayer2, "RAN", 5)
		self.assertEqual(self.newPlayer1.wallet["RAN"], 16)
		self.assertEqual(self.newPlayer2.wallet["RAN"], 5)


	def test_addMiner(self):
		self.newPlayer1 = Player.Player("player1")
		self.newPlayer2 = Player.Player("player2")
		for i in range(1,11):
			self.newPlayer1.setUpMiner("RAN")
			self.assertEqual(self.newPlayer1.miners["RAN"], i)

	def test_addMinerCurrency(self):
		self.newPlayer1 = Player.Player("player1")
		self.newPlayer2 = Player.Player("player2")
		self.newPlayer1.addCurrency("RAN")
		self.newPlayer1.setUpMiner("RAN")
		for i in range(10):
			self.newPlayer1.addMinerCurrency(0.001)
		self.assertEqual(self.newPlayer1.wallet["RAN"], 0.01)

		self.newPlayer1.setUpMiner("RAN")
		for i in range(10):
			self.newPlayer1.addMinerCurrency(0.001)
		#previous 0.01 in wallet + 2 * 0.001 because there are now 2 miners
		self.assertEqual(self.newPlayer1.wallet["RAN"], 0.03)

if __name__ == '__main__':

	unittest.main()