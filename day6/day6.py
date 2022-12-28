f = open("input.txt", 'r')
line = f.readlines()[0]

""" part1
for i in range(len(line) - 3):
    four = []
    index = 0
    for j in range(4):
        print(four)
        if line[i + j] in four:
            print("in")
            index = j
            break
        else:
            print("not in")
            four.append(line[i + j])
    if(len(four)) == 4:
        print(i + 4)
        exit()
"""

for i in range(len(line) - 14):
    fourteen = []
    for j in range(14):
        if line[i + j] in fourteen:
            print("in")
            break
        else:
            print("not in")
            fourteen.append(line[i + j])
    if(len(fourteen)) == 14:
        print(i + 14)
        exit()
