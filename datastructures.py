
# # ==========================================
# # PYTHON DATA STRUCTURES - COMPLETE EXAMPLES
# # ==========================================


# # 1. LIST
# # Ordered, changeable, allows duplicate values

# print("\n--- 1. LIST ---")

# fruits = ["Apple", "Banana", "Mango", "Apple"]

# print(fruits)
# print(fruits[0])            # Access first element

# fruits.append("Orange")     # Add element
# fruits.insert(1, "Grapes")  # Insert at index 1
# fruits.remove("Banana")     # Remove by value
# fruits.pop()                # Remove last element

# fruits[0] = "Pineapple"     # Update element

# print(fruits)
# print("Length:", len(fruits))


# # 2. TUPLE
# # Ordered, unchangeable, allows duplicate values

# print("\n--- 2. TUPLE ---")

# colors = ("Red", "Green", "Blue", "Red")

# print(colors)
# print(colors[0])            # Access element
# print("Length:", len(colors))
# print("Count of Red:", colors.count("Red"))
# print("Index of Green:", colors.index("Green"))

# # colors[0] = "Yellow"      # Error: tuples cannot be changed


# # 3. SET
# # Unordered collection of unique elements

# print("\n--- 3. SET ---")

# numbers = {10, 20, 30, 20, 40}

# print(numbers)              # Duplicate 20 is removed

# numbers.add(50)             # Add element
# numbers.discard(10)         # Remove element safely

# print(numbers)

# set_a = {1, 2, 3, 4}
# set_b = {3, 4, 5, 6}

# print("Union:", set_a | set_b)
# print("Intersection:", set_a & set_b)
# print("Difference:", set_a - set_b)


# # 4. DICTIONARY
# # Stores data as key-value pairs

# print("\n--- 4. DICTIONARY ---")

# student = {
#     "name": "Harsh",
#     "age": 21,
#     "course": "Data Analytics"
# }

# print(student)
# print(student["name"])       # Access value

# student["age"] = 22          # Update value
# student["city"] = "Pune"     # Add new key-value pair

# student.pop("course")        # Remove a key

# print(student)
# print("Keys:", student.keys())
# print("Values:", student.values())
# print("Items:", student.items())


# # 5. STRING
# # Ordered sequence of characters; immutable

# print("\n--- 5. STRING ---")

# name = "Python Programming"

# print(name)
# print(name[0])               # First character
# print(name[0:6])             # Slicing
# print(name.upper())          # Uppercase
# print(name.lower())          # Lowercase
# print(name.replace("Python", "Java"))
# print("Length:", len(name))


# # 6. RANGE
# # Represents a sequence of integers

# print("\n--- 6. RANGE ---")

# for i in range(1, 6):
#     print(i)

# numbers_range = list(range(2, 11, 2))
# print("Even numbers:", numbers_range)


# # 7. LIST COMPREHENSION
# # A concise way to create a list

# print("\n--- 7. LIST COMPREHENSION ---")

# squares = [x * x for x in range(1, 6)]
# print("Squares:", squares)

# even_numbers = [x for x in range(1, 11) if x % 2 == 0]
# print("Even numbers:", even_numbers)


# # 8. NESTED LIST
# # A list containing other lists

# print("\n--- 8. NESTED LIST ---")

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(matrix)
# print(matrix[0])             # First row
# print(matrix[1][2])          # Row 2, column 3


# # 9. NESTED DICTIONARY
# # A dictionary containing other dictionaries

# print("\n--- 9. NESTED DICTIONARY ---")

# employees = {
#     "employee1": {"name": "Amit", "salary": 25000},
#     "employee2": {"name": "Priya", "salary": 30000}
# }

# print(employees["employee1"]["name"])
# print(employees["employee2"]["salary"])


# # 10. STACK
# # Follows LIFO: Last In, First Out
# # Implemented using a list

# print("\n--- 10. STACK ---")

# stack = []

# stack.append(10)             # Push
# stack.append(20)
# stack.append(30)

# print("Stack:", stack)

# print("Popped:", stack.pop())  # Removes 30
# print("Stack after pop:", stack)


# # 11. QUEUE
# # Follows FIFO: First In, First Out
# # deque is efficient for removing from the front

# print("\n--- 11. QUEUE ---")

# from collections import deque

# queue = deque()

# queue.append("A")            # Enqueue
# queue.append("B")
# queue.append("C")

# print("Queue:", queue)

# print("Removed:", queue.popleft())  # Removes A
# print("Queue after removal:", queue)


# # 12. FROZENSET
# # An immutable set of unique elements

# print("\n--- 12. FROZENSET ---")

# fixed_numbers = frozenset([1, 2, 3, 2])

# print(fixed_numbers)
# print("Contains 2:", 2 in fixed_numbers)

# # fixed_numbers.add(4)       # Error: cannot modify a frozenset


# # ==========================================
# # END OF PYTHON DATA STRUCTURES
# # ==========================================
