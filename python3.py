# #python lists

# # a = 2
# # print(id(2))

# L = [1,2,3,4]
# print(id(L))
# print(id (L[0]))
# print(id(L[1]))
# print(id(L[2]))
# print(id(1))
# print(id(2))
# print(id(3))

# #characterstics of a list
# #creating a list
# #Empty
# print([])
# #1D homo
# print([1,2,3,4])

# #2D
# print([1,2,3],[4,6])

# #3D
# print([[[1,2],[3,4]],[[5,6],[7,8]]])

# #heterogeneous
# print([1,2.0,"hello",True])

# #using the type conversion
# # print(list("hello"))

# # #accessing items form a list
# # #indexing
# # L = [1,2,3]
# # print(L[1])
# # #positive indexing 
# # print(L[-1])

# # #slicing
# # L =[1,2,3,4,5]
# # print(L[1:4])
# # print(L[-1:2])

# # #adding items to a list
# # #append
# # L = [1,2,3,4,5]
# # L.append(True)
# # print(L)

# # #extend
# # L = [1,2,3,4,5]
# # L.extend([6,7,8])
# # print(L)

# # L = [1,2,3,4,5]
# # L.extend("delhi")
# # print(L)

# # #insert
# # L = [1,2,3,4,5]
# # L.insert(1,100)
# # print(L)

# # #Editing iterns in a list
# # L = [1,2,3,4,5]
# # L[-1] = 100
# # L[1:4] = [200,300,400] #slicing
# # print(L)


# #deleting items from a list

# #del
# L = [1,2,3,4,5]

# del L[0]
# print(L)

# #slice
# del L[1:3]
# print(L)

# #REMOVE
# L = [1,2,3,4,5]
# L.remove(5)
# print(L)

# #pop
# # L = [1,2,3,4,5]
# # L.pop(1)
# # print(L)

# # #clear
# # L = [1,2,3,4,5]
# # L.clear
# # print(L)

# # #opertions on list
# # #arithmetic (+,*)
# # L1 = [1,2,3,4,5]
# # L2 = [6,7,8,9]
# # print(L1+L2)
# # print(L1*3)

# # #membership

# # L1 = [1,2,3,4,5]
# # L2 = [1,2,3,4,[5,6]]

# # print(5 not in  L1)
# # print([5,6] in  L2)

# # #loops
# # L1 = [1,2,3,4,5]
# # L2 = [1,2,3,4,[5,6]]
# # L3 = [[[1,2],[3,4]],[[5,6],[7,8]]]

# # for i in L1:
# #     print(i)

# # for i in L2:
# #     print(i)

# # for i in L3:
# #     print(i)


# #list functions

# #ien/min/max/sorted
# # L =[2,1,5,66,8]
# # print(len(L))
# # print(min(L))
# # print(max(L))
# # print(sorted(L))
# # print(sorted(L,reverse=True))

# #count
# L = [1,2,1,3,4,1,5]
# L.count(5)


# #index
# L = [1,2,3,4,5,6,78,9,8,8,8,]
# L.index(2)

# #revers
# L = [1,2,1,3,4,1,5]

# L.reverse()
# print(L)

# #sort  vs sorted
# L = [1,2,1,3,4,1,5]
# print(L)
# print(sorted(L))
# print(L)
# L.sort()
# print(L)

# #copy

# L = [1,2,3,4,5]
# print(L)
# print(id(L))
# L1= L.copy()
# print(L1)
# print(id(L1))

# #list comprehension
# L = []

# for i in range(1,11):
#     L.append(i)
#     print(L)

# L = [i for i in range(1,11)]
# print(L)

# v = [2,3,4]
# s = -3
# # print(v*s)

# # x = []
# # for i in v:
# #     x.append(i*s)

# # print(x)


# [s*i for i in v]


# L =[1,2,3,4,5]
# [i**2 for i in L]

# [i for  i in range(1,5) if i%5 == 0]


# languages = ["app","banga","obito","rin"]
# print = [languages for languages in languages if languages.startswith("p")]


# basket = ['apple', 'guava', 'cherry', 'banana']
# my_fruits = ['apple', 'kiwi', 'grapes', 'banana']
# [fruit for fruit in my_fruits if fruit in basket if fruit.startswith('a')]


# [[i*j for i in range(1,4)] for j in range(1,4)]

# L1 =[1,2,3,4]
# L2 =[5,6,7,8]
# [i*j for i in L1 for j in L2]

# 2ways to traverse a list
#itemwise


L =  [1,2,3,4]

for i in L:
    print(i)

#indexwise
L =  [1,2,3,4]

for i in range(0,len(L)):
    print(L[i])

#zip
L1 = [1,2,3,4]
L2=[-1,-2,-3,-4]

list(zip(L1,L2))

[i*j for i,j in zip(L1,L2)]


L =[1,2,print,type,input]
print(L)


a = [1,2,3]
b = a 
print(a)
print(b)
a.append
print(a)
print(b)
