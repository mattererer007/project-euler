import math

"""
In a 20 x 20 grid, find What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) 

up/down
left/right
left diaganolly
right diagonally

Should realistically be able to iterate through grid once per each approach

"""


class Solution:
    def largestProduct(self, grid: list[list[int]]) -> int:

        max_product = 0

        number_of_rows = len(grid)

        number_of_columns = len(grid[0])

        # Iterate left to right
        for row in grid:
            pointer = 3

            while pointer < number_of_columns:
                product = row[pointer] * row[pointer-1] * row[pointer-2] * row[pointer-3]

                max_product = max(max_product, product)

                pointer += 1
        
        # Iterate down and up
        for r in range(0, number_of_rows - 3):
            for c in range(0, number_of_columns):
                product = grid[r+3][c] * grid[r+2][c] * grid[r+1][c] * grid[r][c]
                max_product = max(max_product, product)

        # Iterate left diagonally
        ## Start in top right corner and iterate down and to the left
        ### row 0, col 16 [0,16], [1,17] [2,18] [3,19]
        ### row 0, col col 15 [0,15] [1,16] [2,17] [3,18] >> [1,16] [2,17] [3,18] [4,19]
        current = number_of_columns - 4
        tail_r, tail_c = 0, current

        while current >= 0:

            product = grid[tail_r][tail_c]* grid[tail_r+1][tail_c+1]* grid[tail_r+2][tail_c+2]* grid[tail_r+3][tail_c+3]
            max_product = max(max_product, product)

            if tail_c+3 == number_of_columns - 1:
                current -= 1
                tail_r, tail_c = 0, current
            else:
                tail_r += 1
                tail_c += 1

        current = number_of_columns - 4
        tail_r, tail_c = current, 0

        while current > 0:
            product = grid[tail_r][tail_c]* grid[tail_r+1][tail_c+1]* grid[tail_r+2][tail_c+2]* grid[tail_r+3][tail_c+3]
            max_product = max(max_product, product)

            if tail_r+3 == number_of_rows - 1:
                current -= 1
                tail_r, tail_c = current, 0
            else:
                tail_r += 1
                tail_c += 1

        # Iterate right diadonally
        ## Start in top left corner and iterate down to the right
        ### row 0, col 3 [0,3], [1,2] [2,1] [3,0]
        current = 3
        tail_r, tail_c = 0, current

        while current < number_of_columns:
            product = grid[tail_r][tail_c]* grid[tail_r+1][tail_c-1]* grid[tail_r+2][tail_c-2]* grid[tail_r+3][tail_c-3]
            max_product = max(max_product, product)

            if tail_r+3 == number_of_rows - 1:
                current += 1
                tail_r, tail_c = 0, current
            else:
                tail_r += 1
                tail_c -= 1

           
        return max_product

# A consolidation of the above
# O(n^2) with the double loops
# 4 constant actions potentially take place at each cell
class Solution2:
    def largestProduct(self, grid: list[list[int]]) -> int:

        max_product = 0

        number_of_rows = len(grid)
        number_of_columns = len(grid[0])

        for r in range(0, number_of_rows):
            for c in range(0,number_of_columns):
                # Left to right
                ## Check if the right most value is out of range
                if c+3 < number_of_columns:
                    product = grid[r][c] * grid[r][c+1] * grid[r][c+2] * grid[r][c+3]
                    max_product = max(max_product, product)
                # Up and down
                ## Check if the lowest value is out of range
                if r+3 < number_of_rows:
                    product = grid[r][c] * grid[r+1][c] * grid[r+2][c] * grid[r+3][c]
                    max_product = max(max_product, product)
                # Left and diagonally
                ## Check if the cell has at least 3 rows and 3 columns below it to the left
                if r+3 < number_of_rows and c+3 < number_of_columns:
                    product = grid[r][c]* grid[r+1][c+1]* grid[r+2][c+2]* grid[r+3][c+3]
                    max_product = max(max_product, product)
                # Right and diagonally
                ## Check if the cell has at least 3 rows and 3 columns below it to the right
                if r+3 < number_of_rows and c-3 >= 0:
                    product = grid[r][c]* grid[r+1][c-1]* grid[r+2][c-2]* grid[r+3][c-3]
                    max_product = max(max_product, product)

        return max_product

                


if __name__ == "__main__":
    input = """ 
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48 """

    grid = [[int(num) for num in line.split()] for line in input.strip().split('\n')]


    solution = Solution2()

    print(solution.largestProduct(grid))

