import unittest
from num_repe import *

class Test_repe(unittest.TestCase):
    def test1(self):
        self.assertEqual(numeros_repetidos([1,1,2,2,3]), 
                                           {1:2, 2:2, 3:1})
    def test2(self):
        self.assertEqual(numeros_repetidos([]), {})
    def test3(self):
        self.assertEqual(numeros_repetidos([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]), 
                                           {1:20})
    def test4(self):
        self.assertEqual(numeros_repetidos([9,5,6,7,3,6,4,1,2,4,7,3,6,8,4,3]), 
                                           {1:1, 2:1, 3:3, 4:3, 5:1, 6:3, 7:2, 8:1, 9:1})
    def test5(self):
        self.assertEqual(numeros_repetidos([99,99,99,98,98,1]), 
                                           {99:3, 98:2, 1:1})
    def test6(self):
        self.assertEqual(numeros_repetidos([9000000000000000000000000, 9000000000000000000000000, 9000000000000000000000000]), 
                                           {9000000000000000000000000: 3})
    def test7(self):
        self.assertEqual(numeros_repetidos([0.00000000000001, 0.00000000000001, 0.00000000000001 ,0.00000000000001]), 
                                           {0.00000000000001:4})




if __name__ == "__main__": # pragma: no cover
    unittest.main()