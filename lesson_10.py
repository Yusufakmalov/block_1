class Animal:
    def make_sound(self,s):
        print(s)


class Horse(Animal):
    pass
user = Horse()
print(user.make_sound("shakabum!"))

class Parent():
    pass
class Child(Parent):
    pass
class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

class SuperCar(Car):
    def __init__(self, model, color, year, sponsor):
        super().__init__(model, color, year)
        self.sponsor = sponsor


class MyClass:
    @classmethod
    def class_info(cls):
        return f"this is  {cls.__name__}"
print(MyClass.class_info())


class MyClass:
    def __init__(self, value):
        self.value = value


    @classmethod
    def from_string(cls, string):
        return cls(int(string))

my_obj = MyClass.from_string("10")
print(type(my_obj.value))
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

rectangle = Rectangle(4,5)
print(rectangle.area)

rectangle.height = 100
rectangle.width = 100
print(rectangle.area)

class Worker:
    def __init__(self, name, stuff):
        self.name = name
        self.stuff = stuff



class Worker():
    def __init__(self,name,position):
        self.name = name
        self.position = position

class HR(Worker):
    def __init__(self,name,position,password):
        super().__init__(name,position)
        self.password = password
    def show_position(self,worker_name):
        return worker_name.position


jordan = Worker('Jordan','Junior')
pavel = HR('Pavel','HR',111)
print(pavel.show_position(jordan))
