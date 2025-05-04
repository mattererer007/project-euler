"""
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

Now... how many paths are there for a 20 x 20?

ONLY move DOWN or RIGHT

"""

# This solution is O(mn) time complexity where m is the number of rows and n is the number of columns. With memoization nothing is visited more than once
class Solution:
    def LatticePathCount(self, max_columns: int, max_rows: int) -> int:

        # memoize results to reduce calcuating the same path over and over again
        path = {}
        # use recursion to explore all viable paths
        count = self.RecurPaths(0,0, max_columns, max_rows,path)

        return count


    def RecurPaths(self, col_position: int, row_position: int, max_columns: int, max_rows: int, path: dict) -> int:
        
        # Instantiate a count variable
        count = 0
        
        # If a position has already been visited....then simply return however many unique paths go from that position to the bottom right
        if (col_position, row_position) in path:
            return path[(col_position, row_position)]

        # Check if path is completed 
        if col_position == max_columns and row_position == max_rows:
            return 1
        

 
        # Go Down
        if row_position + 1 <= max_rows:
            # Sum up all the counts as the recusion comes back
            count += self.RecurPaths(col_position, row_position+1, max_columns, max_rows,path)
        # Go Right
        if col_position + 1 <= max_columns:
            # Sum up all the counts as the recusion comes back
            count += self.RecurPaths(col_position+1, row_position, max_columns, max_rows,path)

        # As the recursion comes back and each individual row, col is revisisted, the final total count for that position is listed
        # Ultimately all the counts collate back till (0,0) which is then the sum
        path[(col_position, row_position)] = count
        return count


if __name__ == "__main__":

    col, row = 20,20

    solution = Solution()
    print(solution.LatticePathCount(col,row))