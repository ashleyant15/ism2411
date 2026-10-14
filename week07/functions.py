# Self Assessment Questions 
# 1. The first bug I noticed was the missing colon in the for loop. I always forget to add colons in DataCamp, 
# so I recognized the mistake when looking at the code. This shows I am getting better at recognizing errors.
# 2. The apply_discount function takes the original price and tier then calculates the new price after the discount
# It returns the discounted price based on the tier. 

# AI Disclosure: 
# I used chatgpt to help explain the errors in Excercise 5 and understand how to fix them. It helped me understand
# how to fix them. It helped me understad why the code was not working instead.


# Excercise 1 

# Defining a function
def calculate_tax(price, rate):
    return price * rate 

# Calling the function 

tax1 = calculate_tax(100,0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}")


# Exercise 2 

# Defining a cuntion with multiple parameters 
def apply_discount(price, tier): 
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze": 
        return price * 0.95
    else: 
        return price 

# Calling the function with different tiers 
original_price = 200

for tier in ["gold", "silver", "bronze", "none"]: 
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")


# Exercise 3 

def final_price(price, tier, tax_rate): 
    discounted_price = apply_discount(price, tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax 

print(f"final_price(200, 'gold', 0.07) = ${final_price(200, 'gold', 0.07):.2f}")

# Calling the final_price function 
print(f"Final price: ${final_price(200,'gold', 0.07):.2f}")

# Exercise 4 
orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

for price, tier in orders: 
   total = final_price(price, tier, 0.07)
   print(f"Price: ${price} | Tier: {tier} | Total: ${total:.2f}")

# Exercise 5
# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
# This replaces the total instead of adding each sale.
    total += sale
print(f"Total: ${total}")

count = 0
# The for loop needs a colon at the end.
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
# Using <= goes past the last index of the list.
while i < len(sales):
    print(sales[i])
    i += 1



# Exercise 6 
# The global x is 100, but inside the function x is 999.
# The x inside the function is local, so it does not change the x outside the function.
x = 100 

def double_it(): 
    x = 999
    return x * 2

print(x)
print(double_it())
print(x)