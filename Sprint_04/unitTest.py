import unittest
import Sprint_04

class TestStringMethods(unittest.TestCase):
 
    def test_userstory31(self):
        result = ["ERROR: INDIVIDUAL: US31: Individual I22 (Utkarsh /Jain/) and I19 (Utkarsh /Jain/) have the same name and birth date"]
        self.assertNotEqual(Sprint_04.US31(),result)

    def test_userstory32(self):
        result = ["ERROR: FAMILY: US32: Family with the same spouse names and marriage date already exists:  Husband Name: Aarav /Jain/, Wife Name: Cherry /Jain/, Marriage Date: 5 MAR 2005"]
        self.assertNotEqual(Sprint_04.US32(),result)



if __name__ == '__main__':
    unittest.main()