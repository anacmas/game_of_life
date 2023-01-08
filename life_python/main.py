line = []
grid = []

for i in range(1, 11):
    line.append('X')

i = 0

while i < len(line):
    grid.append(line.copy())
    i += 1


c = 0

while c < len(grid):
    l = 0
    while l < len(grid[c]):
        print(grid[c][l], end='')
        l+=1
    print()
    c+=1


