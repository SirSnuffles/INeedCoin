dictionary = [{9: 16}, {10: 4}, {10: 4}, {10: 4}]
for value in self.sellQueue.values():
	for listOfValues in dictionary:
		for key, val in listOfValues.items():
			print(key,val)
print(dictionary)
