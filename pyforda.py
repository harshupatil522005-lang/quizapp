# import pandas as pd
# data = {
#     "name": ["amit","rahul","rushi","harsh"],
#     "salary":[20000,30000,10000,20000]
# }
# df = pd.DataFrame(data)
# print(df)
# print("1 average salary:",df["salary"].mean()) #average in values
# print("2 Minimum salary:",df["salary"].min()) #minimum value
# print("3 Maximun salary:",df["salary"].max()) #maximum value
# print("4 Total salary:",df["salary"].sum()) #additon of vlaues
# print("5 Most Frequent salary:",df["salary"].mode()) #repeated value
# print("6 Middle one salary:",df["salary"].median()) #middle value
# print("7 Count  salary:",df["salary"].count()) #counting all non null values
# print("8 standard salary:",df["salary"].std()) #difference between values
# print("9 Variance salary:",df["salary"].var()) #sqaured difference in values

#format string

# n=7

# for i in range(1,11):
#     print(f"{i} x {n} = {i * n}")

# name = input("Enter your name :") #string
# age = input("Enter your age: ") #int
# city = input("Enter your city: ") #string

# print(f"Your name is {name} age{age} live in {city}")

#
# def greetings_01():
#     print("girittings")
# def greetings():
#     return "girittings"

# print(greetings())

# greetings_01()

#function with parameters

# def sumtwo(a,b):  #parameters
#      return a+b

# print(sumtwo(10,20))

# def table(n):
#     for i in range(1,11):
#         print(f"{i} x {n} = {i * n}")

# table(7)

# print("\n")
# table(8)

# print("\n")

# def add(n):
#     for i in range(1,11):
#         print(f"{i} + {n}")
#         add(3)


# def person(name="harsh"):
#     print("your name is:", name)

# person()
# person("hey Harsh")

# def square(n):
#     return f"your square of {n} is {n*n}"
# print(square(10))
    
#lambda function

# result = lambda n : n * n 
# print(result(4))

# num = lambda n : "even" if n % 2 == 0 else "odd" 

# print(num(5))
# print(num(6))
# print(num(7))
# print(num(8))

#revision function 

#def myname(name="harsh")
#print (f"this is your name {nanme}")

#myname()
#def numbers(*args):
#  print(sum(args))

#def result(x):
# return x + 100

# result = lambda x : x + 100
#  print (result(80))


# def guess(n):
#     if n >= 0:
#         print("positive num")
#     elif 
#         print("negative num")
#     elif  
#         print("negative num")
#     guess(5)

# def countdown(n):
#     while(n >= 0):
#          print(n)
#          n-=1

#     print("launch sucessful")


# countdown(10)

#remove space from a string

# string = "hello myself harsh ha ah ah a"

# for ch in string:
#     if ch == " ":
#         continue
#     print(ch)


# def removespace(str):

#     result_string = " "

#     for ch in str:
#         if ch == " ":
#             continue
#         result_string+=ch


#     return result_string 


# print(removespace("welcome to pune"))

 
     
# def convert_lowercase(char):
#     return char.lower()

# print(convert_lowercase("A"))


# def vowels(text):
#     for char in text.lower():
#         if char in "aeiou":
#             print(char)

# vowels("harshvardhan prakash patil")




# def replace_char(text):
#     return text.replace("h", "i")

# print(replace_char("hello"))


b = 6 #global

def Outer():
    b= 9 #enclosing

    

    def Inner():
        b= 10 #local

        print(b)

    Inner()
  
Outer()





