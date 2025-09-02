# Unit Tests

# Placeholder for unit tests.

import unittest

def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

class TestUnit(unittest.TestCase):
    def test_example(self):
        self.assertEqual(1 + 1, 2)

    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_subtract_numbers(self):
        self.assertEqual(subtract_numbers(5, 3), 2)

if __name__ == "__main__":
    unittest.main()
