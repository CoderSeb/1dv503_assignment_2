def show_menu():
    print("\n1 - Option 1")
    print("2 - Option 2")
    print("3 - Option 3")
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
            print("Not implemented")
            input("\nPress any key to return to the menu... ")
        elif option == 2:
            print("Not implemented")
            input("\nPress any key to return to the menu... ")
        elif option == 3:
            print("Not implemented")
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
