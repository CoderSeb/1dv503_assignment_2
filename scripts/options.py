from scripts.queries import *


def show_menu():
    print("\n1 - Show all managers")
    print("2 - Find responsible manager for an address")
    print("3 - Find responsible manager by resident name")
    print("4 - Option 4")
    print("5 - Option 5")
    print("0 - Exit")


def handle_menu(my_cursor, DEBUG_MODE):
    while True:
        show_menu()
        option = ""
        try:
            option = int(input("\nEnter choice: "))
        except Exception as error:
            if DEBUG_MODE:
                print(error)
            print("\nInvalid input...")
        if option == 1:
            show_managers(my_cursor)
            input("\nPress any key to return to the menu... ")
        elif option == 2:
            show_manager_for_address(my_cursor)
            input("\nPress any key to return to the menu... ")
        elif option == 3:
            show_manager_for_resident_name(my_cursor)
            input("\nPress any key to return to the menu... ")
        elif option == 4:
            print("Not implemented")
            input("\nPress any key to return to the menu... ")
        elif option == 5:
            print("Not implemented")
            input("\nPress any key to return to the menu... ")
        else:
            print("\nBye!")
            exit(1)
