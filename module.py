# import function
# print(function.sub(10,7))

import math
# print(math.sqrt(9))
# print(math.pi)
# print(math.pow(2,4))
# print(math.factorial(5))

import datetime
# now = datetime.datetime.now()
# print(now)
# print(now.year)
# print(now.month)
# print(now.day)

today = datetime.date.today()
# print(today)

# future = today+datetime.timedelta(days = 10)
# print("10 days later:",future)

import sys
# print(sys.version)
# print(sys.executable)
# print(sys.platform)

import random
# print(random.randint(1,10))
# print(random.random())
# print(random.choice(["aipa","csa","em","dm"]))
# trade = ['aipa','em','csa','dm']
# random.shuffle(trade)
# print(trade)

# import os
# print(os.getcwd())
# print(os.listdir())
# os.mkdir("AIPA")

# os.rmdir("AIPA")

# import time
# # print(time.ctime())

# #practice
# #Question 1.
# r = pow(2,4)
# print(math.pi*r)

# #Question 2.
# print(math.factorial((int(input("enter factorial:")))))
# print(math.sqrt(int(input("enter sqrt:"))))

# #Question 3.
# print("and the number is...",random.choices(["1","2","3","4","5"]))

# #Queston 4.
# print("guessing game:",random.choices([1,2,3,4,5,6,7,8,9]))

# #Question 5.
# print(time.ctime())

# #Question 6.
# future = today + datetime.timedelta(days=10)
# print(future)
# past= today - datetime.timedelta(days=10)
# print(past)

# #Queston 7.
# print(sys.version)
# print(sys.platform)

import datetime
import calendar

day_name=datetime.date.today().weekday()
day_name=calendar.day_name[day_name]
print(day_name)











