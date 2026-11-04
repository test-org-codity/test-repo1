import unittest
from app import echo_value

class EchoTest(unittest.TestCase):
    def test_shell_metacharacters_are_literal(self):
        for value in ("hello", "hello world", "safe; printf injected", "$(printf injected)"):
            self.assertEqual(echo_value(value), value)

if __name__ == "__main__":
    unittest.main()
