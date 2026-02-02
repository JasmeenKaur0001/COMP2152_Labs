print("=" * 50)
print("Question 3: Coordinate System")
print("=" * 50)

# 1. Create tuple point1
point1 = (3, 5)
print("Point 1:", point1)

# 2. Create tuple point2
point2 = (7, 2)
print("Point 2:", point2)

# 3. Unpack point1
x1, y1 = point1
print("x1 =", x1, ", y1 =", y1)

# 4. Unpack point2
x2, y2 = point2
print("x2 =", x2, ", y2 =", y2)

# 5. Calculate distance
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("Distance between points:", distance)

# 6. Create tuple from string
char_tuple = tuple("PYTHON")
print("Characters tuple:", char_tuple)

# 7. Print each character using for loop
for char in char_tuple:
    print(char)

print()