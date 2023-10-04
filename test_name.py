import unittest

def equal():

    name = 'RENZO'
    return name

class myTest(unittest.TestCase):
    def test(self):
        self.assertEqual(equal(), 'RENZO')

if __name__=='__main__':

    unittest.main()