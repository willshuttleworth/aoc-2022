class Node:
    
    def __init__(self, parent, name, size):
        self.size = size
        self.name = name
        self.parent = parent
        self.children = []
    
    def addchild(self, child):
        self.children.append(child) 

    def getdirsize(self):
        total = 0
        for child in self.children:
            if child.size is not None:
                total = total + child.size
            else:
                total = total + child.getdirsize()
        return total


dirs = []
# build up tree, keep pointer to all dirs, write a recursive function to find size of each dir in list
"""
test = Node(None, 'dir_a', None)
test.addchild(Node(test, 'file_a', 100))
print(test.size)
print(test.children[0].name, test.children[0].size)
"""
f = open('input.txt')
lines = f.readlines()
root = Node(None, '/', None)
curr = root
dirs.append(curr)
for i in range(1, len(lines)):
    # possible commands (command line starts with '$'):
    #   cd `dir`: make curr point to `dir`
    #   cd .. : make curr point to curr's parent
    #   ls: read line by line until `$` at first char, adding each entry as a child of curr
    line = lines[i].split()
    if line[1] == 'ls':
        i = i + 1
        line = lines[i].split()
        while line[0] != '$':
            if line[0] == 'dir':
                child = Node(curr, line[1], None)
                dirs.append(child)
                curr.addchild(child)
            else:
                child = Node(curr, line[1], int(line[0]))
                curr.addchild(child)
            if i < len(lines) - 1:
                i = i + 1
                line = lines[i].split()
            else:
                break

    elif line[1] == 'cd' and line[2] == '..':
        curr = curr.parent
    elif line[1] == 'cd':
        direc = line[2]
        for child in curr.children:
            if child.name == direc:
                curr = child
                break
total = 0
for direc in dirs:
    size = direc.getdirsize()
    if size <= 100000:
        total = total + size
print(total)

excess = 30000000 - (70000000 - root.getdirsize())
options = {}
for direc in dirs:
    size = direc.getdirsize()
    if size > excess:
        options[direc] = size
print(min(options, key=options.get).getdirsize())

