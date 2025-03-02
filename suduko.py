#===========================================================================
def check_number(gride,row,column,number):
        if number in gride[row]:
                return False
        for x in range(9):
                if gride[x][column]==number:
                        return False
        corner_row = row-(row%3)
        corner_column=column-(column%3)
        for x in range(3):
                for y in range(3):
                    if gride[corner_row+x][corner_column+y]==number:
                        return False 
        return True
#===========================================================================
def solving(gride,row,column):
    if column==9:
        if row==8:
            return True
        else:
            row+=1
            column=0
    if gride[row][column]>0:
        return solving(gride,row,column+1)
    for number in range(1,10):
        if check_number(gride,row,column,number):
            gride[row][column]=number
            if solving(gride,row,column+1):
                return True
        gride[row][column]=0
    return False
#===========================================================================
def Sudoku(table):
    if solving(table,0,0):
        for i in range(9):
            for j in range(9):
                print(table[i][j],end=" ")
            print("\n")
    else:
        return "No,solution for this Sudoku"
#===========================================================================
table =[[0,0,0,0,6,0,0,0,0],
        [0,0,3,9,0,1,0,4,0],
        [2,0,0,0,0,0,0,0,7],
        [0,0,0,0,8,0,0,5,0],
        [0,0,6,0,4,0,0,0,0],
        [3,0,0,5,0,6,2,0,0],
        [0,0,1,3,0,5,0,9,0],
        [0,0,0,8,0,0,0,0,0],
        [0,9,0,0,0,0,4,0,3]]
print(Sudoku(table))