import bisect 

class Market(object):
    def __init__(self):
        self.marQueue = {}


    def insert(self, key, price, quantity):
        priceDict = self.marQueue.get(key, {price: 0})
        if price not in priceDict:
            self.marQueue[key].update({price:quantity})
            return self.marQueue
        priceDict[price] += quantity
        self.marQueue[key] = priceDict
        return self.marQueue

    def remove(self, key, price, quantity):
        priceDict = self.marQueue.get(key, {price:0})
        if price not in priceDict:
            print("no offer availible!")
            return
        print(priceDict[price], quantity)
        if priceDict[price] < quantity:
            print("Error, not enough availible")
            return
        elif priceDict[price] == quantity:

            del self.marQueue[key][price]
            return self.marQueue
        priceDict[price] -= quantity
        self.marQueue[key] = priceDict
        return self.marQueue

def main():
    """working insert and remove market!!!!"""
    x = Market()
    x.insert("NZD", 9, 4)
    x.insert("NZD", 9, 4)
    x.insert("NZD", 9, 4)
    
    x.insert("GBP", 10, 5)
    x.insert("BLA", 0.1, 0.01)
    x.insert("BLA", 0.1, 0.01)

    x.insert("NZD", 8, 4)
    x.insert("GBP", 1, 10)
    print(x.marQueue)
    x.remove("NZD", 8, 5)
    x.remove("GBP", 10, 2)
    print(x.marQueue)

if __name__ == '__main__':
    main()