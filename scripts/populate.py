from scripts.fileread import managers_tuples, properties_tuples, residents_tuples


def add_managers(my_cursor, DEBUG_MODE):
    for item in managers_tuples:
        sql = (
            "INSERT INTO managers "
            "(id, f_name, l_name, email, phone) "
            "VALUES(%s, %s, %s, %s, %s)"
        )
        try:
            my_cursor.execute(sql, item)
        except Exception as error:
            if DEBUG_MODE:
                print(error)
            pass


def add_properties(my_cursor, DEBUG_MODE):
    for item in properties_tuples:
        sql = (
            "INSERT INTO properties "
            "(id, address, postal, rent, man_id) "
            "VALUES(%s, %s, %s, %s, %s)"
        )
        try:
            my_cursor.execute(sql, item)
        except Exception as error:
            if DEBUG_MODE:
                print(error)
            pass


def add_residents(my_cursor, DEBUG_MODE):
    for item in residents_tuples:
        sql = (
            "INSERT INTO residents "
            "(id, f_name, l_name, email, phone, prop_id) "
            "VALUES(%s, %s, %s, %s, %s, %s)"
        )
        try:
            my_cursor.execute(sql, item)
        except Exception as error:
            if DEBUG_MODE:
                print(error)
            pass


def add_content(my_cursor, DEBUG_MODE):
    add_managers(my_cursor, DEBUG_MODE)
    print("Managers are added..")
    add_properties(my_cursor, DEBUG_MODE)
    print("Properties are added..")
    add_residents(my_cursor, DEBUG_MODE)
    print("Residents are added..")
