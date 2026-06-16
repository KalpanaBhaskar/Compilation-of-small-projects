import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(),'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse("Foo".isupper())
    
    def test_split(self):
        s='hello world' 
        #s= 90       
        # self.assertEqual(s.split(),['hello','world'])
        with self.assertRaises(TypeError):
            # s.split(2)
            self.assertEqual(s.split(),['hello','world'])   #fails
            # self.assertEqual(s.split(2),['hello','world'])  #passes
if __name__ == '__main__':
    unittest.main()
