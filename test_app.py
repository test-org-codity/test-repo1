import sqlite3
import unittest
from app import lookup_user

class LookupTest(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect(":memory:")
        self.db.execute("CREATE TABLE users (name TEXT)")
        self.db.executemany("INSERT INTO users VALUES (?)", [("alice",), ("bob",)])
    def tearDown(self):
        self.db.close()
    def test_exact_lookup(self):
        self.assertEqual(lookup_user(self.db, "alice"), [("alice",)])
    def test_injection_cannot_read_other_users(self):
        self.assertEqual(lookup_user(self.db, "' OR 1=1 --"), [])
    def test_quotes_are_literal(self):
        self.assertEqual(lookup_user(self.db, "O'Reilly"), [])

if __name__ == "__main__":
    unittest.main()
