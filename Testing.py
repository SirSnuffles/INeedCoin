from decimal import Decimal

num = 0

for i in range(10):
	num += Decimal(str(0.01))* Decimal(str(0.01))
print(float(num))