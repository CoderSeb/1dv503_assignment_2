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
