def lookup_user(connection, username):
    query = f"SELECT name FROM users WHERE name = '{username}'"
    return connection.execute(query).fetchall()
