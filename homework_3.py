tabl_1 = ["1*1=1", "2*1=2", "3*1=3", "4*1=4", "5*1=5", "6*1=6", "7*1=7", "8*1=8", "9*1=9", "10*1=10"]
tabl_2 = ["1*2=2", "2*2=4", "3*2=6", "4*2=8", "5*2=10", "6*2=12", "7*2=14", "8*2=16", "9*2=18", "10*2=20"]
tabl_3 = ["1*3=3", "2*3=6", "3*3=9", "4*3=12", "5*3=15", "6*3=18", "7*3=21", "8*3=24", "9*3=27", "10*3=30"]
tabl_4 = ["1*4=4", "2*4=8", "3*4=12", "4*4=16", "5*4=20", "6*4=24", "7*4=28", "8*4=36", "9*4=36", "10*4=40"]
tabl_5 = ["1*5=5", "2*5=10", "3*5=15", "4*5=20", "5*5=25", "6*5=30", "7*5=35", "8*5=40", "9*5=45", "10*5=50"]
tabl_6 = ["1*6=6", "2*6=12", "3*6=18", "4*6=24", "5*6=30", "6*6=36", "7*6=42", "8*6=48", "9*6=546", "10*6=60"]
tabl_7 = ["1*7=7", "2*7=14", "3*7=21", "4*7=28", "5*7=35", "6*7=42", "7*7=49", "7*8=56", "9*7=63", "10*7=70"]
tabl_8 = ["1*8=8", "2*8=16", "3*8=24", "4*8=32", "5*8=40", "6*8=48", "7*8=56", "8*8=64", "9*8=72", "10*8=80"]
tabl_9 = ["1*9=1", "2*9=18", "3*9=27", "4*9=36", "5*9=45", "6*9=36", "7*9=63", "8*9=72", "9*9=81", "10*9=90"]
tabl_10 = ["1*10=1", "2*10=2", "3*10=3", "4*10=4", "5*10=50", "6*10=6", "7*10=7", "8*10=8", "9*10=9", "10*10=100"]
name = input("Enter number:")
if name == "1":
    for i in tabl_1:
        print(i)
if name == "2":
    for i in tabl_2:
        print(i)
if name == "3":
    for i in tabl_3:
        print(i)
if name == "4":
    for i in tabl_4:
        print(i)
if name == "5":
    for i in tabl_5:
        print(i)
if name == "6":
    for i in tabl_6:
        print(i)
if name == "7":
    for i in tabl_7:
        print(i)
if name == "8":
    for i in tabl_8:
        print(i)
if name == "9":
    for i in tabl_9:
        print(i)
if name == "10":
    for i in tabl_10:
        print(i)
else:
    print("Try again")

second_ex_homework = 4


while True:
    name = input("Enter word palindrome: ")



    if name == name[::-1]:
        print(f"{name} is palindrome")
    elif name != name[::-1]:
        print(f"{name} is not palindrome")
    else:
        print("Try again")











