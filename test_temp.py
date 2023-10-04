import unittest

def temp(c,f):
    return c/f

class myTest(unittest.TestCase):
    def test(self):
        self.assertEqual(temp(30,10), 3)

if __name__=='__main__':

    unittest.main()