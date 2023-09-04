class User:
    def __init__(self, name, mail, age, number ):
       self.name = name
       self.mail = mail
       self.age = age
       self.number = number

    def change(self, n):
        self.name = n
    def chang(self, m):
        self.mail = m
    def chan(self, a):
        self.age = a
    def cha(self, num):
        self.number = num

users = User("Islom", "makmalhonov@gmail.com", 23, 998998300427)
print(users)



class Sport:
    def __init__(self, type, rules = 0):
        self.type = type
        self.rules = rules

        def rules(self, rule):
            self.rules = rule
        def type(self, types):
            self.type = types

sport = Sport(type= "Judo", rules= "do not touch legs")
print(sport)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

white = Person("yusuf", 14)
Black = Person("Akmal", 17)
niger = Person("Ayub", 14)
machine = Person("amikoooo", 15)
print(white )
print(Black)
print(niger)
print(machine)





