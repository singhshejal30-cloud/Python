# #distionary

# students = {"name":"shejal","age":18, "trade":"aipa"}   #syntex
# print(students["age"])
# print(students["name"])

# students["marks"]=90
# students["address"]="kunda"
# print(students)

# #removing from dictionary

# students.pop("age")
# print(students)

# # checking key.

# print("phoneNo." in students)
# print("name" in students)

# #itrete over dictionary
# for key ,value in students.items():
#     if key== "trade":
#         continue
#     print(key,":",value)

# #merging dictionary

# x= {"name":"shiya","age":"15",}
# y= {"trade":"csa","address":"kunda"}
# print(x['age'])
# x.update(y)
# print(x)

# #nested dictionary

students={
    "AIPA":{"name":"Shailesh","age":20,"Trade":"AIPA","Address":"Teliyarganj"},
    "COPA":{"name":"Raj","age":20,"Trade":"COPA","Address":"Teliyarganj"},
    "EM":{"name":"Yash","age":20,"Trade":"EM","Address":"Teliyarganj"}
}

# print(students)

 #access particuler data
# print(students["COPA"]["Address"])

#  #copy distionary
# students2=students.copy()
# print(students2)

# #clear dictionary
# students.clear()
# print(students)

#question practice provided by sir......

# #creating a distionary
# student = {"name":"shejal","age":18,"grade":"A"}
# print(student)

# #accessing values(print only name and grade)
# student = {"name":"shejal","age":18,"grade":"A"}
# print(student["name"])
# print(student["grade"])

# #adding a new key-value pair
# student = {"name":"shejal","age":18,"grade":"A"}
# student["course"] = "python"
# print(student)

# #removing a key using pop()
# student = {"name":"shejal","age":18,"grade":"A"}
# student.pop('age')
# print(student)

# #checking key membership
# student = {"name":"shejal","age":18,"grade":"A"}
# print("grade" in student)

# #iterating over a distionary
# student = {"name":"shejal","age":18,"grade":"A"}
# for key, value in student.items():
#     if key== "grade":
#         continue
#     print(key,":",value)

# #using a get() method
# student = {"name":"shejal","age":18,"grade":"A"}


#data structure

# name = ["ram","riya","rohit","raghav","shree","gungun","arpit"]
# trade = ("CTS-AIPA")
# subject = {"maths","computer","english","hindi","science"}
# marks = {
#     "ram":{80,90,50,60,79},
#     "riya":{50,60,70,80,90},
#     "rohit":{70,60,70,80,60},
#     "raghav":{50,40,40,30,60},
#     "shree":{50,70,50,70,60},
#     "gungun":{70,50,40,50,70},
#     "arpit":{70,40,30,80,60},
# }

# print(name)
# print(trade)
# print(subject)
# print(marks["gungun"])

# print("maths" in subject)

# name.append("shejal")

# name.insert(1,"arkriti")
# print(name)

# name.remove("raghav")
# print(name)

# marks["shejal"]=[40,50,60,70,80]
# print(marks)

#nested method

# name = ["ram","riya","rohit","raghav","shree","gungun","arpit"]
# trade = ("CTS-AIPA")
# subject = {"maths","computer","english","hindi","science"}
# marks = {
#     "ram":{"maths":70,"computer":80,"english":50,"hindi":30,"science":20},
#     "riya":{"maths":50,"computer":70,"english":90,"hindi":70,"science":50},
#     "rohit":{"maths":30,"computer":90,"english":40,"hindi":80,"science":90},
#     "raghav":{"maths":40,"computer":70,"english":60,"hindi":50,"science":60},
#     "shree":{"maths":60,"computer":40,"english":30,"hindi":90,"science":50},
#     "gungun":{"maths":90,"computer":60,"english":40,"hindi":90,"science":70},
#     "arpit":{"maths":20,"computer":80,"english":50,"hindi":90,"science":40},
# }
# print(marks["raghav"]["computer"])


#practice

# book_name = ["A Tale of Two Cities","Anna karenina","The Catcher in the rye"]
# country = ("INDIA")
# author = {"Charles dickens","leo tolstoy","j.dsalinger"}
# year = {
#     "A Tale of Two Cities":{"charles dickens":1859},
#     "Anna karenina":{"leo tolstoy":1877},
#     "The Catcher in the rye":{"j.dsalinger":1899},
# }
# print(country)
# print(author)
# print(year)


    
