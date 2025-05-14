import math

"""
The Fibonacci sequence is defined by the recurrence relation: F_n = F_{n - 1} + F_{n - 2}, where F_1 = 1 and $F_2 = 1

What is the index of the first term in the Fibonacci sequence to contain $1000$ digits?
"""
# O(n) solution where n is the index of the first Fibonacci number with the desired number of digits
# O(1) time complexity with index, a, b being negligible variables
class Solution:
    def FibDigitCount(self, digits: int) -> int:

        # Start the index to the second index so as to always count the higher number
        index = 1
        a,b = 0,1 # two variables to walk through fibonacci sequence

        # instead of converting value to a string and then measuring length....just check how many times it takes to 
        # multiple 10 by itself to get to the number
        ## math.floor + 1 rounds number to closest whole number
        while math.floor(math.log10(b)) + 1 < digits:
            a, b = b, a + b
            index += 1

        return index

  
if __name__ == "__main__":
    
    solution = Solution() 
    print(solution.FibDigitCount(1000))
