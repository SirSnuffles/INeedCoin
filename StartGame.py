#prebuilt modules
import sys
sys.path.append("..")

#self-built modules
from BankingSystem import Bank, ReserveBank
from PlayerSystem import Player, Currency

def main():
	print('init, ReserveBank')
	RB = ReserveBank.ReserveBank()
	print('init, bank1')
	B1 = Bank.Bank("Kiwibank")
	print('init,Currency; NZ Dollars')
	NZD = Currency.Currency("New Zealand Dollars", "NZD", 0.002)
	USD = Currency.Currency("United States Dollars", "USD", 0.005)
	GBP = Currency.Currency("Great British Pounds", "GBP", 0.001)

	BTC = Currency.CryptoCurrency("BitCoin", "BTC", 0.001)#LOL
	MUC = Currency.CryptoCurrency("Made Up Coin", "MUC", 1)

	print('init Alex')
	Alex = Player.Player("Alex")

	print('init Will')
	Will = Player.Player("Will")

	print('init Callum')
	Callum = Player.Player("Callum")

	Alex.setUpMiner(MUC.abrv, MUC.mineRate)
	Alex.setUpMiner(BTC.abrv, BTC.mineRate)
	# Alex.setUpMiner(MUC.abrv, MUC.mineRate)

	Will.setUpMiner(BTC.abrv, BTC.mineRate)
	Will.setUpMiner(BTC.abrv, BTC.mineRate)
	# Will.setUpMiner(GBP.abrv, GBP.printRate)

	Callum.setUpMiner(BTC.abrv, BTC.mineRate)
	Callum.setUpMiner(BTC.abrv, BTC.mineRate)


	print("Before")
	print(Will.wallet, Will.miners, "Will")
	print(Alex.wallet, Alex.miners, "Alex")
	print(Callum.wallet, Callum.miners, "Callum")
	print("Before")
	#game loop!

	#need a way to add multiple minerates to addMinerCurrency 
	#Currency instance should have a get minerate method
	for i in range(10):


		Alex.addMinerCurrency(MUC.mineRate)
		Will.addMinerCurrency(BTC.mineRate)
	print("After")
	print(Will.wallet, Will.miners, "Will")
	print(Alex.wallet, Alex.miners, "Alex")
	print(Callum.wallet, Callum.miners, "Callum")
	print("After")

if __name__ == '__main__':
	main()