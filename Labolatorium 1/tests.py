import unittest
from calculator import Add
 
class TestCalculator(unittest.TestCase):
 
    def test_add_empty(self):
        self.assertEqual(Add(""),0)
 
    def test_add_one(self):
        self.assertEqual(Add("1"),1)
 
    def test_add_multiple(self):
        self.assertEqual(Add("2,2,1"),5)
 
    def test_add_newline(self):
        self.assertEqual(Add("1\n2,3"),6)
 
    def test_wrong_newline(self):
        with self.assertRaises(ValueError):
            Add("1\n,2")
 
if __name__ == "__main__":
    unittest.main()