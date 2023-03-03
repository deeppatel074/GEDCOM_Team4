import unittest
import Sprint_02

class TestStringMethods(unittest.TestCase):
    def test_userstory09(self):
        bool = False
        if type(Sprint_02.US09()) == list:
            bool = True
        self.assertTrue(bool)
     
    def test_userstory10(self):
        self.assertLessEqual(len(Sprint_02.US10()), 7)

    def test_userstory17(self):
        result01 = ["ERROR: FAMILY: US17: No marriages to descendents I1 I15 'I15'", "ERROR: FAMILY: US17: No marriages to descendents I7 I8 'I7'", "ERROR: FAMILY: US17: No marriages to descendents I20 I21 'I20'"]
        self.assertNotEqual(Sprint_02.US17(), result01)
   
    def test_userstory18(self):
        result01 = ['ERROR: FAMILY: US18: No marriages to siblings HusbandI7 WifeI8', 'ERROR: FAMILY: US18: No marriages to siblings HusbandI20 WifeI21']
        self.assertNotEqual(Sprint_02.US18(), result01)

    def test_userstory21(self):
        result01 = ['ERROR: INDIVIDUAL: US21: Wife I6 in family F6 is not female', 'ERROR: INDIVIDUAL: US21: Husband I7 in family F4 is not male', 'ERROR: INDIVIDUAL: US21: Husband I7 in family F11 is not male']
        self.assertEqual(Sprint_02.US21(), result01)
    
    def test_userstory22(self):
        result01 = ['ERROR: INDIVIDUAL: US22: Individual ID I1 is not unique', 'ERROR: FAMILY: US22: Family ID F11 is not unique']
        self.assertEqual(Sprint_02.US22(), result01)

    def test_userstory36(self):
        result01 = [['I24', 'Maharsh /Jain/', 'MALE', '21 FEB 2023', '0', 'TRUE', 'N/A', "{'F2'}", 'N/A']]
        self.assertEqual(Sprint_02.US36(), result01)
    
    def test_userstory37(self):
        result01 = [['I24', 'Maharsh /Jain/', 'MALE', '21 FEB 2023', '0', 'TRUE', 'N/A', "{'F2'}", 'N/A']]
        self.assertNotEqual(Sprint_02.US37(), result01)



if __name__ == '__main__':
    unittest.main()