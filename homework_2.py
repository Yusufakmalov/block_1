contact_list = ["Мама", "Папа", "Брат"]
user = input("Enter action of (append, change  or delete) to your contact_list:")
user_1 = input("Enter name of contact: ")

if user == "append":
  print("just a minute")
  contact_list.append(user_1)
elif user == "extend":
  print("just a moment")
  contact_list.extend(user_1)
elif user == "insert":
  print ("just a second")
  contact_list.insert(-1, user_1)
elif user == "pop":
  print("just a moment")
  contact_list.pop(user_1)
elif user == "remove":
  print("just a moment")
  contact_list.remove(user_1)
elif user == "clear":
  print("Ok!")
  contact_list.clear()
elif user == "change":
    a = input("Please Enter what you want to change")
    b = input("Please enter new name:")
    c = contact_list.index(a)
    contact_list[c] = b

else:
  print("Error, please enter action or name correctly)")

print(contact_list)
