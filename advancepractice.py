# Q1. Find the data type of every value in a mixed list.

# my_list = [10, 10.5, "Python", True, 5+2j, None]
# for i in my_list: 
#     print(type(i))

# Q2. Convert a nested list into a tuple of tuples.

# my_list = [[1, 2], [3, 4], [5, 6]]

# result = tuple(tuple(i) for i in my_list)

# print(result)

# Q3. Remove all duplicate values from a mixed list while preserving the
# original order.

# my_list = [10, "Python", 20, 10, "Java", "Python", 30]

# result = []

# for i in my_list: 
#     if i not in result: result.append(i)

# print(result)



# Q4. Check whether a number is a power of 2 using operators.

# n = int(input("Enter a number: "))

# if n > 0 and (n & (n - 1)) == 0:
#     print("Power of 2")
# else:
#     print("Not a power of 2")
# Q5. Swap two numbers using bitwise XOR.

# a = 10
# b = 20

# a = a ^ b
# b = a ^ b
# a = a ^ b

# print(a, b)
# Q6. Find whether a number is divisible by both 4 and 6 using logical
# operators.

# n = int(input("Enter a number: "))

# if n % 4 == 0 and n % 6 == 0:
#     print("Divisible by both")
# else:
#     print("Not divisible by both")

# Q7. Calculate the total electricity bill using different unit rates.

# units = int(input("Enter electricity units: "))

# if units <= 100:
#     bill = units * 3
# elif units <= 200:
#     bill = (100 * 3) + (units - 100) * 5
# elif units <= 300:
#     bill = (100 * 3) + (100 * 5) + (units - 200) * 7
# else:
#     bill = (100 * 3) + (100 * 5) + (100 * 7) + (units - 300) * 10

# print("Total bill:", bill)



# Q8. Check whether three sides can form a triangle.

# a = int(input("Enter first side: "))
# b = int(input("Enter second side: "))
# c = int(input("Enter third side: "))

# if a + b > c and a + c > b and b + c > a:
#     print("Valid Triangle")
# else:
#     print("Invalid Triangle")

# Q9. Determine the type of triangle (Equilateral, Isosceles, Scalene).

# a = int(input("Enter first side: "))
# b = int(input("Enter second side: "))
# c = int(input("Enter third side: "))

# if a <= 0 or b <= 0 or c <= 0:
#     print("Invalid sides")
# elif a + b <= c or a + c <= b or b + c <= a:
#     print("Invalid Triangle")
# elif a == b == c:
#     print("Equilateral Triangle")
# elif a == b or b == c or a == c:
#     print("Isosceles Triangle")
# else:
#     print("Scalene Triangle")

# Q10. Create a simple ATM menu (Withdraw, Deposit, Balance).

# balance = 5000

# while True:
#     print("1. Withdraw")
#     print("2. Deposit")
#     print("3. Balance")
#     print("4. Exit")

#     choice = int(input("Enter choice: "))

#     if choice == 1:
#         amount = int(input("Enter amount: "))

#         if 0 < amount <= balance:
#             balance -= amount
#         else:
#             print("Invalid amount")

#     elif choice == 2:
#         amount = int(input("Enter amount: "))

#         if amount > 0:
#             balance += amount
#         else:
#             print("Invalid amount")

#     elif choice == 3:
#         print("Balance:", balance)

#     elif choice == 4:
#         break

#     else:
#         print("Invalid choice")

# Q11. Calculate income tax based on different tax slabs.

# income = float(input("Enter annual income: "))

# if income <= 300000:
#     tax = 0
# elif income <= 600000:
#     tax = (income - 300000) * 0.05
# elif income <= 900000:
#     tax = 15000 + (income - 600000) * 0.10
# elif income <= 1200000:
#     tax = 45000 + (income - 900000) * 0.15
# else:
#     tax = 90000 + (income - 1200000) * 0.20

# print("Tax:", tax)

# Q12. Create a menu-driven calculator using if-elif.

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))

# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")

# choice = int(input("Enter choice: "))

# if choice == 1:
#     print(a + b)

# elif choice == 2:
#     print(a - b)

# elif choice == 3:
#     print(a * b)

# elif choice == 4:
#     if b != 0:
#         print(a / b)
#     else:
#         print("Cannot divide by zero")

# else:
#     print("Invalid choice")

# Q13. Print all prime numbers between 1 and n.

# n = int(input("Enter a number: "))

# for num in range(2, n + 1):
#     is_prime = True

#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print(num)
# Q14. Find the factorial of a number using a loop.

# n = int(input("Enter a number: "))

# fact = 1

# if n < 0:
#     print("Factorial not possible")
# else:
#     for i in range(1, n + 1):
#         fact = fact * i

#     print(fact)

# Q15. Print the Fibonacci series up to n terms.

# n = int(input("Enter number of terms: "))

# a = 0
# b = 1

# for i in range(n):
#     print(a)

#     a, b = b, a + b

# Q16. Check whether a number is an Armstrong number.

# n = int(input("Enter a number: "))

# temp = n
# total = 0
# power = len(str(n))

# while temp > 0:
#     digit = temp % 10
#     total = total + digit ** power
#     temp = temp // 10

# if n >= 0 and total == n:
#     print("Armstrong Number")
# else:
#     print("Not Armstrong Number")

# Q17. Reverse a number and check if it is a palindrome.

# n = int(input("Enter a number: "))

# temp = n
# reverse = 0

# while temp > 0:
#     digit = temp % 10
#     reverse = reverse * 10 + digit
#     temp = temp // 10

# print("Reverse:", reverse)

# if n == reverse:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# Q18. Find the Greatest Common Divisor (GCD) of two numbers.

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# while b != 0:
#     a, b = b, a % b

# print("GCD:", abs(a))



# Q19. Write a function to check if a string is a palindrome.

# def palindrome(s):
#     s = s.lower()

#     if s == s[::-1]:
#         print("Palindrome")
#     else:
#         print("Not Palindrome")


# palindrome("madam")

# Q20. Write a function to count vowels and consonants in a string.

# def count_letters(s):
#     vowels = 0
#     consonants = 0

#     for i in s.lower():
#         if i.isalpha():
#             if i in "aeiou":
#                 vowels += 1
#             else:
#                 consonants += 1

#     print("Vowels:", vowels)
#     print("Consonants:", consonants)


# count_letters("Python Programming")
# Q21. Create a function to calculate simple and compound interest.

# def interest(p, r, t):
#     si = (p * r * t) / 100

#     ci = p * (1 + r / 100) ** t - p

#     print("Simple Interest:", si)
#     print("Compound Interest:", ci)


# interest(10000, 5, 2)

# Q22. Write a function to return all factors of a number.

# def factors(n):
#     result = []

#     for i in range(1, abs(n) + 1):
#         if n % i == 0:
#             result.append(i)

#     return result


# print(factors(12))

# Q23. Write a function to find the second-largest number in a list.

# def second_largest(numbers):
#     unique = list(set(numbers))

#     if len(unique) < 2:
#         return None

#     unique.sort()

#     return unique[-2]


# numbers = [10, 20, 30, 40, 50]

# print(second_largest(numbers))



# Q24. Merge two lists without duplicates.

# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]

# result = []

# for i in list1 + list2:
#     if i not in result:
#         result.append(i)

# print(result)

# Q25. Find the second-largest and second-smallest elements.

# numbers = [10, 20, 30, 40, 50]

# unique = sorted(set(numbers))

# if len(unique) >= 2:
#     print("Second Largest:", unique[-2])
#     print("Second Smallest:", unique[1])
# else:
#     print("Not enough unique elements")

# Q26. Rotate a list to the left by k positions.

# numbers = [1, 2, 3, 4, 5]

# k = int(input("Enter rotation: "))

# k = k % len(numbers)

# result = numbers[k:] + numbers[:k]

# print(result)

# Q27. Separate even and odd numbers into two lists.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# even = []
# odd = []

# for i in numbers:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)

# print(even)
# print(odd)

# Q28. Find the common elements between two lists.
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]

# common = []

# for i in list1:
#     if i in list2 and i not in common:
#         common.append(i)

# print(common)


# Q29. Count the frequency of each element in a tuple.

# my_tuple = (1, 2, 3, 1, 2, 1, 4)

# frequency = {}

# for i in my_tuple:
#     frequency[i] = frequency.get(i, 0) + 1

# print(frequency)

# Q30. Find the union, intersection, and difference of two sets.

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# print("Union:", set1 | set2)

# print("Intersection:", set1 & set2)

# print("Difference:", set1 - set2)
# Q31. Check whether one set is a subset of another.

# set1 = {1, 2}
# set2 = {1, 2, 3, 4}

# if set1.issubset(set2):
#     print("Subset")
# else:
#     print("Not a subset")


# Q32. Count the frequency of words in a sentence.

# sentence = "python is easy and python is powerful"

# words = sentence.split()

# frequency = {}

# for word in words:
#     frequency[word] = frequency.get(word, 0) + 1

# print(frequency)

# Q33. Create a dictionary from two lists (keys and values).

# keys = ["name", "age", "city"]

# values = ["Harsh", 22, "Pune"]

# result = dict(zip(keys, values))

# print(result)

# Q34. Sort a dictionary by its values.

# my_dict = {
#     "Apple": 50,
#     "Banana": 20,
#     "Mango": 80,
#     "Orange": 40
# }

# result = dict(sorted(
#     my_dict.items(),
#     key=lambda x: x[1]
# ))

# print(result)



# Q35. Read a text file and count the number of lines, words, and
# with open("data.txt", "r") as file:
#     content = file.read()

# lines = content.splitlines()
# words = content.split()
# characters = len(content)

# print("Lines:", len(lines))
# print("Words:", len(words))
# print("Characters:", characters)

# Q36. Copy only the even-numbered lines from one file to another.

# with open("input.txt", "r") as source:
#     lines = source.readlines()

# with open("output.txt", "w") as destination:
#     for i, line in enumerate(lines, start=1):
#         if i % 2 == 0:
#             destination.write(line)

# Q37. Handle invalid integer input using try-except.

# try:
#     n = int(input("Enter a number: "))
#     print(n)

# except ValueError:
#     print("Please enter a valid integer")

# Q38. Handle file-not-found errors while reading a file.

# try:
#     with open("data.txt", "r") as file:
#         content = file.read()
#         print(content)

# except FileNotFoundError:
#     print("File not found")

# except PermissionError:
#     print("Permission denied")



# Q39. Create a random password generator using the random and string
# modules.
# import random
# import string

# def generate_password(length):
#     characters = string.ascii_letters + string.digits + string.punctuation

#     password = ""

#     for i in range(length):
#         password += random.choice(characters)

#     return password


# print(generate_password(12))

# Q40. Use the datetime module to calculate the number of days between two
# dates.

# from datetime import datetime

# date1 = input("Enter first date (DD-MM-YYYY): ")
# date2 = input("Enter second date (DD-MM-YYYY): ")

# d1 = datetime.strptime(date1, "%d-%m-%Y")
# d2 = datetime.strptime(date2, "%d-%m-%Y")

# difference = abs((d2 - d1).days)

# print("Total days:", difference)