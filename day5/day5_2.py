import time
def if_location_in_seeds(seed, seeds):
    for start, end in seeds:
        if start <= seed < end:
            return True
    return False

start_time = time.time()
with open("data.txt",'r') as file:
    min_location = None
    lines = [line.strip() for line in file.readlines()]
    og_seeds_raw = list(map(int, lines[0].split(": ")[1].split()))
    og_seeds = [(og_seeds_raw[i], og_seeds_raw[i] + og_seeds_raw[i + 1]) for i in range(0, len(og_seeds_raw), 2)]
    og_location = 148000000
    lines.reverse()
    while True:
        state = False
        location = og_location
        for line in lines:
            if len(line)>3 and line[0].isdigit() and state == False:
                numbers = line.split(" ")
                if int(numbers[0]) <= location < int(numbers[0]) + int(numbers[2]):
                    location = location -  (int(numbers[0]) - int(numbers[1]))
                    state = True
            if len(line)<3:
                state = False
        if if_location_in_seeds(location,og_seeds):
            break
        og_location+=1
    print(og_location)
    end_time = time.time()
    print(f"Czas wykonania: {end_time - start_time:.6f} sekund")