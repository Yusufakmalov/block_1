korzzina = {}
while True:
    admin = input("vvedi chto hocheesh:")
    if admin == "product":
        print(korzzina)
    elif admin == "kupit":
        product = input("vvedi product:")
        count = int(input("vvedi kolichestvo:"))
        korzzina[product] = count
        print(korzzina)
    elif admin == "dobavit product":
        production = input("vvedi chto hochesh dobavit:")
        counts = input("vvedi kolichestvo")
        korzzina[production] = counts
        print(korzzina)
    elif admin == "keys" or "value":
        keys = input("vvedite keys:")
        value = input("vvedite value:")
        korzzina[keys] = value
        print(korzzina)
    elif admin == "items":
        keys_value = input("Vvedite key and value:")
        korzzina.items(keys_value)
        print(korzzina)
    elif admin == "clear":
        print(korzzina.clear())
    elif admin == "delete el":
        delete = input("vvedi el from korzzina:")
        print(korzzina.pop(delete))
    elif admin == "popitem":
        print(korzzina.popitem())

    else:
        print("prover dannie ERROR:")
