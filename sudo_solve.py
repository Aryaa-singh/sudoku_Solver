import numpy as np # IMPORT NUMPY TO USE MATRIX FUNCTIONALITY 

suduko = []
print("Please use 0 in place of blank spaces")
for i in range(9): # INPUT THE VALUES OF SUDOKU BOARD
    row = list(input("Enter the elements of row {} without any spaces and commas: ".format(i+1)))
    row = [int(i) for i in row]
    suduko.append(row)

print("GIVEN SUDOKU") 
print(np.matrix(suduko)) # PRINT GIVEN INPUT INFORM OF MATRIX USING NUMPY
print("\n")

def isValid(row,col,num):  # CHECK IF NUMBER INSERTED AT SUDOKU[ROW][COL] IS VALID OR NOT
    global suduko
    for i in range(0,9):
        if suduko[row][i] == num:
            return False    
        if suduko[i][col] == num:
            return False
        if suduko[3*(row//3) + i//3][3*(col//3) + i%3] == num:
            return False
    return True

def solve(): # CHECK ALL NUMS IN RANGE(1,10) TO FILL AT EMPTY CELLS
    for row in range(0,9):
        for col in range(0,9):
            if suduko[row][col] == 0:
                for num in range(1,10):
                    if isValid(row,col,num):
                        suduko[row][col] = num
                        solve()
                        suduko[row][col] = 0
                return      
    print(np.matrix(suduko)) # PRINT SOLVED SUDOKU 
    print("\n")
print("All possibles solutions are \n")
solve() # CALL SOLVE FUNCTION TO SOLVE SUDOKU