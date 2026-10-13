#python lists

# a = 2
# print(id(2))

L = [1,2,3,4]
print(id(L))
print(id (L[0]))
print(id(L[1]))
print(id(L[2]))
print(id(1))
print(id(2))
print(id(3))

#characterstics of a list
#creating a list
#Empty
print([])
#1D homo
print([1,2,3,4])

#2D
print([1,2,3],[4,6])

#3D
print([[[1,2],[3,4]],[[5,6],[7,8]]])

#heterogeneous
print([1,2.0,"hello",True])

#using the type conversion
print(list("hello"))

#accessing items form a list
#indexing
L = [1,2,3]
print(L[1])
#positive indexing 
print(L[-1])

#slicing
L =[1,2,3,4,5]
print(L[1:4])
print(L[-1:2])

#adding items to a list
#append
L = [1,2,3,4,5]
L.append(True)
print(L)

#extend
L = [1,2,3,4,5]
L.extend([6,7,8])
print(L)

L = [1,2,3,4,5]
L.extend("delhi")
print(L)

#insert
L = [1,2,3,4,5]
L.insert(1,100)
print(L)

#Editing iterns in a list
L = [1,2,3,4,5]
L[-1] = 100
L[1:4] = [200,300,400] #slicing
print(L)

