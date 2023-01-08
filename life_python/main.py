line = []
grid = []

for i in range(1, 11):
    line.append('X')

i = 0

while i < len(line):
    grid.append(line.copy())
    i += 1


coordinate_line = -1
coordinate_column = -1

while not (coordinate_line >= 1 and coordinate_line <= len(line)):
    coordinate_line = int(input("Escolha a linha onde sua celula vai começar, coloque um numero de 0 a " + str(len(line)) + ": "))
    
    if not (coordinate_line >= 1 and coordinate_line <= len(line)):
        print('Você digitou um caractere inválido')

while not (coordinate_column >= 1 and coordinate_column <= len(line)):
    coordinate_column =  int(input("Escolha a coluna onde sua celula vai começar, coloque um numero de 0 a " + str(len(line)) + ": "))

    if not (coordinate_column >= 1 and coordinate_column <= len(line)):
        print('Você digitou um caractere inválido')



if (coordinate_line >= 1 and coordinate_line <= len(line)) and (coordinate_column >= 1 and coordinate_column <= len(line)):

    grid[coordinate_line - 1][coordinate_column - 1] = '0'
    grid[coordinate_line - 2][coordinate_column - 1] = '0'
    grid[coordinate_line][coordinate_column - 1] = '0'
    grid[coordinate_line - 1][coordinate_column] = '0'
    grid[coordinate_line - 1][coordinate_column + 1] = '0'
    grid[coordinate_line - 1][coordinate_column + 2] = '0'
    grid[coordinate_line - 1][coordinate_column + 3] = '0'


c = 0

while c < len(grid):
    l = 0
    while l < len(grid[c]):
        print(grid[c][l], end='')
        l+=1
    print()
    c+=1


