import database_connection
import select

def update_action(user_id, friend_id, action):
    connection, cursor = database_connection.get_database_connection()

    cursor.execute("UPDATE users SET state = '" + str(action) + "' WHERE id = " + str(user_id) + " OR id = " + str(friend_id) + ";", connection)

def trigger(user_id, friend_id):    
    connection, cursor = database_connection.get_database_connection()

    cursor.execute("LISTEN status_changed;")

    while True:
        select.select([connection], [], [])
        connection.poll()

        while connection.notifies:
            cursor.execute("SELECT state FROM users WHERE id = " + str(user_id))
            return {"state" : cursor.fetchall()[0][0]}