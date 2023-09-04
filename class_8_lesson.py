# class User:
#     name = "Jordan"
#     print(name)
# class Car:
#     tupe = 'Bugatti'
#     color = "white"
#     max_speed = 300
# class Person:
#     name = 'Jordan'
#     age = 23
#     job = 'programmer'
#     print()
#
# class User():
#     name = 'Javlon'
# user1 = User()
# print(user1)
#
# class Nothing():
#     pass
#
# class Car:
#     def __init__(self, model, color, year):
#         self.model = model
#         self.color = color
#         self.year = year
# gentra = Car("chevrolet",color= "black",year= 2023 )
# cobalt = Car("Ravon", "white", 2090)
# print(gentra.model)
# print(cobalt.year)


#class Comment():
#   def __init__(self, username, text, likes = 0):
#       self.username = username
#      self.text = text
#        self.likes = likes
#user99 = Comment('Javik','god')
#print(user99.text)

#





class User:
    def __init__(self, name, mail, age, number ):
       self.name = name
        self.mail = mail
        self.age = age
        self.number = number
        def change_username(self, cname):
            self.name = cname
        def change_number(self, cnum):
            self.number = cnum
        def change_mail(self, cmail):
            self.mail = cmail

users = User("Islom", "makmalhonov@gmail.com", 23, 998998300427)
print(User)
