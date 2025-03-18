import re

def find_shortest_path(p1,p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

with open("data.txt") as file:
    cosmap = []
    galaxies = set()
    for line in file:
        if "#" not in line:
            cosmap.append(list(line.replace("\n","")))
            cosmap.append(list(line.replace("\n","")))
        else:
            galaxies.add(line.find("#",))
            for m in re.finditer("#",line):
                galaxies.add(m.start())
            cosmap.append(list(line.replace("\n","")))
    temp = []
    for row in cosmap:
        new_row = []
        for i, val in enumerate(row):
            new_row.append(val)
            if i not in galaxies:
                new_row.append(".")
        temp.append(new_row)
    cosmap = temp

galaxies = []

rows = len(cosmap)
cols = len(cosmap[0])

for i in range(rows):
    for j in range(cols):
        if cosmap[i][j] == "#":
            galaxies.append((i,j))
result = 0

for i in range(len(galaxies)):
    for j in range(i+1,len(galaxies)):
        result+=find_shortest_path(galaxies[i],galaxies[j])


print(result)
