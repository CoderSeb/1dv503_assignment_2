from mysql.connector import errorcode


def create_database(my_cursor, DB_NAME):
    # Creating database with the stated DB_NAME
    try:
        my_cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME)
        )
    except errorcode as error:
        print("Failed to create database {}".format(error))
        exit(1)
