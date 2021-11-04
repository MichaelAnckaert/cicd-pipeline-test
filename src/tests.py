import unittest

from greeter import Greeter


class GreeterTest(unittest.TestCase):
    def test_create_greeting(self):
        result = Greeter.create_greeting()
        self.assertEqual(result, "Hello, world!")

    def test_fail(self):
        self.assertEqual(2, 3)

if __name__ == "__main__":
    unittest.main()
