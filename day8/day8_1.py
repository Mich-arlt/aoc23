with open("data.txt",'r') as file:
    desert_map = {}
    way = ""
    way_state = True
    for line in file:
        if way_state:
            way_state = False
            way = line.replace("\n","")
        elif len(line)>3:
            line = line.split(" = ")
            code = line[0]
            val = tuple(line[1].replace("\n","")[1:-1].split(", "))
            desert_map[code] = val
    map_point = "AAA"
    steps = 0
    l = len(way)-1
    i=0
    while True:
        steps+=1
        w = way[i]
        if w == "L":
            map_point = desert_map[map_point][0]
        if w == "R":
            map_point = desert_map[map_point][1]
        if map_point == "ZZZ":
            break
        if i == l:
            i = 0
        else:
            i+=1
    print(steps)