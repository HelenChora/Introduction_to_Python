contacts={}

while True:
    print("1 add, 2 search, 3 list, 0 quit")
    choice= input("Choose an option:")

    if choice == "1":
        name=input("Name:")
        phone=input("Phone:")

        if name not in contacts:
            contacts[name]=[]

        contacts[name].append(phone)

    elif choice == "2":
        name= input("Search name:")
        print(contacts.get(name,"Contact not found"))

    elif choice == "3":
        for name in sorted(contacts):
            print(name, contacts[name])

    elif choice =="0":
        break

