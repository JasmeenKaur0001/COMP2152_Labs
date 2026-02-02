print("=" * 50)
print("Question 2: Shopping Cart")
print("=" * 50)

# 1. Create a shopping cart list
cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]

# 2. Count how many times "apple" appears
apple_count = cart.count("apple")
print("Number of apples:", apple_count)

# 3. Find position of "milk"
milk_position = cart.index("milk")
print("Position of milk:", milk_position)

# 4. Remove one "apple" from the cart
cart.remove("apple")

# 5. Pop the last item
removed_item = cart.pop()
print("Removed item using pop:", removed_item)

# 6. Check if "banana" is in the cart
print("Is banana in cart?", "banana" in cart)

# 7. Print the final cart
print("Final cart:", cart)

print()