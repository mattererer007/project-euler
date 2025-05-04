"""
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

Now... how many paths are there for a 20 x 20?

ONLY move DOWN or RIGHT

"""

class Solution:
    def LatticePathCount(self, max_columns: int, max_rows: int) -> int:

        # memoize results to reduce calcuating the same path over and over again
        path = {}
        count = self.RecurPaths(0,0, max_columns, max_rows,path)

        return count


    def RecurPaths(self, col_position: int, row_position: int, max_columns: int, max_rows: int, path: dict) -> int:

        count = 0
        
        if (col_position, row_position) in path:
            return path[(col_position, row_position)]

        # Check if path is completed 
        if col_position == max_columns and row_position == max_rows:
            return 1
        

 
        # Go Down
        if row_position + 1 <= max_rows:
            count += self.RecurPaths(col_position, row_position+1, max_columns, max_rows,path)
        # Go Right
        if col_position + 1 <= max_columns:
            count += self.RecurPaths(col_position+1, row_position, max_columns, max_rows,path)


        path[(col_position, row_position)] = count
        return count


if __name__ == "__main__":

    col, row = 20,20

    solution = Solution()
    print(solution.LatticePathCount(col,row))