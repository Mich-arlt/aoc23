import numpy as np
from collections import deque
with open("data.txt",'r') as file:
    lines = [line.strip() for line in file.readlines()]
    pipe_map = np.array([list(line) for line in lines])
    place  = np.where(pipe_map == "S")
    place = (place[0][0],place[1][0])
    old_place = place
    left_dots = []
    right_dots = []
    all_way = []
    all_way.append(place)

    if place[0]-1 >=0 and pipe_map[place[0]-1][place[1]] in ["|","F","7"]:
        left_dots.append((place[0],place[1]-1))
        right_dots.append((place[0],place[1]+1))
        place = (place[0]-1,place[1])
    elif place[1]-1 >=0 and pipe_map[place[0]][place[1]-1] in ["L","F","-"]:
        left_dots.append((place[0]+1,place[1]))
        right_dots.append((place[0]-1,place[1]+1))
        place = (place[0],place[1]-1)
    elif place[0]+1 <= pipe_map.shape[0] and pipe_map[place[0]+1][place[1]] in ["|","L","J"]:
        right_dots.append((place[0],place[1]-1))
        left_dots.append((place[0],place[1]+1))
        place = (place[0]+1,place[1])
    elif place[1]+1 <= pipe_map.shape[1] and pipe_map[place[0]][place[1]+1] in ['J',"7",'-']:
        left_dots.append((place[0]-1,place[1]))
        right_dots.append((place[0]+1,place[1]))
        place = (place[0],place[1]+1)
    steps = 1
    
    
    while pipe_map[place[0]][place[1]] != "S":
        all_way.append(place)
        steps+=1
        if pipe_map[place[0]][place[1]] == "|":
            if (place[0]+1,place[1]) != old_place:
                if place[1]+1 < pipe_map.shape[1]:
                    left_dots.append((place[0],place[1]+1))
                if place[1]-1 >=0:
                    right_dots.append((place[0],place[1]-1))
                old_place = place
                place = (place[0]+1,place[1])
            else:
                if place[1]+1 < pipe_map.shape[1]:
                    right_dots.append((place[0],place[1]+1))
                if place[1]-1 >=0:
                    left_dots.append((place[0],place[1]-1))
                old_place = place
                place = (place[0]-1,place[1])
        elif pipe_map[place[0]][place[1]] == "L":
            if (place[0]-1,place[1]) != old_place:
                if place[0]+1 < pipe_map.shape[0]:
                    left_dots.append((place[0]+1,place[1]))
                if place[1]-1 >=0:
                    left_dots.append((place[0],place[1]-1))
                old_place = place
                place = (place[0]-1,place[1])
            else:
                if place[0]+1 < pipe_map.shape[0]:
                    right_dots.append((place[0]+1,place[1]))
                if place[1]-1 >=0:
                    right_dots.append((place[0],place[1]-1))
                old_place = place
                place = (place[0],place[1]+1)
               
        elif pipe_map[place[0]][place[1]] == "F":
            if (place[0]+1,place[1]) != old_place:
                if place[0]-1 >=0:
                    right_dots.append((place[0]-1,place[1]))
                if place[1]-1 >=0:
                    right_dots.append((place[0],place[1]-1))
                old_place = place
                place = (place[0]+1,place[1])
            else:
                if place[0]-1 >=0:
                    left_dots.append((place[0]-1,place[1]))
                if place[1]-1 >=0:
                    left_dots.append((place[0],place[1]-1))
                old_place = place
                place = (place[0],place[1]+1)   
        elif pipe_map[place[0]][place[1]] == "J":
            if (place[0]-1,place[1]) != old_place:
                if place[0]+1 < pipe_map.shape[0]:
                    right_dots.append((place[0]+1,place[1]))
                if place[1]+1 < pipe_map.shape[1]:
                    right_dots.append((place[0],place[1]+1))
                old_place = place
                place = (place[0]-1,place[1])
            else:
                if place[0]+1 < pipe_map.shape[0]:
                    left_dots.append((place[0]+1,place[1]))
                if place[1]+1 < pipe_map.shape[1]:
                    left_dots.append((place[0],place[1]+1))
                old_place = place
                place = (place[0],place[1]-1) 
        elif pipe_map[place[0]][place[1]] == "7":
            if (place[0]+1,place[1]) != old_place:
                if place[0]-1 >=0:
                    left_dots.append((place[0]-1,place[1]))
                if place[1]+1 < pipe_map.shape[1]:
                    left_dots.append((place[0],place[1]+1))
                old_place = place
                place = (place[0]+1,place[1])
            else:
                if place[0]-1 >=0:
                    right_dots.append((place[0]-1,place[1]))
                if place[1]+1 < pipe_map.shape[1]:
                    right_dots.append((place[0],place[1]+1))
                old_place = place
                place = (place[0],place[1]-1)   
        elif pipe_map[place[0]][place[1]] == "-":
            if (place[0],place[1]-1) != old_place:
                
                if place[0]+1 < pipe_map.shape[0]:
                    left_dots.append((place[0]+1,place[1]))
                if place[0]-1 >=0:
                    right_dots.append((place[0]-1,place[1]))
                old_place = place
                place = (place[0],place[1]-1)
            else:
                if place[0]+1 < pipe_map.shape[0]:
                    right_dots.append((place[0]+1,place[1]))
                if place[0]-1 >=0:
                    left_dots.append((place[0]-1,place[1]))
                old_place = place
                place = (place[0],place[1]+1)
    
    ms = 0
    os = 0
    
    for q in range(pipe_map.shape[0]):
        for k in range(pipe_map.shape[1]):
            if (q,k) in left_dots and (q,k) not in all_way:
                pipe_map[q][k] = "m"
                ms+=1
            elif (q,k) in right_dots and (q,k) not in all_way:
                pipe_map[q][k] = "o"
                os+=1
                
    def flood_fill(r, c,loop):
        queue = deque([(r, c)])
        enclosed.add((r, c))
        is_enclosed = True
        area = 1
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < loop.shape[0] and 0 <= ny < loop.shape[1]:
                    if loop[nx][ny] == 'm':
                        continue
                    if (nx, ny) not in enclosed and loop[nx][ny] != "m":
                        enclosed.add((nx, ny))
                        queue.append((nx, ny))
                        area += 1
                else:
                    is_enclosed = False 
        return area if is_enclosed else 0
    
    enclosed = set()
    enclosed_areas = 0
    for r in range(pipe_map.shape[0]):
        for c in range(pipe_map.shape[1]):
            if pipe_map[r][c] != 'm' and (r, c) not in enclosed:
                enclosed_areas += flood_fill(r, c,pipe_map)
    print(ms+enclosed_areas)