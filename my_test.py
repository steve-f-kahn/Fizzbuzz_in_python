import unittest
from fizzbuzz import *


class TestFizzBuzz(unittest.TestCase):

    def test_2(self):
        self.assertEqual( fizz(2) ,2)

    def test_3(self):
        self.assertEqual( fizz(3), 'fizz')

    def test_5(self):
        self.assertEqual( fizz(5), 'buzz')

    def test_15(self) :
        self.assertEqual( fizz(15), 'fizzbuzz')

    def test_4(self) :
        self.assertEqual( fizz(4), 4)

    def test_6(self) :
        self.assertEqual( fizz(6), 'fizz')

    def test_30(self) :
        self.assertEqual( fizz(30), 'fizzbuzz')

    def test_10(self) :
        self.assertEqual( fizz(10), 'buzz')


if __name__ == '__main__':
    unittest.main()
