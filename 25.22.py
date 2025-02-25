

n = int(input("Enter the number of items in the dictionary: "))

my_dict = {}

for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    my_dict[key] = value


if not my_dict:
    print("The dictionary is empty.")
else:
    print("The dictionary is not empty.")

