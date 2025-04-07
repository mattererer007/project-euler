import math

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c , for which, a^2 + b^2 = c^2

i.e., 3^2 + 4^2 = 5^2 = 25

There exists exactly one Pythagorean triplet for which a + b + c == 1000

find the product of a*b*c
"""

# Rules to fininding the sides of a Pythagorean triangle (right triangle) using twp positive integers m,n where m > n
## a = m^2 - n^2
## b =  2mn
## c = m^2 + n2

### a + b + c >> (m^2 - n^2) + 2mn + (m^2 + n^2) >> 2m^2 + 2mn >> 2m(m+n) == 1000 >> m(m+n) == 500 >> n = (500/m) - m

# runtime roughly O(needed_sum) where you iterate through all values of m up until 1000 but assuming that n is at least half of needed sum then maybe more like O(sqrt(needed_sum/2)) anticipating that you
# only would need to get halfway to half of needed sum

class Solution:
    def find_pythagorian_triple(self, needed_sum: int) -> int:

        a,b,c = 0,0,0
        m,n = 2, 0

        # Make sure not tooo many iterations are run if there is in fact no actual solution 
        while m < math.sqrt(needed_sum) and (a+b+c) != 1000:

            # Find the n value given above formula
            n = self.find_n(m, needed_sum)

            # Check if n is > m or not an integer (not completely divisible)
            if n == -1:
                m += 1
            # Otherwise the correct m has been found
            else: 
                a,b,c = (m**2 - n**2), 2*m*n, (m**2 + n**2)

        return int(a*b*c)            
            
    # Find n given m and needed sum
    def find_n(self, m: int, needed_sum: int) -> int:

        n = (((needed_sum/2)/m) - m)

        if n > m or not n.is_integer():
            return -1
        else:
            return n


    

if __name__ == "__main__":
    solution = Solution()

    needed_sum = 1000

    print(solution.find_pythagorian_triple(needed_sum))

