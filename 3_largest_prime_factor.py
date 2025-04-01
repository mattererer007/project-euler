from math import sqrt
"""Return the largest prime factor of a number

i.e., for number 13195, the primes are 5, 7, 13, 29

# Hint: If a number n has a factor greater than √n, it must also have a smaller factor


"""
#O(n) run time O(1) space
class Solution1:
    def largestPrime(self, num: int) -> int:
        
        largest = None
        i = 2
        
        while i * i <= num:
            if num % i == 0:
                num //= i
                largest = i
            else:
                i += 1

            print(num, largest, i)

        # After loop, if num > 1, it's a prime and the largest factor
        return num if num > 1 else largest




if __name__ == "__main__":
    solution = Solution1()
    num = 600851475143
    num2 = 8827

    print(solution.largestPrime(num))