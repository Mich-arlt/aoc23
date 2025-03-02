def get_hand_power(hand):
    list_of_app = []
    for c in set(hand[0]):
        list_of_app.append(hand[0].count(c))
    list_of_app.sort()
    if list_of_app == [5]:
        hand.append(6)
        return hand
    if list_of_app == [1,4]:
        hand.append(5)
        return hand
    if list_of_app == [2,3]:
        hand.append(4)
        return hand
    if list_of_app == [1,1,3]:
        hand.append(3)
        return hand
    if list_of_app == [1,2,2]:
        hand.append(2)
        return hand
    if list_of_app == [1,1,1,2]:
        hand.append(1)
        return hand
    if list_of_app == [1,1,1,1,1]:
        hand.append(0)
        return hand
    
def same_power_fight(hand1,hand2):
    power_dict = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"T":10,"J":11,"Q":12,"K":13,"A":14}
    for i in range(len(hand1[0])):
        # print(power_dict[hand1[0][i]],power_dict[hand2[0][i]])
        if power_dict[hand1[0][i]] > power_dict[hand2[0][i]]:
            return True
        elif power_dict[hand1[0][i]] < power_dict[hand2[0][i]]:
            return False

with open("data.txt",'r') as file:
    power_list = []
    for line in file:
        hand = line.replace('\n','').split(' ')
        hand = get_hand_power(hand)
        # print(hand)
        if len(power_list) == 0:     
            power_list.append(hand)
        else:
            pl = len(power_list)
            # print(hand)///////dodaj parryyyyyyyyyyyy
            for h in power_list:
                if h[2] > hand[2]:
                    index = power_list.index(h)
                    power_list.insert(index, hand)
                    break
                elif h[2] == hand[2]:
                    state = True
                    for game in power_list:
                        # print(game)
                        if game[2] == hand[2]:
                            index_game = power_list.index(game)
                            if same_power_fight(game,hand):   
                                power_list.insert(index_game, hand)
                                state = False
                                break
                    if state:
                        # print(hand,"halo kurwa",index_game)
                        power_list.insert(index_game+1, hand)
                    break
            if pl == len(power_list):
                power_list.append(hand)
# print(power_list)  
     
result = 0
for i in range(len(power_list)):
    result += int(power_list[i][1]) * (i+1)
print(result)