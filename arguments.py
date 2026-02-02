# def list(*args):
#     print("list of students:",end="")
#     for i in args:
#         print(i)
# (list("aipa","csa","em"))

# def abc(*args):
#     print("added numbers are:",end="")
#     sum = 0
#     for i in args:
#         sum+=i
#     return sum   
# print(abc(1,2,3,4,5))

# def marks(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
# num = input("enter marks:")
# num_list = [int(x) for x in 
#             num.split()]
# print(marks(*num_list))

# def largest_num(*args):
#     print("largest_num is:",max(args))
# largest_num(20,30,40,50)

# def average_num(*args):
#     avg = sum(args)/ len(args)
#     print("average is:",avg)
# nums = list(map(int, input("enter numbers sepersted by space:").split()))
# average_num(*nums)

# def student_info(**kwargs):
#     print("student details:")
#     for key, value in kwargs.items():
#         print(key , value)
# student_info(name ="shejal", age=20, course="python", city="prayagraj", phone_no="xyz")


# def mix (nsti, opening = 1992,*trade, **detials):
#     print(nsti)
#     print(opening)
#     if trade:
#         print("trade in nsti:",trade)
#     if detials:
#         for key,value in detials.items():    
#          print(key,value)
# mix("allahabad",2007,"aipa","csa",phone_no=7618957947,pincode=212110,email_id="singhshejal30@gmail.com")

# def student_report(name,*subjects,**marks):
#    print(name)
#    if subjects:
#       print("subjects:",subjects)
#    if marks:
#       for key,value in marks.items():
#          print(key,value)
# student_report("shejal","hindi","english","computer","arts",hindi=50,english=70,computer=90,arts=100)

# def travel_booking(destination,day=1,*activities,**hotel_price):
#    print(destination)
#    print(day)
#    if activities:
#       print("activities:",activities)
#    if hotel_price:
#       for key,value in hotel_price.items():
#          print(key,value)
# travel_booking("switzerland",5,"sketing","shopping","travelling",A=5000,Z=4000,B=7000)
# try:
#   x=5
#   y=int(input("enter your="))
#   print(x/y)
# except ZeroDivisionError:
#   print("no can't be division by 0")


# try:
#   a=5
#   b=int(input("enter your number="))
#   print(a/b)
# except ZeroDivisionError:
#   print("no can't divided by 0")  

#Value error
try:
    x=int(input("enter value="))
    print(10/x)
except ValueError:
    print("can't divide by string")
else:
    print("the input was",x)
finally:
    print("all code done")        

 






    
    
    

