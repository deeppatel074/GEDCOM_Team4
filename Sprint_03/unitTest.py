import unittest
import Sprint_03

class TestStringMethods(unittest.TestCase):
    def test_userstory15(self):
        result = ["ERROR: FAMILY: US 15: Family with Family ID: F12 has more than 15 siblings"]
        self.assertEqual(Sprint_03.US15(),result)
    
    def test_userstory16(self):
        result = ["ERROR: FAMILY: INDIVIDUAL: US 16: Family Name of Individual I24 is different from the family name"]
        self.assertEqual(Sprint_03.US16(),result)


if __name__ == '__main__':
    unittest.main()