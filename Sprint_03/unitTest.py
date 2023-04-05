import unittest
import Sprint_03

class TestStringMethods(unittest.TestCase):
    def test_userstory15(self):
        result = ["ERROR: FAMILY: US 15: Family with Family ID: F12 has more than 15 siblings"]
        self.assertEqual(Sprint_03.US15(),result)
    
    def test_userstory16(self):
        result = ["ERROR: FAMILY: INDIVIDUAL: US 16: Family Name of Individual I24 is different from the family name"]
        self.assertEqual(Sprint_03.US16(),result)

    def test_userstory23(self):
        result = ["ERROR: INDIVIDUAL: US23: Individual I22 (Utkarsh /Jain/) and I19 (Utkarsh /Jain/) have the same name and birth date"]
        self.assertEqual(Sprint_03.US23(),result)

    def test_userstory24(self):
        result = ["ERROR: FAMILY: US24: Family with the same spouses names and marriage date already exists: , Husband Name: Aarav /Jain/, Wife Name: Cherry /Jain/, Marriage Date: 5 MAR 2005"]
        self.assertEqual(Sprint_03.US24(),result)

if __name__ == '__main__':
    unittest.main()