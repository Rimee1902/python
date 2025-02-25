
grocery_prices = {
    'apple': 2.5,
    'banana': 1.2,
    'orange': 3.0,
    'milk': 1.5,
    'bread': 2.0
}


grocery_quantities = {
    'apple': 4,
    'banana': 6,
    'orange': 3,
    'milk': 2,
    'bread': 1
}


total_bill = 0


for item in grocery_prices:
    if item in grocery_quantities:  
        total_bill += grocery_prices[item] * grocery_quantities[item]

print("Total bill:", total_bill)
