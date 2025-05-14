"""
n! means n x (n - 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800 and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27

Find the sum of the digits in the number 100!
"""

# O(n) solution based on computing the factorial with O(n) space due to recursion stack (could be made O(1) with loop)
class Solution:
    def FactorialDigitSum(self, digit: int) -> int:
        
        """
        Try with recursion 

        RecurFactorial(4)
        4 * RecurFactorial(3)
        4 * (3 * RecurFactorial(2))
        4 * (3 * (2 * RecurFactorial(1)))
        4 * 3 * 2 * 1 = 24
        """
        def RecurFactorial(num:int) -> int:
            if num <= 1:
                return 1
            else:
                return num * RecurFactorial(num-1)
            
        factorial_result = RecurFactorial(digit)
        total_digit_sum = 0
        digit_place = 1

        while factorial_result > 0:
            # Sum the digit at each place (i.e., 1s, 10s, 100s, etc.)
            total_digit_sum += (factorial_result % (10*digit_place)) // (10*digit_place//10)
            # reduce the factorial result in order to consider the next number
            factorial_result = factorial_result - (factorial_result % (10*digit_place))
            # increase the digit place by 10 to continue iterating through the number
            digit_place *= 10

        return total_digit_sum




if __name__ == "__main__":
    
    solution = Solution()

    print(solution.FactorialDigitSum(100))

    