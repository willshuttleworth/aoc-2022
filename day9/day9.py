# unbounded grid movement :O (not actually unbounded lol i just made grid big)
# well actually ill just make it a really big grid i guess
# one grid, keep track of seen positions, head and tail only needs coords remembered
# loop over each line in input file
    # first, move head to next position
    # then, move tail according to where head went
    # if new tail position isnt seen yet, mark it
# part2: basically snake 
    # keep two arrays, one of ropes x positions and another of ropes y positions
    # move head, then call move tail on every knot in rope

def move_tail(head_x, head_y, tail_x, tail_y):
    # diagonal cases
    if abs(head_x - tail_x) == 2 and (abs(head_y - tail_y) == 1 or abs(head_y - tail_y) == 2):
        if head_x > tail_x:
            tail_x = tail_x + 1
        else:
            tail_x = tail_x - 1
        if head_y > tail_y:
            tail_y = tail_y + 1
        else:
            tail_y = tail_y - 1
    elif abs(head_y - tail_y) == 2 and abs(head_x - tail_x) == 1:
        if head_x > tail_x:
            tail_x = tail_x + 1
        else:
            tail_x = tail_x - 1
        if head_y > tail_y:
            tail_y = tail_y + 1
        else:
            tail_y = tail_y - 1
    # non diagonal cases
    elif head_x - tail_x == 2:
        tail_x = tail_x + 1
    elif head_x - tail_x == -2:
        tail_x = tail_x - 1
    elif head_y - tail_y == 2:
        tail_y = tail_y + 1
    elif head_y - tail_y == -2:
        tail_y = tail_y - 1
    return [tail_x, tail_y]
print(move_tail(0, 0, 2, 2))
f = open('input.txt')
lines = f.readlines()
seen = [[0] * 1000 for i in range(1000)]

head_x = 490
head_y = 490
# tail_x = 490
# tail_y = 490
seen[490][490] = 1

x_pos = [490 for i in range(9)]
y_pos = [490 for i in range(9)]

for line in lines:
    direction = line.split()[0]
    mag = int(line.split()[1])
    for i in range(mag):
        if direction == 'R':
            head_x = head_x + 1
        elif direction == 'L':
            head_x = head_x - 1 
        elif direction == 'U':
            head_y = head_y - 1 
        elif direction == 'D':
            head_y = head_y + 1 
        new_tail = move_tail(head_x, head_y, x_pos[0], y_pos[0])
        x_pos[0] = new_tail[0]
        y_pos[0] = new_tail[1]
        for j in range(1, 9):
            new_tail = move_tail(x_pos[j - 1], y_pos[j - 1], x_pos[j], y_pos[j])
            x_pos[j] = new_tail[0]
            y_pos[j] = new_tail[1]
        seen[x_pos[8]][y_pos[8]] = 1 

seen_total = 0
for i in range(1000):
    for j in range(1000):
        if seen[i][j] == 1:
            seen_total = seen_total + 1
print(seen_total)
