def show_managers(my_cursor):
    sql = """SELECT * FROM managers"""
    try:
        my_cursor.execute(sql)
        result = my_cursor.fetchall()
        print(
            "\n{:<5} {:<12} {:<12} {:<28} {}".format(
                "id", "firstname", "lastname", "email", "phone"
            )
        )
        for manager in result:
            print("{:<5} {:<12} {:<12} {:<28} {}".format(*manager))
    except Exception as error:
        print(error)


def show_manager_for_address(my_cursor):
    address = input("Enter the address: ")
    sql = (
        "SELECT phone as manager_phone, CONCAT_WS(' ', f_name, l_name) as manager_name, email, address"
        " FROM managers, properties"
        " WHERE managers.id = properties.man_id"
        " AND address = '{}';".format(address)
    )
    my_cursor.execute(sql)
    result = my_cursor.fetchone()
    if result != None:
        print(
            "\nResponsible manager for {3}\nPhone number: {0}\nEmail: {2}\nName: {1}".format(
                *result
            )
        )
    else:
        print("No manager found for that address...")
