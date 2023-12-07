import unittest

class Test_something(unittest.TestCase):

    def test_string(self):
        a = 'Something'
        b = 'Nothing'
        self.assertEqual(a, b)

    def test_boolean(self):
        a = False
        b = True
        self.assertEqual(a, b)

if __name__ =='__main__':   
    unittest.main()