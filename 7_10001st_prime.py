import math

"""
By listing the first six prime numbers: 2,3,5,7,11 , and , we can see that the 6th prime is 13

What is the 10001st prime number?
"""

# learned some cool math today - Rosser/Dusart theorem says that the nth prime number P_n will be between n*ln(n) and n(ln(n)+ln(ln(n)))
## Here are some inequalities for the nth prime. The lower bound is due to Dusart (1999) and the upper bound to Rosser (1941) >>  n ( log ⁡ n + log ⁡ log ⁡ n − 1 ) < p n < n ( log ⁡ n + log ⁡ log ⁡ n ) for  n ≥ 6. 
# (1) First calculate an upper bound
# (2) Use an algorithm to determine the list of primes up to that bound >> Sieve of Eratosthenes (because easy)
## Save space by just doing odd numbers....and 2
# (3) Iterate through to the 10001 prime number >> return



class Solution:
    def FindPrimeNumber(self, target: int) -> int:
        
        # Rosser / Dusart Upper bound
        upper_bound = int(target * (math.log(target) + math.log(math.log(target))))

        # Create of potential prime numbers
        # starting with 3 and going for all odd numbers up to upper bound
        ## to calcuate number of odd numbers use formula (upper bound - lower bound) // 2 + 1 (iff both are odd) otherwise (upper bound - lower bound + 1) / 2
        if upper_bound % 2 == 0: # if upper bound even
            size = (upper_bound - 3 + 1) // 2
        else: # if upper bound odd
            size = (upper_bound - 3) // 2 + 1

        odd_numbers = [True] * size

        # iterate through list
        for i in range(0, size):
            if odd_numbers[i]:
                # convert index to odd number (i.e., i = 0 i >> 3)
                number = (2 * i) + 3
                if number * number > upper_bound:
                    break

            # determine the index of the first number that is divisible by given odd number
            ## i.e., number = 3 >> (3*3 -3)//2 >> 6//2 >> 3 (0,1,2,3) >> (3,5,7,9). 9 is the first odd number divisible by 3
            ### there are 6 places from 3 to 9, need to only include odd ones thus divide by 2
            starting_place = (number * number - 3) // 2 
            
            # iterate through all odd multiples of given number (i.e, 3 >> 9, 15, 21 etc.)
            for j in range(starting_place, len(odd_numbers),number):
                odd_numbers[j] = False


        # find target prime numbers 
        ## remember 2 needs to be counted
        ## iterate through list and convert tagged as True to a number 
        prime_numbers = [2] + [2 * i + 3 for i,val in enumerate(odd_numbers) if val]

        # return target -1 to consider 2 
        return prime_numbers[target-1]





if __name__ == "__main__":
    solution = Solution()

    target = 10001
    print(solution.FindPrimeNumber(target))