import math

"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""


class Solution:
    # O(n) time solution with O(1) space given that only two variables are created
    def SumSquareDifference(self, natural_num: int) -> int:

        # sum of all the numbers up to limit inputted and then squared
        # (1+2+3+4+5+...)^2
        sum_of_n = 0

        # sum of the squares of all natural numbers to the limit inputted
        # 1^2 + 2^2 + 3^ + 4^2 + 5^2 + ...
        sum_of_squares = 0

        # iterate through each number in range given to calculate sum        
        for num in range(1, natural_num + 1):
            sum_of_squares += num ** 2

            sum_of_n += num

        return (sum_of_n ** 2) - sum_of_squares
    
    # O(1) time solution with O(1) space 
    # SUm of all natural numbers from 1 to n can be written as 1∑n= n(n+1)​/2
    # Sum of all squares from 1 to n can be written as ∑n​^2=n(n+1)(2n+1)​/6
    def SumSquareDifferenceEfficiently(self, natural_num: int) -> int:
            sum_of_n = natural_num * (natural_num + 1) // 2
            sum_of_squares = natural_num * (natural_num + 1) * (2 * natural_num + 1) // 6
            return sum_of_n ** 2 - sum_of_squares

            


if __name__ == "__main__":
    solution = Solution()

    print(solution.SumSquareDifference(100))