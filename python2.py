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
for i in range(1,5):
    for j in range(1,5):
        print(i,j)
