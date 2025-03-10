"""
Find all multiples of 3 or 5 between 0 and 1000 and then sum them together

"""


# The basic solution simply applies an iterative approach to go through each number
# O(n)
def Solution(num: int):
    
    # Set variable to collect total sum
    total = 0

    # Iterate through each number from 0 to num
    for x in range(num):
        # if x divisible by 3 or 5 then add number to total
        if x % 3 == 0 or x % 5 == 0:
            total += x

    # Return total
    return total

# What if we applied a more mathematical approach utilizing the idea of arithmetic series?
# Arithmetic series is simply a list of numbers computerd by adding (or subtracting) a given constant (arithmetic mean of number k below n == k + 2k + 3k + ... mk)
# TO FIND THE COUNT OF MULTIPLES (m): Where m is m = (n-1)//k or essentially the count of multiples below n
# SUM OF MULTIPLES (sum): sum = [k * m * (m+1)]/2
# NOTE: every number divisble by 3 or 5 is a multiple of either
# O(1)
def MathSolution(n: int, k: int):
    m = (n-1) // k

    return int((k * m * (m+1)) / 2)


if __name__ == '__main__':
    
    solution = Solution(1000)
    print(solution)

    solution2 = MathSolution(1000,3) + MathSolution(1000,5) - MathSolution(1000,15)
    print(solution2)