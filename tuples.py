my = (1, "Hello", [1, 2, "name"], (1, 4.12))
print(my[1])

toys = ("MIshka", "Ball", "goal", "bear")
tous2 = list(toys)
print(tous2)
print(type(tous2))

toys1 = ("MIshka", "Ball", "goal", "bear")
tous23 = tuple(toys1)
print(tous23)
print(type(tous23))


lang = ["English", "Python", "Russian", 4, 5,]
admin = input("ccedi  nazvanie:")
if admin in lang:
    print("i know english ")
elif admin in lang:
    print("I am creater of Python")
else:
    print('reapeat')
