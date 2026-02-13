# class police:
#     def work(self):
#         print("control law & order")
# class doctor:
#     def work(self):
#         print("treatment of patiants") 
# class teacher:
#     def work(self):
#         print("teach students")               
# a = [police(), doctor(), teacher()]
# for i in a:
#     i.work()

# class dog:
#     def sound(self):
#         return "bark"
# class cat:
#     def sound(self):
#         return "meow"
# for animal in (dog(),cat()):
#     print(animal.sound())


# class animal:
#     def sound(self):
#         return "some sound"
    
# class dog(animal):
#     def sound(self):
#         return "bark"
# d=dog()
# print(d.sound())

# class car:
#     def speed(self):
#         print("car speed is 120km/h")
# class bike:
#     def speed(self):
#         print("bike speed is 80 km/h")
# for i in(car(),bike()):
#     i.speed()

# class dog:
#     def sound(self):
#         return "bark"
# class cat:
#     def sound(self):
#         return "meow"
# class cow:
#     def sound(self):
#         return "moo"
# d=dog()
# c=cat()
# c2=cow()
# print(d.sound())
# print(c.sound())
# print(c2.sound())

# #method overriding example
# class person:
#     def work(self):
#         print("person works")
# class student(person):
#     def work(self):
#         print("student studies")
# p = person()
# s = student()
# p.work()
# s.work()

#len method
s = "hello"
lst = [10,20,30,40]
d = {"a": 1, "b": 2, "c": 3}
print(len(s))
print(len(lst))
print(len(d))