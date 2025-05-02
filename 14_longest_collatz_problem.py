"""
The following iterative sequence is defined for the set of positive integers:

(a) n >> n/2 (when n even)

(b) n >> 3n + 1 (when n is odd)


Using the rule above and starting with 13, we generate the following sequence:

13 > 40 > 20 > 10 > 5 > 16 > 8 > 4 > 1

It can be seen that this sequence (starting at and finishing at ) contains terms. Although it has not been proved yet (Collatz Problem), it is thought 
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
# O(n) time complexity due to memoization in storing previous work completed so not resused
# O(n) space complexity with storing up to n numbers (1....1M)
class Solution:
    def longestCollatz(self, max_int: int) -> int:

        # Set variables
        tracker = {}  # track collatz problem counts to avoid duplicate calculations
        max_count = float('-inf') # set the max count of a sequence
        largest_collatz_number = 0 # variable with the longest pathway

        # Iterate through all numbers in given range
        for x in range(1, max_int+1):
            count = 0
            curr = x
            # the number in the sequence is NOT 1 
            while curr > 1:
                # If the current number is already found in tracker....that means that that 
                # part of that sequence has already been explored
                if curr in tracker:
                    # merge the count and break while loop
                    count += tracker[curr]
                    break

                # If even...then divide current by 2
                elif curr % 2 == 0:
                    curr = curr // 2
                    count += 1

                # If odd, then multiple by 3 and divide by 1
                else:
                    curr = (3*curr) + 1
                    count += 1
                
            # Add count and number to tracker for future reference
            tracker[x] = count
            # Check if a new longest path has been discovered
            if count > max_count:
                max_count = count
                largest_collatz_number = x    


        return largest_collatz_number
    
if __name__ == "__main__":

    number = 1000000

    solution = Solution()
    print(solution.longestCollatz(number))

