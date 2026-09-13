
def add_contact(contact):
    name=input("enter your name to be added:")
    phone=int(input("enter contact number:"))
    contact[name]=phone
    print("name added successfully!")

def search_contact(contact):
    name=input("enter the name :")
    if name in contact:
        contact[name]
        print("contact found successfully")
    else:
        print("contact not found")

def update_contact(contact):
    name=input("enter the name :")
    if name in contact:

        new_phone=int(input("enter your updated phone"))
        contact[name] = new_phone
        print("phone updated successfully!")
    else:
        print("contact not found")

def delelte_contact(contact):
    name=input("enter the name :")
    if name in contact:
        del contact[name]
        print("contact deleted successfully!")
    else:
        print("contact not found")

contact={
    "shivam":8529637415,
    "sohan":85295632741,
    "adarsh":85274196363,
}

while True:
    try:
        print("\n contact book ")
        print("1.add contact")
        print("2.search contact")
        print("3.updtae contact")
        print("4.delete contact")
        print("5.exit")

        choice = int(input("enter your choices:"))
        if choice==1:
            add_contact(contact)
        elif choice==2:
            search_contact(contact)
        elif choice==3:
            update_contact(contact)
        elif choice==4:
            delelte_contact(contact)
        elif choice==5:
            print("thank you")
            break
        else:
            raise ValueError("invalid choice")
    except ValueError as e:
        print(e)