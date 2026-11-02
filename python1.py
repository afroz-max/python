
#Arithmentic operators
print(5+6)
print(5-6)
print(5*6)
print(5/6)
print(5//6)
print(5%6)
print(5**6)


#Relational operators
print(5>6)
print(5<6)
print(5>=6)
print(5<=6)
print(5==6)
print(5!=6)

#Logical operators
print(1 and 0)
print(1 or 0)
print(not 0)

#Bitwise operators
# bitwise and
print(2&3)
# bitwise or
print(2|3)

#bitwise xor
print(2^3)

print(~2)

print(2<<3)

print(2>>3)

#Assignment operators
a = 6
#a= a + 6 
a += 6

print(a)


#Membership operators

#in/not in

print("D" in "Delhi")
print("D" not in "Delhi")

print(1 in[2,3,4,5,5])

#program to find the sum of a 3 digit number entered by the user

number = int(input("enter any 3 digit number")) #345
#345 % 10 -> 5 
a = number %10
number = number // 10

#34%10  -> 4
b = number % 10
number = number // 10

#3%10  -> 3 
c = number % 10
number = number // 10

print(a + b +c)

#if-else in the python 

email = input("enter email")
password = input("enter password")

if email == "lucfier@.com" and password =="123":
    print("devil")
elif email == "lucfier@.com" and password !="123": 
    print("incorrect password")
    password = input("enter password again")
    if password == "123":
        print("devil")

    else :
        print("you cant do it ")
    
else:
    print("not correct")

# min of 3 numbers

a = int(input('first number'))
b = int(input("second number"))
c = int(input("third number"))

if a<b and a<c:
    print("smallest number is ",a)
elif b<c:
    print("smallest number is ",b)
else:
    print("smallest number is ",c)



# menu driven calculater
fnum = int(input("enter the first number"))
snum = int(input("enter the second number"))

op = input("enter the operation")
if op == '+':
    print(fnum +snum)
elif op == '-':
    print(fnum -snum)
elif op == '*':
    print(fnum *snum)
elif op == "/":
    print(fnum/snum)
    
menu = input("""
hi! how can in help you.
1.enter 1 for pin chnage
2.enter 2 for balance enquiry
""")
if menu== '1':
    print("pin changed successfully")
elif menu== '2':
    print("your balance is 10000") 

#moduless in python
 #maths
import math
math.factorial(5)

#keywords
import keyword
print(keyword.kwlist)

#random
import random
print(random.randint(1,100))

#datetime
import datetime
print(datetime.datetime.now())

help("modules")

#loops in python
#1.while loop

number = int(input("enter the number"))
i = 1
while i<11:
    print(number *i)
    i = i + 1

#while loop with else
x = 1
while x<3:
    print(x)
    x += 1
else:
    print("limit crossed")

#guessing game
#gernerate a random integer between 1 to 100
import random

jackpot = random.randint(1, 100)

guess = int(input("Guess the number: "))

while guess != jackpot:
    if guess < jackpot:
        print("Wrong! Guess higher.")
    else:
        print("Wrong! Guess lower.")

    guess = int(input("Guess again: "))
    counter += 1
else :
    print("correct guess")
    print("attempts",counter)

#for loop demo
for i in range(1,11):
    print(i)

for i in range(1,11):
    print(i)

for i in range(1,11,4):
    print(i)

for i in range(10, 0, -1):
    print(i)

for i in "delie":
    print(i)

#for loop
curr_pop = 1000
for i in range(10, 0, -1):
    print(i,curr_pop)
    curr_pop = curr_pop - 0.1 * curr_pop

 