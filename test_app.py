# test_app.py
import unittest
from app import add_numbers

class TestApp(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(3, 5), 8)

if __name__ == "__main__":
    unittest.main()
