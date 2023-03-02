import unittest
import Sprint_02

class TestStringMethods(unittest.TestCase):
    def test_userstory09(self):
        result01 = ['ERROR: INDIVIDUAL: US09: Birth date for individual I19 is after the mother death date', 'ERROR: INDIVIDUAL: US09: Birth date for individual I22 is after 9 months of the father death date']
        self.assertEqual(Sprint_02.US09(), result01)
     
    def test_userstory10(self):
        result01 = ['ERROR: INDIVIDUAL: US 10: Marriage for I13 should be after 14 year of the age', 'ERROR: INDIVIDUAL: US10: Marriage for I17 should be after 14 year of the age', 'ERROR: INDIVIDUAL: US 10: Marriage for I18 should be after 14 year of the age']
        self.assertEqual(Sprint_02.US10(), result01)

    def test_userstory21(self):
        result01 = ['ERROR: INDIVIDUAL: US21: Wife I6 in family F6 is not female', 'ERROR: INDIVIDUAL: US21: Husband I7 in family F4 is not male', 'ERROR: INDIVIDUAL: US21: Husband I7 in family F11 is not male']
        self.assertEqual(Sprint_02.US21(), result01)
    
    def test_userstory22(self):
        result01 = ['ERROR: INDIVIDUAL: US22: Individual ID I1 is not unique', 'ERROR: FAMILY: US22: Family ID F11 is not unique']
        self.assertEqual(Sprint_02.US22(), result01)


    # def test03_userstory01(self):
    #     is_True = False
    #     if type(user_sotry_01.US01()) == list:
    #         is_True = True
    #     self.assertTrue(is_True)

    # def test04_userstory01(self):
    #     is_True = False
    #     if type(user_sotry_01.US01()) != list:
    #         is_True = True
    #     self.assertFalse(is_True)

    # def test05_userstory01(self):
    #     result01 = ['Error: Birthday at I2 of Chandresh /Jain/ should before current date']
    #     self.assertListEqual(user_sotry_01.US01(), result01)



if __name__ == '__main__':
    unittest.main()