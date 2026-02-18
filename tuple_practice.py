
# # creating a tuple.
# fruits = ('banana','guava','apple','cherry','grape')
# print(fruits)

# # accessing elements in a tuple
# numbers = (10,20,30,40,50)
# print("first element:", numbers[0])
# print("last element:", numbers[-1])

# # slicing a tuple
# colors = ('red','blue','green','yellow','purple','orange')
# print("middle three colors:")
# print(colors[2:5])

# #concatenating two tuples
# tuple1 = (1,2,3)
# tuple2 = (4,5,6)
# result = tuple1 + tuple2
# print("concatenated tuple",result)

# #iterating through a tuple
# animals = ('cat','dog','rabbit','elephant')
# for i in animals:
#     print(i)

# # membership test in a tuple
# fruits = ('mango','apple','banana','cherry')
# if 'apple' in fruits:
#     print("apple is present")
# else:
#     print("apple not found")

# nested tuples and accessing their elements
student = ("rahul",(85,90,92))
print("rahul's second mark:",student[1][1])

# #applying built in functions on tuples
# numbers = (5,10,15,20,25)
# print("length:", len(numbers))
# print("minimum:", min(numbers))
# print("maximum:", max(numbers))
# print("sum:",sum(numbers))

# #deleting a tuple
# cities = ('Delhi', 'Mumbai', 'Kolkata', 'Chennai')
# del cities
# print("tuple deleted successfully")


# # updating a tuple
# fruits= ("apple","banana",'cherry')
# fruits_list=list(fruits)
# fruits_list[1]='orange'
# fruits = tuple(fruits_list)
# print(fruits)










# set method
# x={1,2,3,4,5,}
# x.add(6)     #ek chij add karne ke liye
# print(x)

# x= {"shiya"}
# x.update(['shejal','raj'])   #multiple chijen add karne ke liye
# print(x)

# y={"aipa","em","copa"}
# z={"fdt","csa","copa"}
# print(y.union(z))
# print(y.intersection(z))
# print(y.difference(z))
# print(y.issubset(z))

# x = {"a","b","c"}
# y = {"z","a","u","s","b","c"}
# print(x.issubset(y))

