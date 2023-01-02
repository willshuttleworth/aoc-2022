import re

f = open('input.txt')

lines = f.readlines()
monkeys = [[] for i in range(len(lines) // 6)]
inspects = [0 for i in range(len(monkeys))]

j = 0
for i in range(1, len(lines), 7):
    nums = list(map(int, re.findall(r'\d+', lines[i])))
    monkeys[j] = nums
    j = j + 1

for i in range(10000): 
    j = 0
    monkey = 0
    while j < len(lines):
        j = j + 2
        line = lines[j].split()
        op = line[4] 
        mag = 0
        if line[5] != 'old':
            mag = int(line[5])
        else:
            mag = None
        j = j + 1
        inspects[monkey] = inspects[monkey] + len(monkeys[monkey])
        for num in monkeys[monkey]:
            val = 0
            if op == '+':
                val = num + mag
            else:
                if mag == None:
                    val = num * num
                else:
                    val = num * mag
            # val = val // 3
            val = val % 9699690
            if val % int(lines[j].split()[3]) == 0:
                # monkeys[monkey].remove(num)
                monkeys[int(lines[j + 1].split()[5])].append(val)
            else:
                # monkeys[monkey].remove(num)
                monkeys[int(lines[j + 2].split()[5])].append(val)
        j = j + 4
        monkeys[monkey] = []
        monkey = monkey + 1
    print(i)
print(inspects)
