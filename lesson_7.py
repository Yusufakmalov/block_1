contact = []

def append():
    name = input("Enter name:")
    if name in contact:
        print("name is there")
    else:
        contact.append(name)
        print(contact)
        print(f"{name} append in list")

def delete(names = input("Enter name that you want:")):
    if names in contact:
        contact.remove(names)
        print(f"{names} ucolen")
        print(contact)
    else:
        print("that name  is not in  contacts")
def change():
        nama = input("vvedi rho you want:")
        if nama in contact:
            new_nama = input("Enter new noma:")
            contact[contact.index(nama)] = new_nama
            print(f"{nama} changed in {new_nama}")
            print(contact)
while True:
    admin = int(input("vvedi voy vibor, 1- dobavit, 3 - udalit, 3 - zamena"))
    if admin == 1:
        append()
    elif admin == 2:
        delete()
    elif admin == 3:
        pass
    else:
        print("Check danniye")
