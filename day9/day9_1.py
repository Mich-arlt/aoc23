with open("data.txt",'r') as file:
    result = 0
    for line in file:
        last_numbers = []
        numbers = list(map(int,line.split(" ")))
        while not len(set(numbers)) == 1:
            temp = []
            last_numbers.append(numbers[-1])
            for i in range(len(numbers)-1):
                temp.append(numbers[i+1] - numbers[i])
            numbers = temp
            add_num = numbers[0]
        for n in last_numbers:
            add_num = n+add_num
        result += add_num
    print(result)