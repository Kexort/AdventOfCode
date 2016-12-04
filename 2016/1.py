import re

input = "R1, R3, L2, L5, L2, L1, R3, L4, R2, L2, L4, R2, L1, R1, L2, R3, L1, L4, R2, L5, R3, R4, L1, R2, L1, R3, L4, R5, L4, L5, R5, L3, R2, L3, L3, R1, R3, L4, R2, R5, L4, R1, L1, L1, R5, L2, R1, L2, R188, L5, L3, R5, R1, L2, L4, R3, R5, L3, R3, R45, L4, R4, R72, R2, R3, L1, R1, L1, L1, R192, L1, L1, L1, L4, R1, L2, L5, L3, R5, L3, R3, L4, L3, R1, R4, L2, R2, R3, L5, R3, L1, R1, R4, L2, L3, R1, R3, L4, L3, L4, L2, L2, R1, R3, L5, L1, R4, R2, L4, L1, R3, R3, R1, L5, L2, R4, R4, R2, R1, R5, R5, L4, L1, R5, R3, R4, R5, R3, L1, L2, L4, R1, R4, R5, L2, L3, R4, L4, R2, L2, L4, L2, R5, R1, R4, R3, R5, L4, L4, L5, L5, R3, R4, L1, L3, R2, L2, R1, L3, L5, R5, R5, R3, L4, L2, R4, R5, R1, R4, L3"

x = 0
y = 0

direction = 0

map = []

for string in input.split(", "):

    if string[0] == "R":
        direction = (direction + 1) % 4
    else:
        direction = (4 + direction - 1) % 4

    len = int(re.search(r'\d+', string).group())
    if direction == 0:
        for i in xrange(0,len):
            y += 1
            if (x,y) in map:
                print x,y
            map.append((x,y))
    elif direction == 1:
        for i in xrange(0,len):
            x += 1
            if (x,y) in map:
                print x,y
            map.append((x,y))
    elif direction == 2:
        for i in xrange(0,len):
            y -= 1
            if (x,y) in map:
                print x,y
            map.append((x,y))
    elif direction == 3:
        for i in xrange(0,len):
            x -= 1
            if (x,y) in map:
                print x,y
            map.append((x,y))



    


