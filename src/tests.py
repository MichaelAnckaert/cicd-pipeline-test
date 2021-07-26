from unittest import TestCase

from greeter import Greeter


class GreeterTest(TestCase):
    def test_create_greeting(self):
        result = Greeter.create_greeting()
        self.assertEqual(result, "Hello, world!")
