import math

"""
 2520 is the smallest number that can be divided by each of the numbers from 1 to 20 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

# Solution: need to find and multiple together the max number of times each prime appears in the list of numbers
# LCM(a1​,a2​,...,an​)=p in primes∏​pmax(e1​,e2​,...,en​)

# At worst potentially O(n^2)
class Solution:
    def SmallestMultiple(self, low_range: int, high_range: int) -> int:

        # To collect max prime factors for each prime number
        prime_factorization = {}

        # Iterate through each number in range to determine the least common multiple
        for n in range(low_range, high_range + 1):
            
            # Dictionary for the prime numbers within an individual number in range
            factors = {}

            # begin with 2 and determine how many times the number can be divded by 2
            if n >= 2:
                factors[2] = 0
                while n % 2 == 0:
                    # divide with round down to the nearest whole number
                    n //= 2
                    factors[2] += 1
                
                # Check if there is a new max # of times that 2 was used
                if factors[2] != 0:
                    if 2 not in prime_factorization:
                        prime_factorization[2] = factors[2]
                    elif 2 in prime_factorization and factors[2] > prime_factorization[2]:
                        prime_factorization[2] = factors[2]

            # Iterate through odd numbers 
            # This works as with even numbers out (number divisible by 2) and by starting with 3, no larger odd numbers that can be divided by 3,5,7, etc... will be applicable
            i = 3
            
            # Iterate up to the number itself in the case that the number is a prime (i.e., 5 or 7)
            while i <= n:
                factors[i] = 0
                while n % i == 0:
                    n //= i
                    factors[i] += 1

                # Check if there is a new max # of times that i was used
                if factors[i] != 0:
                    if i not in prime_factorization:
                        prime_factorization[i] = factors[i]
                    elif i in prime_factorization and factors[i] > prime_factorization[i]:
                        prime_factorization[i] = factors[i]

                # iterate to the next odd number
                i += 2

        # Find the least common mutiple (i.e., 2^3 * 3^4 * 5 * 7)
        lcm = 1
        for prime in prime_factorization:
            lcm *= (prime ** prime_factorization[prime])

        
        return lcm
    

if __name__ == "__main__":
    low_range = 1
    high_range = 20

    solution = Solution()

    print(solution.SmallestMultiple(low_range, high_range))