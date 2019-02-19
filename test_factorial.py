import unittest
from factorial import *

class FactorialTest(unittest.TestCase):
    def setUp(self):
        self.factorial = Factorial()
    def test_factorial(self):
        result = self.factorial.factorial(9)
        self.assertEqual(362880,result)
unittest.main()
###While testing, will display input value.
###Whatever the input is, the test will run Factorial(9) == 362880. 
