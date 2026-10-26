# Reflection Questions
# 1. I was suprised by how many different ways you can work with lists in Python. 
# I didnt realize you could easily add, remove, and organize items without rewriting the list. 
# 2. When I worked at a smoothie shop, we had to keep track of ingredients and supplies. 
# Using a Python list could have made it easier to see what we needed to restock instead 
# of checking everything manually on a list, like how we would in Excel.


# Exercise 1: Build a list 
print("--- Exercise 1: Build a List ---")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# Exercise 2: Index Practice

print("--- Exercise 2: Index Practice ---")
print(inventory[0]) # always grabs the first item
print(inventory[-1]) # always grabs the last item 
middle = len(inventory) // 2 
print(inventory[middle]) # grabs the middle item (not hard coded)


# Exercise 3: List Slicing 

print("--- Exercise 3: List Slicing ---")

print(inventory[:3]) # grabs the first 3 items
print(inventory[-2:]) # grabs the last two items
print(inventory[::2])


# Exercise 4: 

print("--- Exercise 4: List Methods ---")

inventory.append("envelope") # adds an item to the end of the list
print(inventory) 


inventory.remove("tape")
print(inventory)

inventory.sort() # sorts the list in alphabetical order
print(inventory)

# Exercise 5 

print("--- Excercise 5: Tuple Comparison ---")
coords = (40.7128, -74.0060) # New York City coordinates

try: 
    coords[0] = 90
except TypeError as error:
    print(f"TypeError caught: (error)")
    print("Tuples protect coordinates from being changed by accident")

print(coords)

# Exercise 6

print("--- Exercise 6: Average of a list of sales ---")

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total Sales, {total}")
print(f"Number of Sales: {count}")
print(f"Average of sales: {average}")
print(f"Best sale: {max(sales)}")
print(f"Worst sale: {min(sales)}")

best = sales[0]
worst = sales[0]

for amount in sales: 
    if amount > best:
        best = amount
    if amount < worst: 
        worst = amount 

print(f"Best sale (loop): {best}")
print(f"Worst sale (loop): {worst}")

# Exercise 7

print("--- Exercise 7: Accumulator Pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = [] # an empty list
for price in prices:
    discounted.append(round(price * 0.9, 2))# apply a 10% discount

print(prices)
print(discounted)

# Exercise 8 

print("--- Exercise 8: Filter ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for amount in sales: 
    if amount > 300: 
        high_sales.append(amount)

print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")
