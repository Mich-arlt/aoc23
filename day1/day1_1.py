with open("data.txt",'r') as file:
    result = 0
    for line in file:
        whole_num = "".join(filter(str.isdigit,line))
        if len(whole_num) >2:
            num = int(whole_num[0] + whole_num[-1])
        elif len(whole_num) ==  1:
            num = int(whole_num*2)
        else:
            num = int(whole_num)
        result+=num
print(result)