
# print("hello,python learners!")

# name = "shejal"
# age = 18
# trade = "AIPA"
# print("my name is =",(name))
# print("my age is =",(age))
# print("my trade is =",(trade))

# f string

# print(f"my name is={name} and i am {age} years old.")
# a = 5
# b = 5
# print(f"the result of addition {a} + {b} is:",{a+b})
# print(f"the result of subtraction {a} - {b} is:",{a-b})
# print(f"the result of multiplication {a} * {b} is:",{a*b})
# print(f"the result of dividion {a} / {b} is:",{a/b})
# print(f"the result of exponentation {a} ** {b} is:",{a**b})
# print(f"the result of floor division {a} // {b} is:",{a//b})


# print(f"the result of {15}+{10} is: {15+10}")
# print(f"the result of {15}-{10} is: {15-10}")
# print(f"the result of {15}*{10} is: {15*10}")
# print(f"the result of {15}/{10} is: {15/10}")
# print(f"the result of {15}//{10} is: {15//10}")
# print(f"the result of {15}**{10} is: {15**10}")


#add the numbers.

# x = 5
# y = 5
# z = x+y
# print(sum)
# print("the sum is:",z)
# print("the sum of 5 and 5 is:",z)
# print("the product of 5 and 5 is:",z)
# print("5","+","5","=",5 + 5,sep=" ")
# print("4","*","4","=",4 * 4,sep="*")
# print("6","/","3","=",6 / 3,sep=" ")
# print("5 + 5 =", end=" ")
# print(5 + 5)
# print("6 - 3 =", end=" ")
# print(6 - 3)

# x = 20
# print(x)
# print("hello, world!")
# print("welcome to the python programming.")

# length = 10
# width = 5
# area = length * width
# print("the area of the rectangle is:",area)

# x = 10
# result = x * 2
# print("the result is:",result)

# x = 20
# z = x + 30
# print("the result is:",z)

# #printing multiple lines using one statement
# print("python is fun!\nlet's learn it step by step.\nkeep practing every day.")
# print("i am a confident girl.\ni can do everything.\ni want to become a successful business women.")

# print("the sum of 10 & 20 is:",10+20)
# print("the subtraction of of 20 & 30 is:",20-30)
# print("the multiplication of 10 & 2 is:",10*2)

# x=10
# y=5
# c=x+y
# print("the sum of",x,"and",y,"is =",c)
# print(f"the sum of {x} and {y} is = ",c)

# x = 5
# y = 10
# z = 2
# a = x+y+z
# b = x-y-z
# c = x*y*z
# print("the addition of",x,y,z,"is = ",a)
# print("the subtraction of",x,y,z,"is = ",b)
# print("the multiplication of",x,y,z,"is = ",c)

# print(f"the result of {x},{y},{z} is = {a}")
# print(f"the result of {x},{y},{z} is = {b}")
# print(f"the result of {x},{y},{z} is = {c}")

#operator in python

#arithmetic operator
# x = 10
# y = 5
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x**y)
# print(x//y)
# print(x % y)

#comperative operators
# x=10
# y=5
# print(x>y)
# print(x<y)
# print(x==y)
# print(x>=y)
# print(x!=y)
# print(x<=y)

# #asignment operators
# x = 5
# y = 10
# x+=y
# print(x)
# x-=y
# print(x)
# x*=y
# print(x)
# x/=y
# print(x)
# x**=y
# print(x)
# x//=y
# print(x)

# #flow control statements:
# weather = input("enter your weather=")
# if weather =="sunny":
#     print("go outside")
# elif weather =="rainy":
#     print("take umbrella.")
# elif weather =="breezy":
#     print("take jacket")
# else:
#     print("stay at home") 

# marks = int(input("enter your marks:"))
# if marks>=90:
#     print("A+")
# elif marks>=80:
#     print("B")
# elif marks>=70:
#     print("C")
# elif marks>=60:
#     print("D")
# else:
#     print("fail")

# balance = 1000
# withdrow = int(input("enter amount to withdraw:"))
# if withdrow<=balance:
#     print("transaction successful")
# else:
#     print("no amount")

# vehicle = input("enter vehicle:")
# if vehicle in ("xuv,defender,sedan,nano"):
#     print("it is a four wheel vehicle")
# elif vehicle in("bullet,apache,spender"):
#     print("it is a-2wheel vehicle ")
# else:
#     print("unknown vehicle")

#nested if.
# marks = int(input("enter your marks:"))
# if marks>=40:
#     if marks>=90:
#         print("A")
#     elif marks>=80:
#         print("B")
#     elif marks>=70:
#         print("C")
# else:
#     print("fail")                

#voting eligibility
# age = int(input("enter you age:"))
# citizenship = input("enter your citizenship:")
# if age >=18:
#     if citizenship=="indian":
#         print("you can vote")
#     else:
#         print("you are not indian citizen")
# else:
#     print("not eligible to vote")

#student grade
# marks = int(input("enter your marks:"))
# if marks>=40:
#     if marks>=90:
#         print("excellent")
#     elif marks>=75:
#         print("very good")
#     else:
#         print("good")
# else:
#     print("fail") 

#online shopping discount
# purchase_amount = int(input("enter the purchase_amount"))
# is_member = input("are you a mrmber?(yes/no):")
# if purchase_amount>1000:
#     if is_member=="yes":
#         print("20% discount applied")
#     else:
#         print("10% discount applied")
# else:
#     print("no discount avaible")

#exam result checker
# marks = int(input("enter your marks:"))
# if marks >=40:
#    attendance = float(input("enter your attendance:"))
#    if attendance >=75:
#        print("pass")
#    else:
#        print("pass but low attendance")
# else:
#     print("fail")

# #login system
# username = input("enter your username:")
# if username =="admin":
#     password = input("your password:")
#     if password =="1234":
#         print("login successful")
#     else:
#         print("incorrect password")
# else:
#     print("invalid username")

# #temperature check
# temp = float(input("enter the temperature:"))
# if temp>0:
#     if temp<20:
#         print("it's cool")
#     else:
#         print("it's warm")
# else:
#     print("it's freezing!")

# #userdefined error handling
# class nstiadmission(Exception):
#     pass
# try:
#     x=int(input("enter qualification="))
#     if x<12:
#       raise nstiadmission("not qualified")
#     else:
#        print("you are eligible for admission")
# except nstiadmission as shejal:
#    print("reasion:",shejal)

# class invailedadhar(Exception):
#    pass
# try:
#    adhar=input("enter you adhar no.=")
#    if len(adhar) !=12 or not adhar.isdigit():
#       raise invailedadhar("enter a vailed adhar no. with 12 digit=")
#    else:
#       print("adhar no. accepted")
# except invailedadhar as abc:
#    print("reasion",abc)

# def main():
#     try:
#         print("1. addition")
#         print("2. subtraction")
#         print("3. multiplication")
#         print("4. division")
#         choice= int(input("enter the choice(1/2/3/4):"))   #  create calculator. 
#         x=int(input("enter no. 1:"))
#         y=int(input("enter no. 2:"))
#         if choice==1:
#             result=x+y
#             print(result)
#         elif choice ==2:
#             result=x-y
#             print(result)
#         elif choice==3:
#             result=x*y
#             print(result)
#         elif choice==4:
#             if y!=0:
#                 return (x/y)
#         else:
#             print("can't be divide")
#     except ZeroDivisionError:
#         print("can't divided by 0")
#     except ValueError:
#         print("enter vailid number")
#     else:
#         print("number are :",x,y)
#     finally:
#         print("calculator created")

# if __name__=="__main__":
#     main()




# #practice

# try:
#    print("before error")  #predict the output
#    print(5/0)
# except:
#    print("something went wrong")

# try:
#    print("hello")     #find and correct the error 
# except:
#    print("error")

# try:
#    num=int("10a")     #predict the output
# except ValueError:
#    print("valueError occured")
# finally:
#    print("end of program")

# try:
#    a=[10,20,30]
#    print(a[3])
# except 









          






















