import mysql.connector as msql
from mysql.connector import errorcode

from scripts.database import create_database
from scripts.populate import add_content
from scripts.tables import create_tables
from scripts.view import handle_menu

# Settings
DB_HOST = "localhost"
DB_USERNAME = "root"
DB_PASSWORD = "root"
DB_PORT = 3306
DB_NAME = "property_manager"

# Set to true to enable full error messages.
DEBUG_MODE = False


try:
    # Connecting to DB server
    connection = msql.connect(
        host=DB_HOST, user=DB_USERNAME, password=DB_PASSWORD, port=DB_PORT
    )
    # Checking if server connection is established.
    if connection.is_connected():
        cursor = connection.cursor()
        try:
            # Attempting to use the stated database.
            cursor.execute("USE {}".format(DB_NAME))
        except msql.Error as err:
            print("Database {} does not exist".format(DB_NAME))
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                create_database(cursor, DB_NAME)
                connection.database = DB_NAME
                print("Database {} created successfully.".format(DB_NAME))
                # Creating tables and inserting values.
                create_tables(cursor)
                add_content(cursor, DEBUG_MODE)
                # Committing the changes.
                connection.commit()
            else:
                print(
                    "Something went wrong when creating the database {}".format(
                        DB_NAME
                    )
                )
                exit(1)
        # Showing menu
        handle_menu(cursor, DEBUG_MODE)
except Exception as e:
    if DEBUG_MODE:
        print(e)
    cursor.close()
    connection.close()
    exit(1)
