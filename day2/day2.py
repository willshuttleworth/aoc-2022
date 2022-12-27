with open('input.txt') as f:
    lines = f.readlines()

table = {'X': 'A', 'Y': 'B', 'Z': 'C'}
points = {'A': 1, 'B': 2, 'C': 3}
total = 0
for line in lines:
    if line != '\n': 
        chars = line.split()
        yours = table.get(chars[1]).strip()
        theirs = chars[0].strip()
        print(yours + ' ' + theirs)
        total = total + points.get(yours)
        print(points.get(yours))
        if yours == theirs:
            total = total + 3
        elif yours == 'A' and theirs == 'C':
            total = total + 6
        elif yours == 'B' and theirs == 'A':
            total = total + 6
        elif yours == 'C' and theirs == 'B':
            total = total + 6
print(total)
