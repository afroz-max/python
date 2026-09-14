print("hello world ")
print("hello",1,4.5,True)

print("hello",1,4.0,True,sep="/")

print("hello")
print("world")


print("afroz",4,1.5,True)
print("afroz",4,1.5,True,sep='/')

print("lucfier")
print("devil")

print("lucfier",end='/')
print("devil")

print("lucfier",end='')
print("devil")

print(8)#integer
print(1e308)

print(1.5)#foat
print(1.7e306)

print(True)#boolen
print(False)

print("lucfier")#string

print(5+6j)#complex

print([5,8,9])#list

print((5,9,8))#tuple

print({8,9,5})#set

print({"name ":"afroz","age":20})#dictionary


#type 
print(8,type(8))

#variable
a = 10
b = 20
print(a+b)

#Dynamic typing
a = 10 #it mean by the we no need to say about the which datetye of the variable 

#static typing
#nt a = 10

#Dyanmic binding
a = 6
print(a)
a = "lucfier"
print(a)

#static binding
#int a = 6

a = 55
b = 25
c = 5
print(a+b+c)

#are we can wirte the code in the single line
a,b,c = 5,6,8
print(a,b,c)

a=b=c=5
print(a,b,c)

#comments
# This is a single-line comment

#keyworsds 

   #print="print"
   #print(print)

#identifier
#you can't start with a number are digit 1name = "afroz"# but you can use in this way

name1 = "afroz"
#you can use the special character ->_
_ = "afroz"
print(_)
#identifier can not use in the keywords


#user output
#static vs dynamic 

# input('what is your name ')


# fnum= input("enter first number")
# snum = input("enter second number")
# sum = fnum + snum
# print(sum)

#Type of conversion
#impicit and expicit 

#impicit
a = 5
b = 2.5
sum = a +b 
print(sum)

# a = 5
# b = "5"
# sum = a + b 
# print(sum)

#expicit
#
# fnum= input("enter first number")
# snum = input("enter second number")
# sum = int(fnum) + int(snum)
# print(sum)

a = 8
b = "5"
sum = a + int(b)
print(sum)

print(type(b))


a = True + 8
b = False + 8
print("a;",a)
print("b:",b)



print("lucfier the devil true",1,40,sep = '/')
print("afroz is only ",False,4,4.5,sep = "")

print("hello")
print("world")


print("afroz",4,1.5,True)
print("afroz",4,1.5,True,sep='/')

print("lucfier")
print("devil")

print("lucfier",end='/')
print("devil")

print("lucfier",end=" ")
print("devil")

print(8)#integer
print(1e308)