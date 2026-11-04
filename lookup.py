def lookup_user(connection, username):
    """Return exactly the requested username, treating user input literally."""
    return connection.execute(
        "SELECT name FROM users WHERE name = ?", (username,)
    ).fetchall()
