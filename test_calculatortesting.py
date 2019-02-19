import unittest
#reference calculatortesting.py
from calculatortesting import *

class CalculatorTests(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    def test_addition(self):
        print("\nTesting addition+ + + + +\n ")
        result = self.calculator.add(5,7)
        self.assertEqual(12,result)
    def test_subtraction(self):
        print("\nTesting subtraction- - - - -\n")
        result = self.calculator.subtract(10,7)
        self.assertEqual(3,result)
    def test_multiplication(self):
        print("\nTesting multiplication* * * * *\n")
        result = self.calculator.multiply(5,6)
        self.assertEqual(30,result)
    def test_division(self):
        print("\nTesting division/ / / / /\n")
        result = self.calculator.divide(30,6)
        self.assertEqual(5,result)
unittest.main()
