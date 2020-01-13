gameBoard = []

# ===============================================
# Insert your values for your grid here
gameBoard.append([0,0,0,2,0,0,8,4,0])
gameBoard.append([3,0,0,5,0,0,6,0,1])
gameBoard.append([7,0,9,0,0,1,0,0,2])
gameBoard.append([0,1,0,0,9,0,5,0,0])
gameBoard.append([0,0,0,0,0,0,0,0,0])
gameBoard.append([0,0,3,0,5,0,0,2,0])
gameBoard.append([8,0,0,7,0,0,2,0,6])
gameBoard.append([6,0,5,0,0,4,0,0,8])
gameBoard.append([0,3,1,0,0,8,0,0,0])
# ==================================================

def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

# ------- helper methods------ 
def  checkRow(arr, row, num):
    # if (num in arr[row]):
    #     return True

    # return False
    for i in range(9): 
        if(arr[row][i] == num): 
            return True
    return False
  

def checkColumn(arr, col, num):
    # for row in arr:
    #     if (row[col] == num):
    #         return True
    
    # return False
    for i in range(9): 
        if(arr[i][col] == num): 
            return True
    return False

# checks if num is contained in the corresponding box
def checkBox(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if (arr[row+i][col+j] == num):
                return True

    return False

# determines if a possible num can be assigned
def isValid(arr, row, col, num):
    # returns true if the grid is valid
    return not checkRow(arr,row,num) and not checkColumn(arr,col,num) and not checkBox(arr,row - row%3,col - col%3,num)


# finds unassigned grid
def findEmpty(arr, l):
    for row in range(9):
        for col in range(9):
            if(arr[row][col] == 0):
                l[0] = row
                l[1] = col
                return True

    return False


# ---- final recursion backtracking algo ----- 
def sudokuSolve(board):
    # "l" is used to register the "findEmpty" record of info
    l = [0,0]

    # base case
    if(not findEmpty(board,l)):
        return True

    # initial assignment to for row and col
    row = l[0]
    col = l[1]

    for num in range(1,10):
        if(isValid(board,row,col,num)):
            # if the number has a possibility of being correct, use it
            board[row][col] = num

            if(sudokuSolve(board)):
                return True

        # if the previous logic isn't true, that means it was unsuccesful, so we reset the grid position and try again
        # change the grid position back to zero
            board[row][col] = 0

    return False


printBoard(gameBoard)
print("\n===============Solved=====================")

if(sudokuSolve(gameBoard)):
    printBoard(gameBoard)
else:
    print("No solution")



