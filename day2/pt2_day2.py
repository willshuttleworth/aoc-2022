with open('input.txt') as f:
    lines = f.readlines()

table = {'X': 'A', 'Y': 'B', 'Z': 'C'}
points = {'A': 1, 'B': 2, 'C': 3}
total = 0
for line in lines:
    if line != '\n': 
        chars = line.split()
        yours = chars[1].strip()
        theirs = chars[0].strip()
        print(yours + ' ' + theirs)
        print(points.get(yours))
        if yours == 'X':
            if theirs == 'A':
                total = total + 3
            elif theirs == 'B':
                total = total + 1
            else:
                total = total + 2
            
        elif yours == 'Y':
            total = total + 3
            total = total + points.get(theirs)
            
        elif yours == 'Z':
            total = total + 6
            if theirs == 'A':
                total = total + 2
            elif theirs == 'B':
                total = total + 3
            else:
                total = total + 1
print(total)
