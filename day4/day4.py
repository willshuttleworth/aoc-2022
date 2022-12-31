total_overlaps = 0
partial_overlaps = 0

f = open("day4input.txt", 'r')

for line in f:
    line = line.strip()
    elves = line.split(',')
    range1 = elves[0].split('-')
    range1[0] = int(range1[0])
    range1[1] = int(range1[1])
    range2 = elves[1].split('-')
    range2[0] = int(range2[0])
    range2[1] = int(range2[1])
    if range1[0] <= range2[0] and range1[1] >= range2[1]:
        total_overlaps = total_overlaps + 1
    elif range2[0] <= range1[0] and range2[1] >= range1[1]:
        total_overlaps = total_overlaps + 1
    if range1[1] in range(range2[0], range2[1] + 1) or range1[0] in range(range2[0], range2[1] + 1):
        partial_overlaps = partial_overlaps + 1
    elif range2[1] in range(range1[0], range1[1] + 1) or range2[0] in range(range1[0], range1[1] + 1):
        partial_overlaps = partial_overlaps + 1

print(total_overlaps)
print(partial_overlaps)
