with open("data.txt",'r') as file:
    result = 0
    for line in file:
        first_numbers = []
        numbers = list(map(int,line.split(" ")))
        while not len(set(numbers)) == 1:
            temp = []
            first_numbers.append(numbers[0])
            for i in range(len(numbers)-1):
                temp.append(numbers[i+1] - numbers[i])
            numbers = temp
            add_num = numbers[0]
        first_numbers.reverse()
        for n in first_numbers:
            add_num = n - add_num
        result += add_num
    print(result)