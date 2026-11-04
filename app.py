def lookup_user(connection, username):
    """Return the exact matching username, treating input as a literal string."""
    query = f"SELECT name FROM users WHERE name = '{username}'"
    return connection.execute(query).fetchall()
