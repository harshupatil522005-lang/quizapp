# def greetings():

#     print("hello")



# greetings()


# num1 = int(input("Enter num 1 :- "))
# num2 = int(input("Enter num 2 :- "))


# multiplication = lambda a,b : a * b



# print(multiplication(num1,num2))

# fruit = ["apple","mango","orange","banana","kivi"]

# add = lambda x : x + "2"
# result = map(add,fruit)

# print(list(result))

# fruit = ["apple","mango","orange","banana","kivi"]
# def add(x) :
 
#     return x + "4"

# result = map(add,fruit)

# print(list(result))

# print ("quiz app")

# score = 0 

# answer = input("what is capital of india ")
# if answer.lower() == "delhi":
#     print("Correct")
#     score += 1
# else: 
#     print("Wrong!! Answer is delhi")

# answer = input("2. Which language is used for AI? ")
# if answer.lower() == "python":
#     print("Correct!")
#     score += 1
# else:
#     print("Wrong!! Answer is Python")


# answer = input("3. What is 10 + 5? ")
# if answer.lower() == "15":
#     print("Correct!")
#     score += 1
# else:
#     print("Wrong! Answer is 15.")


# print("Your result")
# print(" Your score", score , "/ 3" )

# if score == 3:
#     print("Excellent!")
# elif score == 2:
#     print("Good job!")
# else:
#     print("Keep practising!")


import random

# Generate OTP
otp = random.randint(100000, 999999)

print("Your OTP is:", otp)

# Take OTP from user
takeotp = int(input("Enter your OTP: "))

# Verify OTP
if takeotp == otp:
    print("OTP Verified Successfully!")
else:
    print("Invalid OTP!")



