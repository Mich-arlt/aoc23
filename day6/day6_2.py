with open("data.txt",'r') as file:
    lines = [line.strip() for line in file.readlines()]
    time =  int(lines[0].split(':')[1].replace(" ",""))
    distance =  int(lines[1].split(':')[1].replace(" ",""))
    ways = 0
    for j in range(time):
            if (time - j)*j > distance:
                ways +=1 
    
    print(ways)