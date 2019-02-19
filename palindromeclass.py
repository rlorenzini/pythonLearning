#reference palindrome.py and test_palindrom.py

class Palindrome():
    def __init__(self):
        pass
    def reverse(self,word):
        self.word = word
        if self.word == self.word[::-1]:
            return ("palindrome")
            print("Palindrome.\n")
        else:
            return ("not palindrome")
            print("Not palindrome.\n")
