with open("data.txt",'r') as file:
    min_location = None
    lines = [line.strip() for line in file.readlines()]
    seeds = lines[0].split(": ")[1].split(" ")
    for seed in seeds:
        seed_id = int(seed)
        state = False
        for line in lines:
            if len(line)>3 and line[0].isdigit() and state == False:
                numbers = line.split(" ")
                if int(numbers[1]) <= seed_id < int(numbers[1]) + int(numbers[2]):
                    seed_id = seed_id +  (int(numbers[0]) - int(numbers[1]))
                    state = True
            if len(line)<3:
                state = False
        if min_location == None or min_location > seed_id:
            min_location = seed_id
    print(min_location)