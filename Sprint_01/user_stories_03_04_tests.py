import unittest
import user_stories_03_04

class TestStringMethods(unittest.TestCase):
    # USER STORY 03 TESTS START
    def test_no_dob(self):
        output = ['Error: Date of death is before birth date for Rodulal /Jain/', 'Error: Person Miloni /Jain/ does not have date of birth']
        self.assertEqual(user_stories_03_04.validate_births(), output)

    def test_incorrect_result(self):
        output = ['Error: Dat of death is before birth date for Rodulal /Jain/', 'Error: Person Miloni /Jain/ does not have date of birth']
        self.assertNotEqual(user_stories_03_04.validate_births(), output)

    def test_result_comparison(self):
        output = ['Error: Date of death is before birth date for Rodulal /Jain/', 'Error: Person Miloni /Jain/ does not have date of birth']
        self.assertListEqual(user_stories_03_04.validate_births(), output)
    
    def test_result_list_postive(self):
        self.assertTrue(len(user_stories_03_04.validate_births()) == 2)

    def test_result_list_negative(self):
        self.assertFalse(len(user_stories_03_04.validate_births()) == 0)

    # USER STORY 03 TESTS END


if __name__ == '__main__':
    unittest.main()