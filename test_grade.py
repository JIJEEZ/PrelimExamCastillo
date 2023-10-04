import unittest

def grade(x):
    return x >= 50

class myTest(unittest.TestCase):
    def test(self):
        self.assertTrue(grade(50))
        print('Passed')

if __name__=='__main__':

    unittest.main()