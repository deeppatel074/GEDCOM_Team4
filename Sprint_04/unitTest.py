import unittest
import Sprint_04

class TestStringMethods(unittest.TestCase):
 
    def test_userstory31(self):
        result = ["ERROR: INDIVIDUAL: US31: Individual I22 (Utkarsh /Jain/) and I19 (Utkarsh /Jain/) have the same name and birth date"]
        self.assertNotEqual(Sprint_04.US31(),result)

    def test_userstory32(self):
        result = ["ERROR: FAMILY: US32: Family with the same spouse names and marriage date already exists:  Husband Name: Aarav /Jain/, Wife Name: Cherry /Jain/, Marriage Date: 5 MAR 2005"]
        self.assertNotEqual(Sprint_04.US32(),result)
    
    def test_userstory38(self):
        result = ["ERROR: INDIVIDUAL: US38: Individual ID I1 is not unique"]
        self.assertNotEqual(Sprint_04.US38(),result)

    def test_userstory39(self):
        result = ["ERROR: FAMILY: US39: Family with Family ID: F12 has more than 15 siblings"]
        self.assertNotEqual(Sprint_04.US39(),result)

    def test_userstory29(self):
        result = 6
        self.assertEqual(Sprint_04.US29(),result)

    def test_userstory30(self):
        result = 22
        self.assertEqual(Sprint_04.US30(),result)
    



if __name__ == '__main__':
    unittest.main()