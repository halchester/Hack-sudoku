board = [
    [0,0,0,7,9,0,0,5,0], #if i % 3 then print ----- if j %3 then print |
    [3,5,2,0,0,8,0,4,0],
    [0,0,0,0,0,0,0,8,0],
    [0,1,0,0,7,0,0,0,4],
    [6,0,0,3,0,1,0,0,8],
    [9,0,0,0,8,0,0,1,0],
    [0,2,0,0,0,0,0,0,0],
    [0,4,0,5,0,0,8,9,1],
    [0,8,0,0,3,7,0,0,0]
]

#solving function here
def solve(bo):
    find = empty(bo)
    if not find:
        return True
    else:
        row, column = find
    for i in range(1,10):
        if valid(bo, i, (row, column)):
            bo[row][column] = i

            if solve(bo):   #recursively solving
                return True

            bo[row][column] = 0  #implementing backtrack to assure no missing spot

    return False

#check if the spot is valid or not
def valid(bo, num, pos):
    # for row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # for column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # for box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def show_board(bo):
    for row in range(len(bo)):
        if row % 3 == 0 and row != 0:
            print("-----------------------")

        for column in range(len(bo[0])):
            if column % 3 == 0 and column != 0:
                print("| ", end="")
            if column == 8:
                print(bo[row][column])
            else:
                print(str(bo[row][column]) + " ", end="")


def empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, column

    return None

#actually solving here
print("Before Solve : ")
show_board(board)
solve(board)
print()
print("After solve : ")
show_board(board)