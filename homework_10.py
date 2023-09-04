class Animal:
    def make_sound(self,s ):
        print(s)


class Cat(Animal):
    def __init__(self, color, name, type):
        super(Cat, self).__init__()
        self.color = color
        self.name = name
        self.type = type
ucat = Cat("Black", "shustriy", "Gendos")
print(ucat.make_sound("shakabum, myauuuuuuuuuuuuuuuuuuuu"))
class Dog(Animal):
    def __init__(self, color, height, type):
        super(Dog, self).__init__()
        self.color = color
        self.height = height
        self.type = type
udog = Dog("white", 1.70, "BUldog")
print(udog.make_sound("Gav Gav , Fuck cats!"))
class Cow(Animal):
    def __init__(self, kilo, type):
        super(Cow, self).__init__()
        self.kilo = kilo
        self.type = type

ucow = Cow(500, "debiloyid")
print(ucow.make_sound("siuuuuu, Muuuuuuuuuu!"))
print(ucow.type)
class Parent():
    def __init__(self, respect, level, height):
        self.respect = respect
        self.level = level
        self.height = height
uparent = Parent(100, 101, 190)
print(uparent.height)
class inheritance_of_Parent(Parent):
    def __init__(self, respect, level, height, name):
        super().__init__(respect, level, height)
        self.name = name

uinheritance_of_Parent = inheritance_of_Parent(50, 40, 1.69, "MOl paras")
print(uinheritance_of_Parent.height)

class Player():
    def __init__(self, speed, ball_control, innings, pas):
        self.speed = speed
        self.ball_control = ball_control
        self.innings = innings
        self.pas = pas

Messi = Player(100, 101, 97, 99)
CR7 = Player(100, 100, 96, 87)
Maguire = Player(103, 999, 1999, 0)
Ter_stegen = Player("Fuck Muguire", "Fuck Muguire", "Fuck Muguire", "Fuck Muguire" )
class Attack(Player):
    def __init__(self, speed, ball_control, innings, pas, fints):
        super(Attack, self).__init__(speed, ball_control, innings, pas)
        self.fints = fints
    def fintes(self, f):
        print(f)

Neymar = Attack(100, 101, 100, 100, 111)
print(Neymar.fintes("The best fint is Rabona, NJ is here!"))

class Midfielder(Player):
    def __init__(self, speed, ball_control, innings, pas, style):
        super(Midfielder, self).__init__(speed, ball_control, innings, pas)
        self.style = style

Roonie = Midfielder(99, 98, 100, 97, 89)
print("Roonie's style level - ", Roonie.style)
class Defender(Player):
    def __init__(self, speed, ball_control, innings, pas, power):
        super(Defender, self).__init__(speed, ball_control, innings, pas)
        self.power = power
Ramos = Defender(96, 90, 96, 97, 100)
print("Ramos's power - ", Ramos.power)

class Goalkeeper(Player):
    def __init__(self, speed, ball_control, innings, pas, safes):
        super(Goalkeeper, self).__init__(speed, ball_control, innings, pas)
        self.safes = safes
    def safe(self, s):
        print(s)

De_Gea = Goalkeeper(99, 97, 100, 100, 101)
print("De gea's safes level - ", De_Gea.safe("Fuck Mugire"))
print("De gea's safes real level - ", De_Gea.safes)
