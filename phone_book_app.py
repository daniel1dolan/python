#phone book app
def menu():
    print("Electric Phone Book")
    print("=" * 21)
    print("1. Look up an entry")
    print("2. Set an entry")
    print("3. Delete an entry")
    print("4. List all entries")
    print("5. Quit")

phone_book = {}
user_input = "0"
menu()
while user_input != "5": 
    user_input = input("What would you like to do (1-5)?")
    if user_input == "1":
        name_wanted = input("Name: ")
        if name_wanted not in phone_book:
            print("Entry not found. Try set an entry.")
            menu()
        else:
            print(f"Found entry for {name_wanted}: {phone_book[name_wanted]}")
            menu()
    elif user_input == "2":
        name_addition = input("Name: ")
        addition_number = input("Phone Number: ")
        phone_book[name_addition] = addition_number
        print(f"Entry stored for {name_addition}.")
        menu()
    elif user_input == "3":
        del_name = input("Name: ")
        if del_name not in phone_book:
            print("Entry not found. Try set an entry.")
            menu()
        else:
            del phone_book[del_name]
            print(f"Deleted entry for {del_name}")
            menu()
    elif user_input == "4":
        item_pairs = phone_book.items()
        for key, value in item_pairs:
            print(f"Found entry for {key}: {value}")
        menu()
    else: 
        print("Please enter an option (1-5).")
        menu()
print("Bye. Have a wonderful day.")




    