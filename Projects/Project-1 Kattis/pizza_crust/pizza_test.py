
import unittest
from pizzaCrust import pizza_time

class TestAah(unittest.TestCase):
    """
    test cases must start with test and must be a method
    """
    def test1_answer(self):
        radius = 1
        crust = 1
        ans = 0
        self.assertEqual(pizza_time(crust,radius), ans, 'broken')
    
    def test2_answer(self):
        radius = 100
        crust = 10
        ans = 81.000000
        self.assertEqual(pizza_time(crust,radius), ans, 'broken')
    
    def test3_answer(self):
        radius = 20
        crust = 2
        ans = 81.000000
        self.assertEqual(pizza_time(crust,radius), ans, 'broken')

    def test4_answer(self):
        radius = 10
        crust = 9
        ans = 1.000000
        self.assertEqual(pizza_time(crust,radius), ans, 'broken')

    def test5_answer(self):
        radius = 10
        crust = 1
        ans = 81.000000
        self.assertEqual(pizza_time(crust,radius), ans, 'broken')

    def test6_answer(self):
        radius = 2
        crust = 1
        ans = 25.000000
        self.assertEqual(pizza_time(crust,radius), ans, 'broken')


if __name__ =="__main__":
    unittest.main(verbosity=2)
