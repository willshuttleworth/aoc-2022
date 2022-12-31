def check_cycle():
    if cycle_count in cycles:
        strenghts.append(x * cycle_count)

def draw(screen):
    positions = [x - 1, x, x + 1]
    print(positions, cycle_count)

    if cycle_count % 40 in positions:
        screen = screen + "#"
    else:
        screen = screen + "."
    return screen

f = open('input.txt')

# cycles = [20, 60, 100, 140, 180, 220]
cycle_count = 0
x = 1
# strenghts = []
screen = ""
screen = draw(screen)
for line in f:
    l = line.split()
    if l[0] == 'noop':
        cycle_count = cycle_count + 1
        screen = draw(screen)
        # check_cycle()

    elif l[0] == 'addx':
        cycle_count = cycle_count + 1
        screen = draw(screen)
        # check_cycle()
        cycle_count = cycle_count + 1
        x = x + int(l[1])
        screen = draw(screen)
        # check_cycle()
    
# print(sum(strenghts))
for i in range(0, 240):
    if i % 41 == 0:
        screen = screen[:i] + '\n' + screen[i:]
print(screen)
