def lookup_user(connection, username):
    """Return exactly the requested username, treating user input literally."""
    query = f"SELECT name FROM users WHERE name = '{username}'"
    return connection.execute(query).fetchall()
