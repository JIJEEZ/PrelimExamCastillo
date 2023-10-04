import unittest

def area(length, width, height, area):
    length = float(12.5)
    width  = float (12.5)
    height = float (12.5)

    
class myTest(unittest.TestCase):

    def test(self):

        self.area = self.length * self.width * self.height
        return area

        perimeter = 2 * (self. length + self.width)
        return perimeter

        self.assertEqual(area(), 37.5)

if __name__=='__main__':

    unittest.main()