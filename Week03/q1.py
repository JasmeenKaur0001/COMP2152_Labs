print("=" * 50)
print("Question 1: Student Grades List")
print("=" * 50)

# 1. Create a list with initial grades
grades = [85, 92, 78, 95, 88]

# 2. Append a new grade
grades.append(90)

# 3. Sort the grades in ascending order
grades.sort()

# 4. Print the sorted list
print("Sorted grades:", grades)

# 5. Print highest grade (last element using negative indexing)
print("Highest grade:", grades[-1])

# 6. Print lowest grade (first element)
print("Lowest grade:", grades[0])

# 7. Print total number of grades
print("Total number of grades:", len(grades))

print()
