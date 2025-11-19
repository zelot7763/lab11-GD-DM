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
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(9, 9), 81)
        self.assertEqual(mul(9123, 69348), 632661804)
        self.assertEqual(mul(23.9885, 2.8967), 69.48748795)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(5, 10), 2)
        self.assertEqual(div(7, 95263), 13609)
        self.assertEqual(div(89.4937, 23.889), 0.2669349909546705522)
    # ##########################

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
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(15, 20), 25)
        self.assertAlmostEqual(hypotenuse(17, 53), 55.65968020030299)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        with self.assertRaises(ValueError):
            square_root(-1)
        # Test basic function
        self.assertEqual(square_root(144), 12)
        self.assertEqual(square_root(952), 30.854497241083024978)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()