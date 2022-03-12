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
    address = input("Enter the address (ex. 50187 Springs Terrace): ")
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


def show_manager_for_resident_name(my_cursor):
    first = input("Enter first name (ex. Neil): ")
    last = input("Enter last name (ex. Kilshaw): ")
    sql = (
        "SELECT CONCAT_WS(' ', managers.f_name, managers.l_name) as name, managers.phone, managers.email, p.address"
        " FROM managers"
        " JOIN properties p on managers.id = p.man_id"
        " WHERE p.id = (SELECT residents.prop_id"
        " FROM residents"
        " WHERE residents.f_name = '{0}' AND residents.l_name = '{1}');".format(
            first, last
        )
    )
    my_cursor.execute(sql)
    result = my_cursor.fetchall()
    if len(result) > 0:
        print("\nResponsible manager:\n----------------------")
        print(
            "{:<20} {:<15} {:<26} {}".format(
                "name", "phone", "email", "manager_on_address"
            )
        )
        for manager in result:
            print("{:<20} {:<15} {:<26} {}".format(*manager))
    else:
        print("No manager found...")


def list_managers_nr_properties(my_cursor):
    sql = """SELECT CONCAT_WS(' ', managers.f_name, managers.l_name) as name, COUNT(p.man_id) as number_of_properties, SUM(p.rent) as rent_income
            FROM managers
            LEFT JOIN properties p on managers.id = p.man_id
            GROUP BY name
            ORDER BY number_of_properties DESC;
            """
    my_cursor.execute(sql)
    result = my_cursor.fetchall()
    if len(result) > 0:
        print("\nManagers:\n----------------------")
        print("{:<20} {:<20} {}".format("name", "nr_of_properties", "rent_income"))
        for manager in result:
            print("{:<20} {:<20} {}".format(*manager))
    else:
        print("No manager found...")


def list_residents_on_address(my_cursor):
    address = input("Enter address (ex. 7265 Tennessee Drive): ")
    sql_1 = """SELECT address, postal, rent
                FROM properties
                WHERE address = '{}';""".format(
        address
    )
    my_cursor.execute(sql_1)
    prop = my_cursor.fetchone()
    sql_2 = """SELECT CONCAT_WS(' ', residents.f_name, residents.l_name) as name, email, phone
    FROM residents
    JOIN properties p on residents.prop_id = p.id
    WHERE p.address = '{}';""".format(
        address
    )
    my_cursor.execute(sql_2)
    result = my_cursor.fetchall()
    if len(result) > 0:
        print("\nResidents of {0}, {1} with monthly rent of {2}".format(*prop))
        print("-----------------------------------------------------")
        print("{:<26} {:<27} {}".format("name", "email", "phone"))
        for resident in result:
            print("{:<26} {:<27} {}".format(*resident))
