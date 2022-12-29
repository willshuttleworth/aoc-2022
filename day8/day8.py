def is_visible(i, j):
    # if (i == 0 or j == 0) or (i == (len(grid) - 1) or j == len(grid[i]) - 1):
        # return True
    
    from_top = True
    top_score = 0
    for k in range(i - 1, -1, -1):
        top_score = top_score + 1
        if grid[k][j] >= grid[i][j]:
            from_top = False
            break
    
    from_bottom = True
    bottom_score = 0
    for k in range(i + 1, len(grid)):
        bottom_score = bottom_score + 1
        if grid[k][j] >= grid[i][j]:
            from_bottom = False 
            break
    
    from_left = True
    left_score = 0
    for k in range(j - 1, -1, -1):
        left_score = left_score + 1
        if grid[i][k] >= grid[i][j]:
            from_left = False 
            break
    
    from_right = True
    right_score = 0
    for k in range(j + 1, len(grid[i])):
        right_score = right_score + 1
        if grid[i][k] >= grid[i][j]:
            from_right = False 
            break
    
    return top_score * bottom_score * left_score * right_score
    # return from_top or from_bottom or from_left or from_right



f = open('input.txt')
lines = f.readlines()

grid = [[None] * (len(lines[0]) - 1) for i in range(len(lines))]
for i in range(len(lines)):
    for j in range(len(lines[i]) - 1):
        grid[i][j] = int(lines[i][j])

num_visible = 0
scores = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if is_visible(i, j):
            # num_visible = num_visible + 1
            scores.append(is_visible(i, j))

print(max(scores))
# print(num_visible)


