import numpy as np
from collections import defaultdict

with open("data.txt",'r') as file:
    lines = [line.strip() for line in file.readlines()]
    engine_map = np.array([list(line) for line in lines])
    # print(engine_map)
    result_dict = defaultdict(lambda: [1, 0])
    result = 0
    number = ''
    state = False
    star_place = None
    for i in range(engine_map.shape[0]):
        for j in range(engine_map.shape[0]):
            if engine_map[i][j].isdigit():
                if i-1 >=0 and not engine_map[i-1][j].isdigit() and engine_map[i-1][j] != '.':
                    state = True
                    if engine_map[i-1][j] =='*':
                        star_place = (i-1,j)
                if j-1 >=0 and not engine_map[i][j-1].isdigit() and engine_map[i][j-1] != '.':
                    state = True
                    if engine_map[i][j-1] =='*':
                        star_place = (i,j-1)
                if i+1 <engine_map.shape[0] and not engine_map[i+1][j].isdigit() and engine_map[i+1][j] != '.':
                    state = True
                    if engine_map[i+1][j] =='*':
                        star_place = (i+1,j)
                if j+1 <engine_map.shape[0] and not engine_map[i][j+1].isdigit() and engine_map[i][j+1] != '.':
                    state = True
                    if engine_map[i][j+1] =='*':
                        star_place = (i,j+1)
                if i-1 >= 0 and j-1 >= 0 and not engine_map[i-1][j-1].isdigit() and engine_map[i-1][j-1] != '.':
                    state = True
                    if engine_map[i-1][j-1] =='*':
                        star_place = (i-1,j-1)
                if i+1 < engine_map.shape[0] and j-1 >= 0 and not engine_map[i+1][j-1].isdigit() and engine_map[i+1][j-1] != '.':
                    state = True
                    if engine_map[i+1][j-1] =='*':
                        star_place = (i+1,j-1)
                if i-1 >= 0 and j+1 < engine_map.shape[0] and not engine_map[i-1][j+1].isdigit() and engine_map[i-1][j+1] != '.':
                    state = True
                    if engine_map[i-1][j+1] =='*':
                        star_place = (i-1,j+1)
                if i+1 < engine_map.shape[0] and j+1 < engine_map.shape[0] and not engine_map[i+1][j+1].isdigit() and engine_map[i+1][j+1] != '.':
                    state = True
                    if engine_map[i+1][j+1] =='*':
                        star_place = (i+1,j+1)
                number+=engine_map[i][j]  
            elif not engine_map[i][j].isdigit():
                if number != '' and state == True:
                    if star_place is not None:
                        result_dict[star_place][0] *= int(number)
                        result_dict[star_place][1] += 1
                    state = False
                    star_place = None
                number = ''
    for _,val in result_dict.items():
        if val[1] > 1:
            result+=val[0]      
    print(result)