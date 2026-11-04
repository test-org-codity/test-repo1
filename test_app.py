import sqlite3
import unittest
from app import lookup_user

class LookupTest(unittest.TestCase):
    def test_lookup_and_injection(self):
        db = sqlite3.connect(":memory:")
        db.execute("CREATE TABLE users (name TEXT)")
        db.executemany("INSERT INTO users VALUES (?)", [("alice",), ("bob",)])
        self.assertEqual(lookup_user(db, "alice"), [("alice",)])
        self.assertEqual(lookup_user(db, "' OR 1=1 --"), [])
        self.assertEqual(lookup_user(db, "O'Reilly"), [])

if __name__ == "__main__":
    unittest.main()
