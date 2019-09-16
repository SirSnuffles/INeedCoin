import bisect 

class Market(object):
    def __init__(self):
        self.buyQueue = dict()
        self.sellQueue = dict()
        self.currencyList = []
        self.priceList = []


    def buy(self, cur, price, amount):
        pass


    def sell(self, cur, price, amount):
        """inserts various currencies into self.sellQueue and combines like prices
        together"""
        # priceList = []
        # if cur not in self.sellQueue:
        #     print(True)
        #     self.sellQueue[cur] = [{price: amount}]
        # else:
        #     for value in self.sellQueue.values():
        #         print(value,self.sellQueue, 'HLELERWKENGKWNET')
        #         for listOfValues in value:

        #             for key, val in listOfValues.items():
        #                 print(key, val, 'here')
        #                 if key == price:
        #                     self.sellQueue[cur] = [{price: amount + val}]
        #                 elif key != price:
        #                     print(self.sellQueue[cur],type(self.sellQueue[cur]), 'thisone!')
        #                     self.sellQueue[cur].append({price:amount})
        #                     return
        self.priceList.append([cur,[price,amount]])
        for i in self.priceList:
            if cur in i:
                self.priceList.append([cur,[price,amount]])     
        # # print(self.priceList)
        # elif cur in self.priceList:
        #     print(True)
        print(self.priceList)

def main():
    # sell(self, cur, price, amount)
    x = Market()
    x.sell("NZD", 9, 4)
    x.sell("NZD", 9, 4)
    # x.sell("NZD", 9, 4)
    # x.sell("NZD", 9, 4)

    # x.sell("NZD", 10, 4)
    # x.sell("NZD", 10, 4)
    # x.sell("NZD", 10, 4)

    # x.sell("GBP", 10, 5)

    # x.sell("GBP", 11, 5)
    # print(x.buyQueue)
    # print(x.sellQueue)
    # x.buy("NZD", 8, 4)
    # x.buy("GBP", 1, 10)
    print(x.buyQueue, "Buyqueue")
    print(x.sellQueue, "Sellqueue")

if __name__ == '__main__':
    main()