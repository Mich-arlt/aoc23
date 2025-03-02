import re

with open("data.txt",'r') as file:
    lines = [line.strip() for line in file.readlines()]
    time =  list(map(int,re.findall(r'\d+', lines[0].split(':')[1])))
    distance =  list(map(int,re.findall(r'\d+', lines[1].split(':')[1])))
    ways = 0
    result = 1
    for i in range(len(time)):
        ways = 0
        for j in range(time[i]):
             if (time[i] - j)*j > distance[i]:
                ways +=1 
        result*=ways       
    print(result)