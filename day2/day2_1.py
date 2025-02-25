with open("data.txt",'r') as file:
    result = 0
    i = 1
    for line in file:
        game = line.split(": ",1)[1].replace(";",",").replace('\n','')
        cubes = game.split(', ')
        state = 0
        for color in cubes:
            pair = color.split(' ')
            if pair[1] == "red" and int(pair[0]) >12:
                state = 1
                break
            elif pair[1] == "green" and int(pair[0]) >13:
                state = 1
                break
            elif pair[1] == "blue" and int(pair[0]) >14:
                state = 1
                break 
            
        if state !=1:
            result+=i
        i+=1
    print(result)