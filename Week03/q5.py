print("=" * 50)
print("Question 5: Contact Book")
print("=" * 50)

# 1. Create contacts dictionary
contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}

# 2. Print Alice's phone number
print("Alice's number:", contacts["Alice"])

# 3. Add Diana
contacts["Diana"] = "555-4321"
print("Contacts after adding Diana:", contacts)

# 4. Update Bob's number
contacts["Bob"] = "555-0000"
print("Contacts after updating Bob:", contacts)

# 5. Delete Charlie
del contacts["Charlie"]
print("Contacts after deleting Charlie:", contacts)

# 6. Print all names using keys()
print("All names:", contacts.keys())

# 7. Print all numbers using values()
print("All numbers:", contacts.values())

# 8. Print total number of contacts
print("Total contacts:", len(contacts))

print()