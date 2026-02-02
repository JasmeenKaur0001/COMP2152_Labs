print("=" * 50)
print("Question 6: Inventory Management System")
print("=" * 50)

# 1. Create inventory dictionary with tuples as values
inventory = {
    "Laptop": (999.99, 5),
    "Mouse": (29.99, 15),
    "Keyboard": (79.99, 10),
    "Monitor": (299.99, 8)
}

# 2. Print inventory using for loop with items()
print("=== Current Inventory ===")
for product, details in inventory.items():
    price = details[0]
    quantity = details[1]
    print(product + " - Price: $" + str(price) + ", Quantity: " + str(quantity))

print()

# 3. Create category sets
electronics = {"Laptop", "Monitor"}
accessories = {"Mouse", "Keyboard"}

# 4. Find all products using union
all_products = electronics | accessories
print("All product categories:", all_products)

print()

# 5. Create list of all prices
prices = []
for product in inventory:
    price = inventory[product][0]
    prices.append(price)
print("Price list:", prices)

# 6. Sort prices and print lowest/highest
prices.sort()
print("Sorted prices:", prices)
print("Lowest price: $" + str(prices[0]))
print("Highest price: $" + str(prices[-1]))

print()

# 7. Add new product
inventory["Headphones"] = (49.99, 20)

# 8. Update Mouse quantity (keep same price)
mouse_price = inventory["Mouse"][0]
inventory["Mouse"] = (mouse_price, 12)

# 9. Remove Monitor
del inventory["Monitor"]

# 10. Print final inventory
print("=== Final Inventory ===")
for product, details in inventory.items():
    price = details[0]
    quantity = details[1]
    print(product + " - Price: $" + str(price) + ", Quantity: " + str(quantity))