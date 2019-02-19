#reference palindrome.py and palindromeclass.py

import unittest
from palindromeclass import *
class PalindromeTest(unittest.TestCase):
    def setUp(self):
        self.palindrome = Palindrome()
    def test_palindrome(self):
        result = self.palindrome.reverse("mom")
        self.assertEqual("palindrome",result)
    def test_not_palindrome(self):
        result = self.palindrome.reverse("tacos")
        self.assertEqual("not palindrome",result)
unittest.main()
