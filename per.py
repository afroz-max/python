# # #keywords
# # import keyword
# # print(keyword.kwlist)

# # #datetime
# # import datetime
# # print(datetime.datetime.now())

# # help("modules")

# # #loops in python
# # #1.while loop

# # number = int(input("enter the number"))
# # i = 1
# # while i<11:
# #     print(number *i)
# #     i = i + 1

# # #while loop with else
# # x = 1
# # while x<3:
# #     print(x)
# #     x += 1
# # else:
# #     print("limit crossed")

# # #guessing game
# # #gernerate a random integer between 1 to 100
# # import random

# # jackpot = random.randint(1, 100)

# # guess = int(input("Guess the number: "))

# # while guess != jackpot:
# #     if guess < jackpot:
# #         print("Wrong! Guess higher.")
# #     else:
# #         print("Wrong! Guess lower.")

# #     guess = int(input("Guess again: "))
# #     counter += 1
# # else :
# #     print("correct guess")
# #     print("attempts",counter)

# # #for loop demo
# # for i in range(1,11):
# #     print(i)

# # for i in range(1,11):
# #     print(i)

# # for i in range(1,11,4):
# #     print(i)

# # for i in range(10, 0, -1):
# #     print(i)

# # for i in "delie":
# #     print(i)

# # #for loop
# # curr_pop = 1000
# # for i in range(10, 0, -1):
# #     print(i,curr_pop)
# #     curr_pop = curr_pop - 0.1 * curr_pop

#  #sequence sum
# #1/1! + 2/2! + 3/3! 
# n = int(input("enter n"))

# result = 0
# fact = 1

# for i in range(1,n+1):
#     result = result + fact
#     fact = fact * i

# print(result)

# #nested loop
# for i in range(1,5):
#     for j in range(1,5):
#         print(i,j)



#pattern
# rows = int(input('enter the number of rows'))
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print("*", end="")
#     print()



# rows = int(input('Enter the number of rows: '))

# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print("*", end="")
#     print()

#pattern
# rows = int(input("enter the number of rows"))

# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     for k in range(i-1,0,-1):
#         print(k,end="")  
#     print( ) 



# #loop control statements
# #break statement

# # for i in range(1,10):
# #     if i == 5:
# #         break
# #     print(i)



# lower =  int(input("enter the lower limit"))
# upper =  int(input("enter the upper limit"))
                   
# for i in range (lower,upper+1):
#     for j in range(2,i):
#         if i%j == 0:
#             break
#         else:
#             print(i)



# #contiue statement  
# for i in range(1,10):
#     if i ==5:
#         continue
#     print(i)

# #pass statement
# for i in range(1,10):
#     pass

#creating stings
s = "hello"
s = 'hello '
s = '''hello'''
print(s)


#Accessing characters in a string
# positive indexing

s = 'hello world'
print(s[0])

#negative indexing
s = 'hello world'
print(s[-1])

#slicing
s = 'hello world'
print(s[0:6:2])
print(s[6:0:-1])

print(s[::-1])


s = 'hello world'
print(s[-5:])

print(s[-1:-6:-1])


#eduting strings
# s = 'hello world'
# s[0] = "H"

# python strings are immutable


# s = 'hello world'
# del s
# print(s)

# s = 'hello world'
# del s[-1:-5:2] #error will  come

# print(s)


#operations on strings
#Arithmetic operations

print("delhi" + "mumbai")

print("delhi" + " "+ "mumbai")

print("delhi" * 3)

#Relational operations

print('delhi' == 'goa')
print('delhi' != 'goa')
print('delhi' > 'goa')#lexicographical comparison
print("Goa" > "goa")

#Logical operations
print("hello " and "world")
print("hello " or "world")
print(" " and "world ")
print(" " or "world ")
print(not "hello")

#Loops on strings

for i in "hello":
    print(i)

for i in "delhi":
    print('pune')

#Membership operations
print("D" in "Delhi")
print("D" not in "Delhi")

#Functions on strings
#common functions on strings
# len 
# max
#min
#sorted

print(len("heloo world"))

print(max("hello world"))

print(min("hello world"))

print(sorted("hello world"))

print(sorted("hello world", reverse = True))


#capitalize/Title/Upper/Lower/Swapcase its only works on strings

s = "hello world"
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.swapcase())

#count/find/indix
print("afroz is a not a good boy".count("a"))
print("afroz is a not a good boy".find("a"))
print("afroz is a not a good boy".index("a"))

#endswith/startswith
print("afroz is a not a good boy".endswith("boy"))
print("afroz is a not a good boy".startswith("afroz"))

#Format
name = "afroz"
gender = "male"
print("my name is {} and my gender is {}".format(name,gender))

#isalnum/isalpha/isdigit/isidentifier
print("afroz123%".isalnum())
print("afroz".isalpha())
print("123".isdigit())
print("afroz".isidentifier())

#split/join
s = print("afroz is a good boy".split())
s = print("afroz is a good boy".split('i'))

#joim
print(" ".join(['afroz','is','a','good','boy']))


#Replace
s = "afroz is a good boy"
print(s.replace("good","bad"))

#strip

s = "   afroz is a  good boy   "
print(s.strip())