f = open("input.txt", 'r')
lines = f.readlines()

stacks = []
for i in range(9):
    stacks.append([])

for i in range(7, -1, -1):
    line = lines[i].split(' ')
    j = 0
    k = 0
    while k < len(line):
        if line[k] != '':
            stacks[j].append(line[k][1])
            k = k + 1
        else:
            k = k + 4
        j = j + 1

""" part1
for i in range(10, len(lines)):
    # 1, 3, 5
    # count, src, dst
    line = lines[i].split()
    count = int(line[1])
    src = int(line[3])
    dst = int(line[5])
    for j in range(count):
        if(len(stacks[src - 1]) > 0):
            mov = stacks[src - 1].pop()
            stacks[dst - 1].append(mov)
"""

for i in range(10, len(lines)):
    # 1, 3, 5
    # count, src, dst
    line = lines[i].split()
    count = int(line[1])
    src = int(line[3])
    dst = int(line[5])
    mov = []
    for j in range(count):
        if(len(stacks[src - 1]) > 0):
            mov.insert(0, stacks[src - 1].pop())
    for j in range(len(mov)):
        stacks[dst - 1].append(mov[j])

for i in range(9):
    print(stacks[i][len(stacks[i]) - 1])
