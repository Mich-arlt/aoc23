def word_to_num(val:str):
    numbers = ["one","two","three","four","five","six","seven","eight","nine"]
    rep = [("one","1"),("two","2"),("three","3"),("four","4"),("five","5"),("six","6"),("seven","7"),("eight","8"),("nine","9")]
    line = ''
    result = ''
    for i in range(0, len(val)):
        if val[i].isdigit():
            line = val[i]
            break
        line = line +  val[i]
        if any(num in line for num in numbers):
            for word,num in rep:
                line = line.replace(word,num)
            break
    result = line
    line = ''
    for i in range(len(val) - 1, -1, -1):
        if val[i].isdigit():
            line = val[i]
            break
        line = val[i]+line
        if any(num in line for num in numbers):
            for word,num in rep:
                line = line.replace(word,num)
            break
    result += line
    return result

with open("data.txt",'r') as file:
    result = 0
    for line in file:
        line = word_to_num(line)
        whole_num = "".join(filter(str.isdigit,line))
        if len(whole_num) >2:
                num = int(whole_num[0] + whole_num[-1])
        elif len(whole_num) ==  1:
                num = int(whole_num*2)
        else:
                num = int(whole_num)
        result+=num
print(result)