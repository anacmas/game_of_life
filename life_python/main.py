import copy

line = []
grid = []
size = 20

dead = '-'
alive = '#'

for i in range(0, size+1):
    line.append(dead)

i = 0

while i < len(line):
    grid.append(line.copy())
    i += 1

line_number = 5
column_number = 3

grid[line_number][column_number] = alive
grid[line_number - 1][column_number] = alive
grid[line_number + 1][column_number] = alive
grid[line_number][column_number + 1] = alive
grid[line_number][column_number + 2] = alive
grid[line_number][column_number + 3] = alive


#rules 
def check_neighbors(i, j):
    neighbors = 0
    if (i !=0) and (j != 0):
        if grid[i-1][j-1] == alive: neighbors += 1

    if (i != 0):
        if grid[i-1][j] == alive: neighbors += 1
    
    if (j != 0):
        if grid[i][j-1] == alive: neighbors += 1
    
    if (i != size) and (j != size):
        if grid[i+1][j+1] == alive: neighbors += 1

    if (i != size):
        if grid[i+1][j] == alive: neighbors += 1

    if (j != size):
        if grid[i][j+1] == alive: neighbors += 1

    if (i != 0 and j != size):
        if grid[i-1][j+1] == alive: neighbors += 1
    
    if (i != size and j != 0):
        if grid[i+1][j-1] == alive: neighbors += 1


    return neighbors

def mutate_cells(i, j):
    is_dead = grid[i][j] == dead

    neighbors = check_neighbors(i, j)

    if is_dead:
        if neighbors == 3:
            return alive

        else:
            return dead
    
    if neighbors <= 1 or neighbors >= 4:
        return dead

    return alive 

def create_new_cycle():
    gridCopy = copy.deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            gridCopy[i][j] = mutate_cells(i, j)
    return gridCopy        

def print_matrix():
    c = 0

    while c < len(grid):
        l = 0
        while l < len(grid[c]):
            print(grid[c][l], end='')
            l+=1
        print()
        c+=1

print_matrix()


game = input('Aperte enter para gerar ou continuar um ciclo ou digite sair para encerrar ').lower()

while game != 'sair':
    grid = create_new_cycle()
    print_matrix()
    game = input('Aperte enter para gerar um novo ciclo ou digite sair para encerrar ')



