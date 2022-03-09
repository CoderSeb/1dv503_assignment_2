TABLES = {
    "managers": (
        "CREATE TABLE `managers`("
        " `id` int(20) NOT NULL,"
        " `f_name` varchar(100) NOT NULL,"
        " `l_name` varchar(100) NOT NULL,"
        " `email` nvarchar(100) NOT NULL,"
        " `phone` varchar(100) NULL,"
        " PRIMARY KEY (id))"
    ),
    "properties": (
        "CREATE TABLE `properties`("
        " `id` int(20) NOT NULL,"
        " `address` varchar(255) NOT NULL,"
        " `postal` varchar(150) NOT NULL,"
        " `rent` int(50) NOT NULL,"
        " `man_id` int(20) NULL,"
        " PRIMARY KEY (id), "
        " FOREIGN KEY (man_id) REFERENCES managers(id))"
    ),
    "residents": (
        "CREATE TABLE `residents`("
        " `id` int(20) NOT NULL,"
        " `f_name` varchar(100) NOT NULL,"
        " `l_name` varchar(100) NOT NULL,"
        " `email` nvarchar(100) NOT NULL,"
        " `phone` varchar(100) NOT NULL,"
        " `prop_id` int(20) NULL,"
        " PRIMARY KEY (id),"
        " FOREIGN KEY (prop_id) REFERENCES properties(id))"
    ),
}


def create_tables(my_cursor):
    # Dropping tables if they exists and creating new ones.
    my_cursor.execute("DROP TABLE IF EXISTS `managers`")
    my_cursor.execute(TABLES["managers"])
    my_cursor.execute("DROP TABLE IF EXISTS `properties`")
    my_cursor.execute(TABLES["properties"])
    my_cursor.execute("DROP TABLE IF EXISTS `residents`")
    my_cursor.execute(TABLES["residents"])
