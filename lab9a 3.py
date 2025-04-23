import random

l = [random.randint(-15, 15) for _ in range(10)]
print("Original list:", l)

m = map(lambda x: x**2, l)

squared_list = list(m)
print("Squared list:", squared_list)

