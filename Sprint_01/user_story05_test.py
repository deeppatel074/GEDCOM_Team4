import unittest
import user_stories_05_06

class TestStringMethods(unittest.TestCase):

    # User Story 05 test cases
    def test_us05_01(self):
        result = ['Error: Marriage of family F9 occurred after death of husband']
        self.assertEqual(user_stories_05_06.US05(), result)

    def test_us05_02(self):
        self.assertNotEqual(user_stories_05_06.US05(), 5)

    def test_us05_03(self):
        self.assertTrue(len(user_stories_05_06.US05()) == 1)

    def test_us05_04(self):
        self.assertFalse(len(user_stories_05_06.US05()) == 10)
    
    def test_us05_05(self):
        self.assertTrue(isinstance(user_stories_05_06.US05(), list))


if __name__== '__main__':
    unittest.main()

