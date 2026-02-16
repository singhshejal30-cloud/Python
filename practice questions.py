# print("hello, python learners!")

# name = 'adit'
# age = 18
# print( f"my name is {name} and i am {age} years old.")
# a = 10
# b = 5
# print(f"the result of addition {a} + {b} is: {a+b}")
# print(f"the result of subtraction {a} - {b} is: {a-b}")
# print(f"the result of multiplication {a} * {b} is: {a*b}")
# print(f"the result of division {a} / {b} is: {a/b}")

# #this program adds two numbers
# #step 1: store two numbers in variables
# num1 = 8
# num2 = 12
# # step 2: add the numbers sum = num1 + num2
# # step 2: add the numbers
# sum = num1 + num2
# # step 3: print the result
# print("the sum is:", sum)

# #printing multiple lines using one statement
# print("python is fun!\nlet's learn it step by step.\nkeep practing every day.")

# #comprative operators.
# x = 10
# y = 5
# print(x > y)
# print(x < y)
# print(x == y)
# print(x >= y)
# print(x != y)

# #operatore in python.
# x = 10
# y = 5
# print(x+y)
# print(x-y)
# print(x*y)
# print(x**y)
# print(x/y)
# print(x//y)
# print(x%y)

# #logical  operators:
# a = 5
# b = 6
# c = 7
# print(a<b and c>b)
# print(a>b or c>a)
# print(not c>a)

# x = 'true'
# y = 'true'
# print(x and y)
# print(x or y)
# print(not x)

# asignment operators
x = 10
y = 5
# x+=y
# print(x)
# x*=y
# print(x)
# x/=y
# print(x)
# x%=y
# print(x)
# x**=y
# print(x)
# x//=y
# print(x)

#loop concept(for loop)
# name = "shejal"
# for i in range(10):
#     print(name+str(i))

# for i in range(1,10):
#     print(name)

# for i in "python":
#     print(i)
# num =5
# for i in range(1,11):
#     print(num,"x",i,"=",num*i)
# else:
#     print("table completed")

# num = int(input("enter the number ="))
# for i in range(1,11,2):
#     print(num*i)
# else:
#     print("table completed")

#mostly for exams 
# for i in range(6):
#     print("*" * i)

# for i in range(11):
#     print("+"*i)

# #even number
# for i in range (2,21,2):
#     print(i)

# #odd numkber
# for i in range (1,19,2):
#     print(i)

#square
# for i in range (1,10):
#     print(i**2)

#sum of natural numbers
# total = sum(range(1,11))
# print(total)

# #reverse form
# for i in range(11,0,-1):
#     print(i)

#factorial of given number
# num = int(input("enter a number:"))
# factorial = 1
# for  i in range(1,num+1):
#     factorial = factorial*i
# print("factorial of",num,"is",factorial) 






#while loop
# num = 5
# while num>0:
#     print(num)
#     num-=1
# print("loop ends here")

# import time
# money =0
# while money<1000:
#     money+=50
#     time.sleep(2)
#     print("added money:",money)
# print("time's up")


# i = 1
# while i<=5:
#     print(i)
#     i+=1

#factorial
# num = int(input("enter a number: "))
# factorial = 1
# i = 1
# while i<=num:
#     factorial = factorial * i
#     i+=1
# print('factorial of',num,"is",factorial)

# import time
# classname = 1
# while classname<11:
#     print("class:", classname)
#     for i in range(1,11):
#         print(i,end=" ")
#         time.sleep(1)
#     print("\nattendance done")
#     classname+=1
# print("exit")

# classname = 1
# while classname<11:
#     print("class:", classname)
#     for i in range(1,11):
#         print(i,end=" ")
#     print("\nattendance done")
#     classname+=1
# print("exit")
# import time
# for round in range(1,4):
#     print("round:",round)
#     countdown = 3
#     while countdown>0:
#         print("countdown:",countdown)
#         time.sleep(1)
#         countdown-=1
#     print("round completed!")
#     print("next round!")

# customer = 1
# while customer<=3:
#     print("customer:",customer)
#     total = 0
#     for i in range(1,4):
#         amount = int(input("enter your amount: "))
#         total+=amount
#         print("total bill:",total)
#         print("next customer")
#         customer+=1

#data structure in python
#1. list method
# a = [1, 2, 3, "shejal", "riya","kajal","billu"]
# print(a)
# print(a[1])
# print(a[-1])

#2. slicing
# print(a[0:10])

#3. append method
# a.append("rohan")
# print(a)

#4. insert method
# a.insert(1,"NSTI")
# print(a)

# #5. remove method
# a.remove("billu")
# print(a)

# tuple method
# x = (1,"AIPA",2,"CSA",3,"EM")
# y = (4, "COSMO",5,"DM",)
# z=x+y
# print(z)

# x=(1,2,3,4,5,6)
# y=list(x)
# print(y)

# #loop method in tuple.
# students = ("shejal","shiya","riya","arpit")

# class Demo:
#     def method():
#         print("Hello")
# obj = Demo()
# obj.method()

# class Test:    
#      def __init__(self, value):        
#              self.value = value
# obj = Test(10)
# print(obj.value)
# class Test:    
#         count = 0
# def __init__(self):        
#                Test.count += 1
# a = Test()
# b = Test()
# print(Test.count)

# class MyClass:
#        def __init__(self):
#             self.num = 1
#        def increment(self):
#             self.num += 1
# obj = MyClass()
# obj.increment()
# obj.increment()
# print(obj.num)

# class Test:    
#       def __init__(self):        
#              self.name = "Python"
#       def display(self):        
#         print("Language:", self.name)
# obj = Test()
# obj.display()

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"name:{self.name}") 
        print(f"age:{self.age}")

name = input("enter your name: ") 
age = int(input("enter your age: "))
 
p1 = person(name, age)
p1.display_details()

class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius**2)

    def circumference(self):
        return 2 * 3.14159 * self.radius

radius = float(input("enter the radius: ")) 
circle1 = circle(radius)
print(f"area of the circle:{circle.area()}")
print(f"circumference of the circle: {circle1.circumference()}") 

# class example:
#     def __init__(self):
#         self.public_var = "public"
#         self._protected_var = "protected"
#         self.__private_var = "private"

#     def display(self):
#         print(self.public_var)
#         print(self._protected_var)
#         print(self.__private_var) 

# obj = example()
# print(obj.public_var)
# print(obj._protected_var)
# print(obj.__private_var)
# obj.display() 
class student:
    def __init__(self,name,roll_num):
        self.name = name
        self.roll_num = roll_num

    def print_details(self):
        print(f"name:{self.name}, roll number: {self.roll_num}")

s1 = student("shejal",1)
s2 = student("riya",2)

s1.print_details()
s2.print_details()


        









































