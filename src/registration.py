from database_connection import *
from passlib.hash import sha256_crypt

def create_user(email, password):
    connection, cursor = get_database_connection()
    password = sha256_crypt.hash(password)

    try:
        cursor.execute("INSERT INTO users (email, password) VALUES ('" + str(email) + "', '" + str(password) + "') RETURNING id;", connection)
        id = cursor.fetchall()[0][0]

        return {"status" : "success", "code" : 200, "message" : "USER CREATED", "result" : {"id" : id}}

    except:
        # Someone with that email exists
        return {"status" : "failure", "code" : 400, "message" : "USER ALREADY EXISTS", "result" : {}}

def check_credentials(email, password):
    connection, cursor = get_database_connection()

    cursor.execute("SELECT id, password FROM users WHERE email = '" + str(email) + "';", connection)
    result = cursor.fetchall()

    if len(result) == 0:
        return {"status" : "failure", "code" : 400, "message" : "NO USER WITH THAT EMAIL EXISTS", "result" : {}}

    user_id = result[0][0]
    hashed_password = result[0][1]

    is_password_correct = sha256_crypt.verify(password, hashed_password)

    if is_password_correct:
        return {"status" : "success", "code" : 200, "message" : "VALID CREDENTIALS", "result" : {"id" : user_id}}
    else:
        return {"status" : "failure", "code" : 400, "message" : "INCORRECT PASSWORD", "result" : {"id" : user_id}}