import database_connection

if __name__ == '__main__':
    connection, cursor = database_connection.get_database_connection()
    cursor.execute("INSERT INTO users (email) VALUES ('shit');", connection)