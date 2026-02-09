# name = "shejal"
# for i in range (10):
#     print(name)

# name = "shejal"
# for i in range (11):
#     print(name + str (i))

# for i in range (2,11):
#     print(i)

# num = 5
# for i in range (1,21):
#     print(num, "x", i, "=" , num*i)
# else:
#     print("table completed")

# num = 2
# num = int(input("enter your number:"))
# for i in range (1, 11,2):
#     print(num,"x",i, "=", num*i)
# else:
#     print("table completed")

# for i in range (6):
#     print("*" * i)

# num = 3
# for i in range (1,11):
#     print(num*i)


# #practice 
# num = 5
# for i in range (11):
#     print(num)

# name = "shejal"
# for i in range (5):
#     print(name)

# #even number
# for i in range (2, 21, 2):
#     print(i)

# #odd number
# for i in range(1, 19,2):
#     print(i)

# #square
# for i in range(1,10):
#     print(i**2)

# #multiplication table
# num = 5
# for i in range(1,11):
#     print(num, "multiplication of", i,"=", num*i)

# #reverse form.

# #find the sum of natural number
# total = sum(range(1,11))
# print(total)

# #factorial of given number.
# num = int(input('enter a number:'))
# factorial = 1
# for i in range(1,num +1):
#     factorial = factorial*i
#     print("factorial of",num, "is", factorial)


# #while loop.
# num = 5
# while num>0:
#     print(num)
#     num-=1
# print("LOOP ENDS HERE")

# num = int(input("enter the number:"))
# while num >0:
#     print(num)
#     num-=1
# print("LOOP ENDS HERE")

apple = 10
while apple>0:
    print("eat apple:",apple)
    apple-=1
print('finished')
import time
money = 0
while money<1000:
    money+=50
    time.sleep(2)
    print('added money:', money)
print("time's up")