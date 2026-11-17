# Even or Odd Function
# Write a function is_even(n) that returns "Even" if the number is even, otherwise "Odd".
# num = lambda n : "even" if n % 2 == 0 else "odd" 

# print(num(5))
# print(num(6))
# print(num(7))
# print(num(8))

#normal function

def num(n):
    if n % 2 == 0:
        print ("even")
    else :
        print ("odd")
print(num(5))
print(num(6))
print(num(7))
print(num(8))






# Largest of Two Numbers
# Write a function largest(a, b) that returns the larger number.

# num = lambda a,b : "num a is large" if a > b  else " num b is large"
# print(num(12,14))
# print(num(200,50))

# Print Numbers
# Write a function print_numbers(n) that prints numbers from 1 to n using a loop.

# print_numbers = lambda n: [print(i) for i in range(1, n + 1)]

# print_numbers(60)

# Sum of Numbers
# Write a function sum_n(n) that returns the sum of numbers from 1 to n.


# def sum(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += i
#     return total

# print(sum(10))

# Multiplication Table
# Write a function table(n) that prints the multiplication table of n from 1 to 10.

# def table(n):
#     for i in range(1, 11):
#         print(f"{i} x {n} = {i * n}")

# table(22)
    
# Count Even Numbers
# Write a function that takes a list and returns how many even numbers it contains.
# Example:
# count_even([1, 2, 3, 4, 6])
# Output:3
# def even(numbers):
#     count = 0

#     for i in numbers:
#         if i % 2 == 0:
#             count += 1

#     return count

# print(even([1, 2, 3, 4, 6]))


# Find Maximum
# Without using max(), write a function that returns the largest number in a list.
 
# def find(numbers):
#     largest = numbers[0]

#     for i in numbers:
#         if i > largest:
#             largest = i

#     return largest

# print(find([10, 25, 5, 40, 15]))
    
# FizzBuzz
# Write a function that prints numbers from 1 to 100.

# def fizzbuzz():
#     for i in range(1, 101):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)

# fizzbuzz()
# If divisible by 3, print "Fizz".
# If divisible by 5, print "Buzz".
# If divisible by both, print "FizzBuzz".



# def fizzbuzz(): 
#     for i in range(1, 101):

#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")

#         elif i % 3 == 0:
#             print("Fizz")

#         elif i % 5 == 0:
#             print("Buzz")

#         else:
#             print(i)

# fizzbuzz()

# Palindrome Checker
# Write a function that returns True if a string is a palindrome.
# def palindrome(word):
#     if word == word[::-1]:
#         return True
#     else:
#         return False

# print(palindrome("madam"))
# print(palindrome("hello"))


# Count Vowels
# Write a function that counts the vowels in a string.
# def count_vowels(word):
#     count = 0

#     for i in word.lower():
#         if i in "aeiou":
#             count = count + 1

#     return count

# print(count_vowels("Education"))









# Second Largest Number
# Write a function that returns the second largest number in a list without using sort().
# def second_largest(numbers):
#     largest = float('-inf')
#     second = float('-inf')

#     for i in numbers:

#         if i > largest:
#             second = largest
#             largest = i

#         elif largest > i > second:
#             second = i

#     if second == float('-inf'):
#         return None

#     return second

# print(second_largest([10, 25, 40, 15, 30]))









# Guessing Game
# Generate a random number between 1 and 10.
# Keep asking the user to guess until they get it right.
# import random

# def guessing_game():

#     number = random.randint(1, 10)

#     while True:

#         guess = int(input("Guess a number between 1 and 10: "))

#         if guess == number:
#             print("Congratulations! Correct guess.")
#             break

#         elif guess > number:
#             print("Too high! Try again.")

#         else:
#             print("Too low! Try again.")

# guessing_game()















# Use a loop, conditionals, and functions.

#       Write a function grade(marks) that:
# Returns "A" for marks ≥ 90
# Returns "B" for marks ≥ 80
# Returns "C" for marks ≥ 70
# Returns "D" for marks ≥ 60
# Otherwise returns "F"

# def grade(marks):

#     if marks >= 90:
#         return "A"

#     elif marks >= 80:
#         return "B"

#     elif marks >= 70:
#         return "C"

#     elif marks >= 60:
#         return "D"

#     else:
#         return "F"


# print(grade(95))
# print(grade(85))
# print(grade(75))
# print(grade(65))
# print(grade(45))








 
