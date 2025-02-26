with open("data.txt",'r') as file:
    result = 0
    for line in file:
        win_sum = 0
        numbers = line.split(': ',1)[1].replace("  ", " ").replace("\n",'').split(' | ')
        win_num = numbers[0].split(' ')
        my_num = numbers[1].split(' ')
        for num in my_num:
            if num in win_num:
                if win_sum == 0:
                    win_sum+=1
                else:
                    win_sum*=2
        result+=win_sum
    print(result)       