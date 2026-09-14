
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
