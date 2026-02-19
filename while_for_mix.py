# classname =1
# while classname<11:
#     print("class:", classname)
#     for i in range (1,11):
#         print(i, end=" ") 
#     print("\n attendence done")
#     classname +=1
# print("exit")


# import time

#     print("round:", round)
#     countdown = 3
#     while countdown>0:
#         print("countdown:",countdown)
#         countdown-=1
#         time.sleep(1)    
#     print('round completed')
#     print('next round!') 

# #atm withdrawl
# user = 1
# originalbalance={1:1000,2:5000,3:6000}
# while user<=3:
#     print("user:",user)
#     balance=originalbalance[user]
#     for i in range(1,4):
#         amount=int(input("enter your amount:"))
#         if amount<=balance:
#             balance+=amount
#             print("remaining balance:",balance)
#         # else:
#         #     print("insufficient balance")
#     print("user:",user,"transanction complete")
#     user+=1 


customer=1
while customer<=2:
    print("customer:",customer)
    total=0
    for i in range(1,3):
        amount=int(input("enter your amount:"))
        total=total+amount
        print("total bill:",total)
        print("next customer")
        customer+=1

# students =1

# while students<=4:
#     print("\nstudents:",students)
#     total_marks=0
#     for subject in range(1,6):
#        total=int(input('enter your marks:'))
#        total_marks+=total
#        average=total_marks/subject
#     print("total marks:",total_marks)
#     print("average:",average)
#     students+=1










    

            


    