def lookup_user(connection, username):
    """Return exactly the requested username, treating user input literally."""
    query = "SELECT name FROM users WHERE name = ?"
    return connection.execute(query, (username,)).fetchall()
