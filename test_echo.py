import unittest
from echo import echo_value

class EchoTest(unittest.TestCase):
    def test_normal_value(self):
        self.assertEqual(echo_value("hello"), "hello")
    def test_empty_value(self):
        self.assertEqual(echo_value(""), "")
    def test_whitespace(self):
        self.assertEqual(echo_value("hello world"), "hello world")
    def test_metacharacters_are_literal(self):
        for value in ("safe; printf injected", "$(printf injected)", "a'b", 'a"b'):
            self.assertEqual(echo_value(value), value)
