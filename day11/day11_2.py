import re

def find_shortest_path(p1,p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

with open("data.txt") as file:
    cosmap = []
    galaxies_rows = set()
    galaxies_cols = set()
    for i,line in enumerate(file):
        if "#" not in line:
            galaxies_rows.add(i)
            cosmap.append(list(line.replace("\n","")))
        else:
            for m in re.finditer("#",line):
                galaxies_cols.add(m.start())
            cosmap.append(list(line.replace("\n","")))
galaxies = []

rows = len(cosmap)
cols = len(cosmap[0])

for i in range(rows):
    for j in range(cols):
        if cosmap[i][j] == "#":
            temp_i = i
            temp_j = j
            for x in galaxies_rows:
                if x < i:
                    temp_i+=999999
            all_numbers = set(range(cols))
            miss = all_numbers - galaxies_cols
            for y in miss:
                if y < j:
                    temp_j+=999999      
            
            galaxies.append((temp_i,temp_j))
result = 0

for i in range(len(galaxies)):
    for j in range(i+1,len(galaxies)):
        result+=find_shortest_path(galaxies[i],galaxies[j])


print(result)
