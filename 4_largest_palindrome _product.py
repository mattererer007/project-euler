import math

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two -digit numbers is 9009 = 91 * 99

Find the largest palindrome made from the product of two 3-digit numbers.
"""

# Brute force but efficient brute force
# (1) start at the largest possible number that can be created by two 3 digit numbers and iterate down
# (2) start at the largest possible 3 digit number and divide the identified plaindromic number starting with the largest first
# These two steps shoudl reduce the amount of combinations explored
class Solution:
    def largestPalindrome(self, digits: int) -> int:

        # find largest possible number:
        largest_divisor = 0
        incrementer = 1 
        for x in range(0,digits):
            largest_divisor += incrementer
            incrementer *= 10

        largest_divisor *= 9

        # find smallest possible numner
        smallest_divisor = 1
        for x in range(1,digits):
            smallest_divisor *= 10

        # Find range of all potential numbers that can be created by multiplying together two 3 digit numbers
        largest_possible_number = (largest_divisor) * (largest_divisor)
        smallest_possible_number = (smallest_divisor) * (smallest_divisor)

        # iterate through all numbers in range
        for x in range(largest_possible_number, smallest_possible_number, -1):
            # Check if pallindromic
            if str(x) == str(x)[::-1]:
                # Check if the pallindromic number is a result of two 3 digit numbers being multiplied together
                for y in range(largest_divisor, smallest_divisor, -1):
                    if (x % y) == 0 and x / y <= largest_divisor and x / y >= smallest_divisor:

                        # 906609
                        return x

            

if __name__ == "__main__":

    solution = Solution()

    print(solution.largestPalindrome(3))

