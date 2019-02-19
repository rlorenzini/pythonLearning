

# num = 1
# while n>1:
#     num = num * n
#     n = n -1
#
#
# print(num)
#


class Factorial:
    def __init__(self):
        pass
    def factorial(self,n):
        self.n = n
        self.factorial = self.n

        while self.n>1:
            self.factorial = self.factorial * (self.n-1)
            self.n = self.n -1
        return(self.factorial)
n = Factorial()
n.factorial(int(input("Enter number.\n::")))
print(n.factorial)
