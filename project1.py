contacts = {}

while True:
    print("\n1.Add 2.View 3.Search 4.Delete 5.Exit")
    ch = input("Choice: ")
    if ch == '1':
        name = input("Name: ")
        num = input("Number: ")
        contacts[name] = num
    elif ch == '2':
        print(contacts)
    elif ch == '3':
        name = input("Search Name: ")
        print(contacts.get(name, "Not Found"))
    elif ch == '4':
        name = input("Delete Name: ")
        contacts.pop(name, None)
    elif ch == '5':
        break