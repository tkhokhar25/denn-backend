import database_connection

def update_action(user_id, friend_id, action):
    connection, cursor = database_connection.get_database_connection()

    cursor.execute("UPDATE users SET state = '" + str(action) + "' WHERE id = " + str(id) + " OR id = " + str(friend_id), connection)