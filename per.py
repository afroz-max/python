# #keywords
# import keyword
# print(keyword.kwlist)

# #datetime
# import datetime
# print(datetime.datetime.now())

# help("modules")

# #loops in python
# #1.while loop

# number = int(input("enter the number"))
# i = 1
# while i<11:
#     print(number *i)
#     i = i + 1

# #while loop with else
# x = 1
# while x<3:
#     print(x)
#     x += 1
# else:
#     print("limit crossed")

# #guessing game
# #gernerate a random integer between 1 to 100
# import random

# jackpot = random.randint(1, 100)

# guess = int(input("Guess the number: "))

# while guess != jackpot:
#     if guess < jackpot:
#         print("Wrong! Guess higher.")
#     else:
#         print("Wrong! Guess lower.")

#     guess = int(input("Guess again: "))
#     counter += 1
# else :
#     print("correct guess")
#     print("attempts",counter)

# #for loop demo
# for i in range(1,11):
#     print(i)

# for i in range(1,11):
#     print(i)

# for i in range(1,11,4):
#     print(i)

# for i in range(10, 0, -1):
#     print(i)

# for i in "delie":
#     print(i)

# #for loop
# curr_pop = 1000
# for i in range(10, 0, -1):
#     print(i,curr_pop)
#     curr_pop = curr_pop - 0.1 * curr_pop

 #sequence sum
#1/1! + 2/2! + 3/3! 
n = int(input("enter n"))

result = 0
fact = 1

for i in range(1,n+1):
    result = result + fact
    fact = fact * i

print(result)

#nested loop

