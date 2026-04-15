# --------------------------
# LIST OPERATIONS
# --------------------------
my_list = ["apple", "banana", "cherry"]
print("Original List:", my_list)

# Add 1 new item
my_list.append("date")
print("After adding:", my_list)

# Remove 1 item
my_list.remove("banana")
print("After removing:", my_list)

# Sort the list
my_list.sort()
print("After sorting:", my_list)
print("\n")

# --------------------------
# TUPLE OPERATIONS
# --------------------------
my_tuple = (1, 2, 3, 4)
print("Original Tuple:", my_tuple)

# Try modifying one element
try:
    my_tuple[0] = 10
except TypeError as e:
    print("Error:", e)
    print("Explanation: Tuples are immutable, meaning their values cannot be changed or modified after creation.")
print("\n")

# --------------------------
# SET OPERATIONS
# --------------------------
my_set = {1, 2, 3}
print("Original Set:", my_set)

# Add a value
my_set.add(4)
print("After adding:", my_set)

# Remove a value
my_set.discard(2)
print("After removing:", my_set)

# Print the updated set
print("Final Set:", my_set)
print("\n")

# --------------------------
# DICTIONARY OPERATIONS
# --------------------------
my_dict = {"name": "Alice", "age": 20}
print("Original Dictionary:", my_dict)

# Add a new key "grade"
my_dict["grade"] = "A"

# Update your "age"
my_dict["age"] = 21

# Print all keys
print("All Keys:", my_dict.keys())
print("Final Dictionary:", my_dict)
