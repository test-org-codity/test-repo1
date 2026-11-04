def lookup_user(connection, username):
    """Return the exact matching username, treating input as a literal string."""
    return connection.execute(
        "SELECT name FROM users WHERE name = ?", (username,)
    ).fetchall()
