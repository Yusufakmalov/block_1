a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = (input("enter  math operator like (+, -, *, /):"))


if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/":
    print(a / b)
elif c == "**":
    print(a ** b)
elif c == "//":
    print(a // b)

else:
    print("enter againly:")
