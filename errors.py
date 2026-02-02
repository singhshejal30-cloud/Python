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