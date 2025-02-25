with open("data.txt",'r') as file:
    result = 0
    for line in file:
        game = line.split(": ",1)[1].replace(";",",").replace('\n','')
        cubes = game.split(', ')
        red = 0
        blue = 0
        green = 0
        for color in cubes:
            pair = color.split(' ')
            if pair[1] == "red" and int(pair[0]) > red:
                red = int(pair[0])
            elif pair[1] == "green" and int(pair[0]) > green:
                green = int(pair[0])
            elif pair[1] == "blue" and int(pair[0]) > blue:
                blue = int(pair[0])    
        result+=(red*green*blue)
    print(result)