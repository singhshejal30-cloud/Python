# class student:
#     def __init__(self,name,trade):
#         self.name = name
#         self.trade = trade
# s1 = student("shejal","aipa")
# s2 = student("akriti","csa")
# print(s1.name,s1.trade)
# print(s2.name,s2.trade)

# class movies:
#     def __init__(self,name,type):
#         self.name = name
#         self.type = type
# m1 = movies("the godfather","hollywood")
# m2 = movies("dangal","bollywood")
# print(m1.name,m1.type)
# print(m2.name,m2.type)

# class bankaccount:
#     def __init__(self,balance):
#         self.balance = balance
#     def add(self,add):
#         self.balance+=add
#     def withdraw(self,amt):
#         self.balance-=amt
#     def finalamount(self):
#         return self.balance
# acc = bankaccount(100)
# acc.add(50)
# acc.withdraw(100)
# print(acc.finalamount())


# class bankaccount:
#     def __init__(self,balance):
#         self.balance = balance
#     def add(self,add):
#         self.balance+=add
#     def withdraw(self,amt):
#         self.balance-=amt
#     def finalamount(self):
#         return self.balance
# initial = int(input("enter your amount:"))
# deposit = int(input("enter your depositamount "))
# credit = int(input("enter your creditamount:")) 
# acc = bankaccount(100)
# acc.add(50)
# acc.withdraw(100)
# print(acc.finalamount())

# #PRACTICE
# #student class
# class student:
#     def __init__(self,name,roll,marks):
#         self.name=name
#         self.roll=roll
#         self.marks=marks
# s= student("sheju","1","70%")
# print(s.name,s.roll,s.marks)

# class car:
#     def __init__(self,company,model,price):
#         self.company=company
#         self.model=model
#         self.price=price
#     def discount(self):
#         self.price=self.price-5000        
# c1=car("tata","punch",600000)
# c2=car("hyundai","i20",750000)
# c1.discount()
# c2.discount()
# print("car 1:",c1.company,c1.model,"final pricem =",c1.price)
# print("car 2:",c2.company,c2.model,"final pricem =",c2.price)

#mobile
class mobile:
    def __init__(self,brand,ram,storage):
        self.brand=brand
        self.ram=ram
        self.storage=storage
    def full_spec(self):
        print('brand:',self.brand)
        print("ram:",self.ram)
        print("storage:",self.storage)
m1 = mobile("samsung","8GB","128GB")
m2 = mobile("redmi","6GB","64GB")

m1.full_spec()
print()
m2.full_spec()



    




