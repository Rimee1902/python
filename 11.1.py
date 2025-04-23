def try2():
    while True:
        try:
            x = int(input("Enter an integer: "))
            return x
        except ValueError as ve:
            print(ve)
            print("Try again\n")


result = try2()
print(f"You entered: {result}")
