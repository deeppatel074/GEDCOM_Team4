import unittest
import user_stories_07_08

class TestStringMethods(unittest.TestCase):
    def test_age(self):
        expected_output = ['ERROR: Birthday of Individual with id I10 is no longer alive is of age greater than 150.', 'ERROR: Birthday of Individual with id I11 is of age greater than 150.']
        self.assertEqual(user_stories_07_08.US07() , expected_output)

    def test_age_output(self):
        expected_output = ['ERROR: Birthday of Individual with id I6 is no longer alive is of age greater than 150.', 'ERROR: Birthday of Individual with id I12 is of age greater than 150.']
        self.assertNotEqual(user_stories_07_08.US07() , expected_output)

    def test_array_type(self):
        bool = False
        if type(user_stories_07_08.US07()) == list:
            bool = True
        self.assertTrue(bool)
    
    def test_array_content(self):
        expected_output = ['ERROR: Birthday of Individual with id I10 is no longer alive is of age greater than 150.', 'ERROR: Birthday of Individual with id I11 is of age greater than 150.']
        self.assertListEqual(user_stories_07_08.US07(), expected_output)
    
    def test_05(self):
        self.assertLessEqual(len(user_stories_07_08.US07()), 23)
    

if __name__ == '__main__':
    unittest.main()