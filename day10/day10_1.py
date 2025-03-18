import numpy as np
with open("data.txt",'r') as file:
    lines = [line.strip() for line in file.readlines()]
    pipe_map = np.array([list(line) for line in lines])
    place  = np.where(pipe_map == "S")
    place = (place[0][0],place[1][0])
    old_place = place
    print(place)
    if place[0]-1 >=0 and pipe_map[place[0]-1][place[1]] in ["|","L","F","J","7","-"]:
        place = (place[0]-1,place[1])
    elif place[1]-1 >=0 and pipe_map[place[0]][place[1]-1] in ["|","L","F","J","7","-"]:
        place = (place[0],place[1]-1)
    elif place[0]+1 <= pipe_map.shape[0] and pipe_map[place[0]+1][place[1]] in ["|","L","F","J","7","-"]:
        place = (place[0]+1,place[1])
    elif place[1]+1 <= pipe_map.shape[0] and pipe_map[place[0]][place[1]+1] in ["|",'L',"F,'J,'7",'-']:
        place = (place[0],place[1]+1)
    steps = 1
    while pipe_map[place[0]][place[1]] != "S":
        steps+=1
        # print(pipe_map[place[0]][place[1]])
        if pipe_map[place[0]][place[1]] == "|":
            if (place[0]+1,place[1]) != old_place:
                old_place = place
                place = (place[0]+1,place[1])
            else:
                old_place = place
                place = (place[0]-1,place[1])
        elif pipe_map[place[0]][place[1]] == "L":
            if (place[0]-1,place[1]) != old_place:
                old_place = place
                place = (place[0]-1,place[1])
            else:
                old_place = place
                place = (place[0],place[1]+1)   
        elif pipe_map[place[0]][place[1]] == "F":
            if (place[0]+1,place[1]) != old_place:
                old_place = place
                place = (place[0]+1,place[1])
            else:
                old_place = place
                place = (place[0],place[1]+1)   
        elif pipe_map[place[0]][place[1]] == "J":
            if (place[0]-1,place[1]) != old_place:
                old_place = place
                place = (place[0]-1,place[1])
            else:
                old_place = place
                place = (place[0],place[1]-1)   
        elif pipe_map[place[0]][place[1]] == "7":
            if (place[0]+1,place[1]) != old_place:
                old_place = place
                place = (place[0]+1,place[1])
            else:
                old_place = place
                place = (place[0],place[1]-1)   
        elif pipe_map[place[0]][place[1]] == "-":
            if (place[0],place[1]-1) != old_place:
                old_place = place
                place = (place[0],place[1]-1)
            else:
                old_place = place
                place = (place[0],place[1]+1)   
    print(steps/2)