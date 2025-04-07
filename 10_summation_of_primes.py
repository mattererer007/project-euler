"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Can use very similar approach to finding the 10001st prime number
"""

#run time approximately (and pessimistically) O(n^2) to accomodate iterating over the list multiple times  
class Solution():
    def sum_of_primes(self, num: int) -> int:  

        prime_sum = 2

        # Create list of potential prime numbers (i.e., odd numbers after 2)
        # starting with 3 and going for all odd numbers up to input (num)
        ## to calcuate number of odd numbers use formula (upper bound - lower bound) // 2 + 1 (iff both are odd) otherwise (upper bound - lower bound + 1) / 2. Note lower bound is 3 in this case
        if num % 2 == 0: # if upper bound even
            size = (num - 3 + 1) // 2
        else: # if upper bound odd
            size = (num - 3) // 2 + 1

        # list of size of potential odd numbers
        list_of_nums = [True] *size

        # iterate through list
        for i in range(0, size):
            # if a number has not already been determine to be divisible by a lower i... will still be shown as True
            if list_of_nums[i]:
                # convert index to odd number (i.e., i = 0 i >> 3)
                number = (2 * i) + 3

                # to limit how far I need to go in list of numbers before 2M
                if number * number > num:
                    break

            # determine the index of the first number that is divisible by given odd number
            ## i.e., number = 3 >> (3*3 -3)//2 >> 6//2 >> 3 (0,1,2,3) >> (3,5,7,9). 9 is the first odd number divisible by 3
            ### there are 6 places from 3 to 9, need to only include odd ones thus divide by 2
            starting_place = (number * number - 3) // 2 
            
            # iterate through all odd multiples of given number (i.e, 3 >> 9, 15, 21 etc.)
            for j in range(starting_place, len(list_of_nums),number):
                list_of_nums[j] = False


        # find sum of prime numbers < 2000000 
        ## iterate through list and convert tagged as True to a number 
        for i,val in enumerate(list_of_nums):
            if val:
                prime_sum += 2 * i + 3

        return prime_sum
     


if __name__ == "__main__":

    solution = Solution()
    num = 2000000
    print(solution.sum_of_primes(num))