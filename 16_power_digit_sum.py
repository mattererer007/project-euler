import math

"""
2^15 = 32768 and the sum of its digits is 3+2+7+6+8 = 26

What is the sum of the digits of the number 2^1000?
"""
# O(n) time complexity where 'n' is the number of digits in 2^1000, O(1) space complexity as all that is stored is the digit itself
class Solution:
    def PowerDigitSum(self, number: int, power: int) -> int:

        # set return value
        digit_sum = 0

        # use ** as this preserves the value as a long integer vs. math.pow which turns it into a float
        calculated_number = number ** power

        # use modulo math to peel of digit by digt and sum them together
        while calculated_number > 0:
            digit_sum += calculated_number % 10

            # Use // to round down number to closest integer
            calculated_number = calculated_number // 10


        return int(digit_sum)
    

if __name__ == "__main__":
    solution = Solution()

    print(solution.PowerDigitSum(2,1000))