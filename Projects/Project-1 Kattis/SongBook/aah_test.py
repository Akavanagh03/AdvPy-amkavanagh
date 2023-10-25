
import unittest
from aah import goOrNo

class TestAah(unittest.TestCase):
    """
    test cases must start with test and must be a method
    """
    def test1_answer(self):
        person1 = "aaaah"
        doctor1 = "aaaaah"
        self.assertEqual(goOrNo(person1,doctor1), "no", 'broken')
    
    def test2_answer(self):
        person2 = "aaaaaaah"
        doctor2 = "aaah"
        self.assertEqual(goOrNo(person2,doctor2), "go", 'borken')
    
    def test3_answer(self):
        person3 = "aaaaah"
        doctor3 = "aaaaah"
        self.assertEqual(goOrNo(person3,doctor3), "go", 'broken')


if __name__ =="__main__":
    unittest.main(verbosity=2)
