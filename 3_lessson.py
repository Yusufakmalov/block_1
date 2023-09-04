#a = ["yusuf", "amal", "akmal", "akrom", "man"]
#rint(a[0:3:1])

#.append
#names = ['Sasha']
#names.append(['Pavel'])
#print(names)

#.insert
#names = ["Loki", "Spiderman"]
#names.insert(0, "THor")
#print(names)

#.extend
#names = ["liki", "Spiderman"]
#names.extend(["THor", 0, 23, "tanos"])
#print(names)

#names = ["Loki", "thor", "hulk"]
#names.clear()
#print(names)

#names = ["loki", "THor", "Hulk"]
#names.pop()
#print(names)

#names = ["loki", "THor", "Hulk"]
#names.remove("Hulk")
#print(names)


names = ['mirik', "Javlon", "Kamran"]
staroe_name = input("ccedi staroe name:")
new_name = input("Vvedi novoe name:")
name_index = names.index(staroe_name)
names[name_index] = new_name
print(names)
