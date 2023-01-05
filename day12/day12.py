class Tile:
    def __init__(self, row, col, steps):
        self.row = row
        self.col = col
        self.steps = steps

def isvalid(i, j):
    if (i >= 0 and i < len(grid)) and (j >= 0 and j < len(grid[0])) and [i, j] not in seen:
            return True
    return False

f = open('input.txt')
lines = f.readlines()

grid = [['' for i in range(len(lines[0]) - 1)] for i in range(len(lines))]

s = [] # position of start
q = [] # queue for bfs
seen = [] # list of all seen tiles

# loading grid
for i in range(len(lines)):
    for j in range(len(lines[0]) - 1):
        grid[i][j] = lines[i][j]
        if lines[i][j] == 'S':
            s.append(i)
            s.append(j)

curr = Tile(s[0], s[1], 0)
seen.append([curr.row, curr.col])
# add all a's to q
# north
if isvalid(curr.row - 1, curr.col):
    if grid[curr.row - 1][curr.col] == 'a':
        q.insert(0, Tile(curr.row - 1, curr.col, curr.steps + 1))
        seen.append([curr.row - 1, curr.col])

# east 
if isvalid(curr.row, curr.col + 1):
    if grid[curr.row][curr.col + 1] == 'a':
        q.insert(len(q), Tile(curr.row, curr.col + 1, curr.steps + 1))
        seen.append([curr.row, curr.col + 1])

# south 
if isvalid(curr.row + 1, curr.col):
    if grid[curr.row + 1][curr.col] == 'a':
        q.insert(len(q), Tile(curr.row + 1, curr.col, curr.steps + 1))
        seen.append([curr.row + 1, curr.col])

# west
if isvalid(curr.row, curr.col - 1):
    if grid[curr.row][curr.col - 1] == 'a':
        q.insert(len(q), Tile(curr.row, curr.col - 1, curr.steps + 1))
        seen.append([curr.row, curr.col - 1])

print('q:')
for tile in q:
    print(tile.row, tile.col, tile.steps)
print()

curr = q.pop(0)
    
steps = 0
while grid[curr.row][curr.col] != 'z':
    
    print(curr.row, curr.col)
    if curr.row == 19 and curr.col == 145:
        print('q:')
        for tile in q:
            print(tile.row, tile.col, tile.steps)
        print()
        
    """
    print('seen: ')
    for s in seen:
        print(s)
    print()
    """
    # add neighbors to queue(need to check n, s, e, w)
    # north (row - 1, col)
    if isvalid(curr.row - 1, curr.col):
        if ord(grid[curr.row - 1][curr.col]) - ord(grid[curr.row][curr.col]) <= 1 and grid[curr.row - 1][curr.col] != 'E':
            q.insert(len(q), Tile(curr.row - 1, curr.col, curr.steps + 1))
            seen.append([curr.row - 1, curr.col])

    # east  (curr.row, curr.col + 1)
    if isvalid(curr.row, curr.col + 1):
        if ord(grid[curr.row][curr.col + 1]) - ord(grid[curr.row][curr.col]) <= 1 and grid[curr.row][curr.col + 1] != 'E':
            q.insert(len(q), Tile(curr.row, curr.col + 1, curr.steps + 1))
            seen.append([curr.row, curr.col + 1])
    
    # south (curr.row + 1, curr.col)
    if isvalid(curr.row + 1, curr.col):
        if ord(grid[curr.row + 1][curr.col]) - ord(grid[curr.row][curr.col]) <= 1 and grid[curr.row + 1][curr.col] != 'E':
            q.insert(len(q), Tile(curr.row + 1, curr.col, curr.steps + 1))
            seen.append([curr.row + 1, curr.col])
    
    # west (curr.row, curr.col - 1)
    if isvalid(curr.row, curr.col - 1):
        if ord(grid[curr.row][curr.col - 1]) - ord(grid[curr.row][curr.col]) <= 1 and grid[curr.row][curr.col - 1] != 'E':
            q.insert(len(q), Tile(curr.row, curr.col - 1, curr.steps + 1))
            seen.append([curr.row, curr.col - 1])
    
    """
    print('q:')
    for tile in q:
        print(tile.row, tile.col, tile.steps)
    print()
    """

    curr = q.pop(0)
    steps = curr.steps
print(steps + 1)
