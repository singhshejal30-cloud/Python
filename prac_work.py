# #factorial of given number
# num = int(input("enter a number:"))
# factorial = 1
# for  i in range(1,num+1):
#     factorial = factorial*i
# print("factorial of",num,"is",factorial)

# #Remove duplicate elements:
# list=[1,2,2,3,4,3,5]
# new_list = []
# for item in list:
#     if item not in new_list:
#         new_list.append(item)
# print("list without duplicates:", new_list)

# list = [10,20,4,15]
# largest = second=float('-inf')

# for i in list:
#     if i > largest:
#         second = largest
#         largest = i
#     elif i> second and i != largest:
#         second = i
# print(second)

# A = [1,3,5]
# B = [2,3,6]
# result = []
# i = 0
# while i<len(A) or i< len(B):
#     if i < len(A):
#         result.append(A[i])
#     if i < len(B):
#         result.append(B[i])
#     i += 1
# print("Merge list:",result)             

# A = [1,2,3,4]
# B = [2,3,5,6] 
# result = []
# for x in A:
#     if x in B and x not in result:
#         result.append(x)
# print(result) 

# list = [1,2,3,4] 
# squared = []
# for i in list:
#     squared.append(i * i)
# print(squared)

# list = [1,2,3,4,5,6]
# even = []
# odd = [] 
# for i in list:
#     if i % 2== 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("Even:", even)
# print("Odd:", odd) 

#Rotate list to the right by N steps
# num_list = [1,2,3,4,5,6]
# N = 2
# N = N % len(num_list)
# result = num_list[-N:] + num_list[:-N]
# print(result) 


# #9. Elements common in all three lists
# A = [1,2,3,4]
# B = [2,3,5]
# C = [3,2,6]
# common = []
# for x in A:
#     if x in B and x in C and x not in common:
#         common.append(x)
# print(common)


#lecture notebook practice

#set type datatype
# u_n = {1,2,3,3,3,4,5,5}
# u_n.remove(1)
# print(u_n)

# i_s = frozenset([1,2,3,3,3,4,4,5,6,6])
# print(i_s)

#element badalna inex method ka use karke
# lst = [1,2,3,4]
# lst[2] = 10
# print(lst)

#identity operator
# a = [1,2,3,4]
# b=a
# c = [1,2,3,4]
# print(a is b)
# print(a is not c)

# memebership operator
# veg = ['karela','aloo','gajar']
# print('bhindi' in veg)

# #flow control statement
# #(i) conditional statement
# age = int(input("enter your age: "))
# if age >=18:
#     print("you can vote")
# elif age <= 0:
#     print("you are not eligible for vote")
# elif age>=100:
#     print("greater then 100!")    
# else:
#     print("you cannot vote")

# num_1 = int(input("enter number_1: "))
# num_2 = int(input("enter number_2: ")) 
# choice = input("enter your choice + - * /: ")
# if choice == '+':
#     print(f"addition {num_1 + num_2}")
# elif choice == '-':
#     print(f"substraction{num_1 - num_2}")
# elif choice == '*':
#     print(f"multiplication{num_1 * num_2}")
# elif choice == '/':
#     print(f"dividsion{num_1 / num_2}")
# else:
#     print("invalid choice!")               
    

# #(ii) looping.
# #for loop:
# a = [1,2,3,4,5]
# for i in a:
#     print(i)

#while loop:
# i = 1
# while i<=5:
#     print(i)
#     i+=1 

# a = tuple(range(1,11,1))
# print(a)

#nested loop
# for i in range(1,3):
#     for j in range(3,6):
#         print(f"{i},{j}")

# for num in range(1,10,1):
#     if num ==5:
#         break
#     print(num)

# for num in range(1,5):
#     if num ==3:
#         continue
#     print(num)

# for num in range(1,10,1):
#     if num ==5:
#         pass
#     print(num)

# #even number
# num = int(input("enter a number: "))
# if num%2 ==0:
#     print("even")
# else:
#     print("odd")

# for i in range(1,11):
#     if i % 2 == 0:
#         print('even',i)
#     else:
#         print('odd',i)

#string
# a = "shejal"     #koi ek element print karvane ke liye
# print(a[0]) 

#iterable
# language = "python"
# for i in language:
#     print(i)

#len() integer.
# str = "python"
# print(len(str))

# password = "123@python"
# if len(password)>5:
#     print('login successfull')
# else:
#     print('length is too short or <5')    

# #slicing
# text = "this_is_python_king_of_AI"
# print(text[0:50:1])

# #string ko repeat karvana
# num = "10"
# print(num * 2)

# #concatenate
# name = "shejal"
# ser_name = "singh"
# print('hi',name + ser_name)

# #checking membership
# email = "singhsheju19@gmail.com"
# if "riya" in email:
#     print('valid email')
# else:
#     print("in-valid")

#lowar case use in string
# str = 'THIS IS PYTHON'.lower()
# print(str)

# str = input("enter your name= ").lower()
# print(str)

# str = input('enter your name= ').capitalize()
# print(str)

# str = input('enter a sentence=').title()
# print(str)

# str = input('enter a sentence=').swapcase()
# print(str)

# #searching and replacing method
# text = "python programming"
# print(text.find('t'))

# #spliting and joining method
# str = "a,b,c"
# s = str.split(",")
# print('after splitting',s)

# #join(iterable)
# str = "a,b,c"
# s = str.split(",")
# print('after splitting',s)
# result = ','.join(s)
# print(result)

#checking method
# str = "python"
# print(str.startswith('p'))
# print(str.endswith('n'))
# print(str.isalpha())
# print(str.isalnum())
# print(str.isdigit())
# print(str.islower())
# print(str.isupper())
# print(str.istitle())























    





         














