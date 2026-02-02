print("=" * 50)
print("Question 4: Class Attendance")
print("=" * 50)

# 1. Create Monday class set
monday_class = {"Alice", "Bob", "Charlie", "Diana"}

# 2. Create Wednesday class set
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}

# 3. Add Grace to Monday class
monday_class.add("Grace")

print("Monday class:", monday_class)
print("Wednesday class:", wednesday_class)

# 4. Intersection - students who attended both classes
both_classes = monday_class & wednesday_class
print("Attended both classes:", both_classes)

# 5. Union - students who attended either class
all_students = monday_class | wednesday_class
print("Attended either class:", all_students)

# 6. Difference - students who attended only Monday
only_monday = monday_class - wednesday_class
print("Only Monday:", only_monday)

# 7. Symmetric difference - students who attended only one class
only_one = monday_class ^ wednesday_class
print("Only one class (not both):", only_one)

# 8. Check if Monday is subset of all students
print("Is Monday subset of all students?", monday_class <= all_students)

print()
