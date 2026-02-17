# my_list = [1,2,3,10.56, "hello", "true"]
# print(my_list)

# my_list = list((1,2,3,10.56, "hello", "true"))
# print(my_list)

# list = [1,2,3,4,5]
# print(f'before list{list}')
# list[0]="hello"
# print(f'after list{list}')

# #slicing
# list = [1,2,3,4,5]
# list[0:3] = 10,20,30
# print(list)

#concate
# lst1 = [1,2,3,4,5]
# lst2 = [6,7,8,9,10]
# result = lst1 +lst2
# print(result)

# #repetation
# str = [1,2,3,4,"shejal","riya"]
# print(str*3)

# #membership
# lst_1 = [1,2,3,4,5]
# check = int(input('enter a number to check= '))
# if check in lst_1:
#     print('found')
# else:
#     print('not found')

# lst_2 = [6,7,8,9,10] 
# check = int(input('enter a number= '))
# if check not in lst_2:
#     print('yes not found') 
# else:
#     print('found')

# #aliasing:
# lst1 = [1,2,3]
# lst2 = lst1 
# lst2[0] =100
# print(lst1,lst2)

# #copy methyod
# list_1 = [1,2,3]
# list_2 = list_1.copy()
# list_2[0] = 100
# print(list_1,list_2)

# #append
# a = [1,2,3,4,5]
# a.append(6)
# print(a)

# name = ['shejal','teena','shipra','riya']
# name.append('kajal')
# print(name)

# #extend
# a = [1,2,3,4,5]
# b = [6,7,8,9,10]
# a.extend(b)

# #insert
# a = [1,2,3]
# a.insert(0,"hii coders")
# print(a)

# name = ['shejal','riya']
# name.insert(1,"arpit")
# print(name)

# #pop method
# a = [1,2,3,4,5]
# popped = a.pop(0)
# print(a)

# name = ['shejal','riya']
# name.pop(0)
# print(name)

# #clear method
# a = [1,2,3,4,5]
# cleared = a.clear()
# print(a)

# #index method
# a = [1,2,3,4,5,6,7]
# index = a.index(5)
# print(index)

# #count method

# a = [1,2,3,4,5,6,7,"python","java","true",1,1,1,5,6,7,4,3,4]
# counter = a.count(1)
# print(counter)

# #Sort method
# a= [90,50,120,-1.5,-10,4,5]
# sorted = a.sort()
# print(a)

#reverse method:
# a = "python programming is fun"
# print(a[::-1])

# #finding method:
# a = [1,2,3,-10,-5,100,200]
# print(min(a))
# print(max(a))

# #Common method:
# a = [1,2,3,4,5,6,7,8,9,10]
# b = [2,4,6,8,9,45,6,7,8]
# s1 = set(a)
# s2 = set(b)
# s3 = s1.intersection(s2)
# print(list(s3))

# y = {"aipa","csa","em","copa"}
# z = {"copa","csa","em"}
# print(y.intersection(z))

#nested list:
# a = [1,2,3]
# b = [4,5,6,a,[7,8,9]]
# print(b)

# #range
# num = (list(range(1,10)))
# print(num)

# #list comprehenson
# square = []
# for i in range(0,11):
#     square.append(i**2)
# print(square)

# square for even numbers
# square = [i ** 2 for i in range(1,11)if i%2 ==0]
# print(square)

# num = int(input("enter a number:"))
# if num%2==0:
#     print('even number')
# else:
#     print('odd number') 

# for i in range(1,11):
#     if i%2==0:
#         print("even no.",i)
#     else:
#         print("odd no.",i)

#tuple 
#concatenation
name = ("shejal","riya","shipra","shakshi","anamika")
ser_name = ("singh","sherma","yadav","maurya","rai")
# print(name + ser_name)
# print(f"{name},{ser_name}")

# #slicing
# print(name[0:3])

#len
# print(len(name))
# print(len(ser_name))
# if len(name) >6:
#     print('yes this is right')
# else:
#     print('no')

#index
    


















