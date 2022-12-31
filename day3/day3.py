# read line by line
# split line in half, make two separate substrings
# read first half, put each character into dict
# read second, check if that character is in dict, stop and save it if it is
# do some ascii calculation thing to get value
# sum up values

def val(char):
    if(char.isupper()):
        return ord(char) - 38
    else:
        return ord(char) - 96
    return 0

f = open("day3input.txt", 'r')
lines = list(f)
f.close()

f = open("day3input.txt", 'r')

sum = 0

for line in f:
    part1 = line[0:len(line) // 2]
    part2 = line[len(line) // 2:len(line)]

    chars = {}
    for char in part1:
        chars[char] = True
    for char in part2:
        if chars.get(char) is True:
            sum += val(char)
            break
print(sum) 

sum2 = 0
for i in range(0, len(lines) - 2, 3):
    # find characters shared between first two lines
    # find only character in line 3 that is also shared between first two
    chars = {}
    chars2 = {}
    for char in lines[i]:
        chars[char] = True
    for char in lines[i + 1]:
        if chars.get(char) is True:
            chars2[char] = True
    for char in lines[i + 2]:
        if chars2.get(char) is True:
            sum2 += val(char)
            break
    i = i + 2

print(sum2)

f.close()

