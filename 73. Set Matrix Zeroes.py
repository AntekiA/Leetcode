class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        colu = len(matrix[0])
        m = []
        n = []
        i = j = a = b = 0
        while i < row:
            while j < colu:
                if matrix[i][j] == 0:
                    m.append(i)
                    n.append(j)
                j += 1
            i += 1
            j = 0
        while a < row:
            if a in m:
                matrix[a] = [0] * colu
            a += 1
        while b < colu:
            if b in n:
                for i in range(row):
                     matrix[i][b] = 0
            b += 1
          
class Solution(object):
    def setZeroes(self, matrix):
        '''
        Idea:
        Use a var to store the line # of which has the first 0.
        Use that line as a mask line. update the all items in that line to 1. 
        When we meet a 0, update the mask line's same index item to 0, 
            and then update the items in current line to 0.
        Make a new loop which uses the mask line to do 'and' operation with each line. 
        At the end, change the the mask line to all 0.
        '''

        mask = -1
        high = len(matrix)
        width = len(matrix[0])
        for r in range(high):
            clear = False
            for c in range(width):
                if matrix[r][c] == 0:
                    if mask == -1:                  # Meet the first 0
                        mask = r                    # Get the mask line number
                        for i in range(width):      # The 0 in the mask line will keep 0, change other items to 1
                            matrix[mask][i] = 1 if matrix[mask][i] != 0 else 0
                        break                       # We don't want to clear the mask line 
                    else:                           # Meet any other line which has 0
                        clear = True                # Will clear the line to all 0
                    matrix[mask][c] = 0             # Update the mask.  
            if clear:
                matrix[r] = [0] * width             # Clear the current line which has 0
        if mask == -1:                              # In case of no 0 at all
            return
        for r in range(high):
            for c in range(width):                  # Use mask to do 'and' with each line
                matrix[r][c] = matrix[mask][c] and matrix[r][c]
        matrix[mask] = [0] * width                  # Clear the mask line
