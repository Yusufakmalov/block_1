list_of_students = {"8V": {"Teacher": {"Kiril"}}}
los = list_of_students

def append_c_s_g():
    s = (input("Enter name of st:"))
    s_1 = input("Enter class of st:")
    s_2 = input("Enter subjects of st:")
    s_3 = input("Enter grade of this subjects:")
    los[s_1] = {"Students": {s: {s_2: s_3}}}
    print(los)
    print(f"{s},{s_2},{s_3} was dobavlen")
def append_t():
    t = input("Enter name of teach:")
    t_2 = input("Enter class of teach:")
    los[t_2] = {"Teacher": {t}}
    print(los)
    print(f"{t} was dobavlen")
def delete_s():
    d_s = input("Enter name of st:")
    if d_s in los:
        los.pop(d_s)
        print(los)
        print(f"{d_s} was udalen")
    else:
        print(f"{d_s} is not in los")
def delete_t():
    d_t = input("Enter name:")
    if d_t in los:
        los.pop(d_t)
        print(los)
        print(f"{d_t} was udalen")
    else:
        print(f"{d_t} is not in los")
def delete_g():
    d_g = input("Enter name:")
    if d_g in los:
        los.pop(d_g)
    print(los)
    print(f"{d_g} was udalen")
def create():
    cr = input("Enter class:")
    cri = input("Enter st")
    los[cr] = {"Students": {cri}}
    print(los)
    print(f"Class {cr}  was created")
def change_t():
    ch = input("Enter name of past teach:")
    ch_1 = input("Enter name of new teach:")
    if ch in los:
        c = los.index[ch]
        los[ch_1] = c
        print(los)
        print(f"{ch} was changed to {ch_1}")
    else:
        print("Error")
def put_g():
    p_1 = input("enter name of boy:")
    p_3 = input("enter sub :")
    p_2 = input("enter grade:")
    p = input("enter class of boy:")
    los[p] = {p_1: {p_3: {p_2}}}
    print(f"{p_2} for {p_1} was put")
def change_g():
    g = input("Enter past g:")
    g_1 = input("Enter new g:")
    if g in los:
        g_2 = los.index[g]
        los[g_1] = g_2
while True:
    name = input("Enter what do you want to do f/e(dobavit s/t, delete s/t or grade, create, change t, "
"put grades, change grades,: ")
    if name == "dobavit s":
        append_c_s_g()
    elif name == "dobavit t":
        append_t()
    elif name == "delete s":
        delete_s()
    elif name == "delete t":
        delete_t()
    elif name == "delete grades":
        delete_g()
    elif name == "create":
        create()
    elif name == "change t":
        change_t()
    elif name == "put grades":
        pass
    elif name == "change grades":
        pass
    else:
        print("Try again")

        print("Second homework")
summa = lambda a, b: a + b
print(summa(5, 8))
name = int(input("Enter  number:"))
names = int(input("enter second nmb:"))
sum = lambda n, ns: (n + ns)
print(sum(name, names))
