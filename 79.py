class Solution:
    def add_boundary(self, matrix):
        # Determine the size of the original matrix
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0

        # Create a new matrix with additional boundary
        new_matrix = [[' ' for _ in range(cols + 2)] for _ in range(rows + 2)]

        # Copy the original matrix into the center of the new matrix
        for i in range(rows):
            for j in range(cols):
                new_matrix[i + 1][j + 1] = matrix[i][j]

        return new_matrix

    def search(self, board, word, i, j, c, oi, oj ):
        print(c,"c")
        if c == len(word):
            return True
        if board[i+1][j] == word[c] and oi != i + 1:
            oi = i
            oj = j
            i += 1
            c += 1
            
            self.search( board, word, i, j, c, oi, oj)
        if board[i-1][j] == word[c] and oi != i - 1:
            oi = i
            oj = j
            i -= 1
            c += 1
            self.search( board, word, i, j, c, oi, oj)
        if board[i][j+1] == word[c] and oj != j + 1:
            oi = i
            oj = j
            j += 1
            c += 1
            self.search( board, word, i, j, c, oi, oj)
        if board[i][j-1] == word[c] and oj != j - 1:
            oi = i
            oj = j
            j -= 1
            c += 1
            self.search( board, word, i, j, c, oi, oj)
    

    def exist(self, board: List[List[str]], word: str) -> bool:
        
        board = self.add_boundary(board)
        c = 1
        oi = -1
        oj = -1
        print(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    if self.search( board, word, i, j, c, oi, oj) == True:
                        return True
        return False
