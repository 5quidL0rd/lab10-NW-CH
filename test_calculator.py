#https://github.com/5quidL0rd/lab10-NW-CH
#Partner 1: Blake Fowler
#Partner 2: Grayson Christie 



import unittest
from calculator import *





class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
     def test_multiply(self): 
          
          self.assertEqual(mul(3,3), 9)
          self.assertEqual(mul(10, 5), 50)
          self.assertEqual(mul(11, 100), 1100)

     def test_divide(self):
          
          self.assertEqual(div(3,3), 1)

          self.assertEqual(div(10, 5), 2)

          self.assertEqual(div(8, 2), 4)

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
     def test_log_invalid_argument(self):
          
          with self.assertRaises(ValueError):
               log(2, 0)

     def test_hypotenuse(self):
          
          self.assertEqual(hypotenuse(3, 4), 5.0)
          self.assertEqual(hypotenuse(5, 12), 13.0)
          self.assertEqual(hypotenuse(1,1), math.sqrt(2), places=5)

     def test_sqrt(self):
          
          with self.assertRaises(ValueError):
            square_root(-1)
          
          self.assertEqual(square_root(9), 3.0)
          self.assertEqual(square_root(16), 4.0)

        

# Do not touch this
if __name__ == "__main__":
    unittest.main()