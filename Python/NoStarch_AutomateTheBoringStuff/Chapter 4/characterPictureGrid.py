def printGrid(inputGrid):
    for y in range(len(inputGrid)):
        for x in range(len(inputGrid[y])):
            print (inputGrid[y][x], end=' ')
        print()

def printGridRotate(inputGrid):
    for y in range(len(inputGrid[0])):
        for x in range(len(inputGrid)):
            print (inputGrid[x][y], end=' ')
        print()

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

printGrid(grid)
print()
printGridRotate(grid)