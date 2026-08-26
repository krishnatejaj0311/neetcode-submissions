class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check 1#no duplicates in any row
        #check 2#no duplicates in any column
        #in a (row,column) checks 1 and 2-3x3

        duplicates = []

        for i in range(0,len(board)):
            row = board[i]
            for j in range(len(row)):
                element = board[i][j]
                if element not in duplicates and element != '.':
                    duplicates.append(element)
                elif element == '.':
                    continue
                else:
                    return False
            duplicates = []
        
        for i in range(0,len(board)):
            row = board[i]
            for j in range(len(row)):
                element = board[j][i]
                if element not in duplicates and element != '.':
                    duplicates.append(element)
                elif element == '.':
                    continue

                else:
                    return False
            
            duplicates = []
        
        for i in range(0,len(board),3):
            for j in range(0,len(board),3):
                for inner_i in range(0, 3):
                    for inner_j in range(0, 3):
                        element = board[i+inner_i][j+inner_j]
                        if element not in duplicates and element != '.':
                            duplicates.append(element)
                        elif element == '.':
                            continue
                        else:
                            return False
                duplicates = []
        return True
