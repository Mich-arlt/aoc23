from collections import defaultdict
with open("data.txt",'r') as file:
    lines = [line.strip() for line in file.readlines()]
    scratch_dict = defaultdict(int)
    result = 0
    for i in range(len(lines)):
        line = lines[i]
        win_sum = 0
        numbers = line.split(': ',1)[1].replace("  ", " ").replace("\n",'').split(' | ')
        win_num = numbers[0].split(' ')
        my_num = numbers[1].split(' ')
        for num in my_num:
            if num in win_num:
                win_sum+=1
        scratch_dict[i] = [1,win_sum]
    for key,val in scratch_dict.items():    
        for _ in range(val[0]):
            p=1
            for j in range(val[1]):
                scratch_dict[key+p][0]+=1
                p+=1
        result+=val[0]
            
    print(result)