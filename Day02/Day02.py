def read_data(file_path):
    f = open(file_path,'r')
    lines = f.read().split('\n')
    
    return lines

def calc_choice_score(choice):
    if choice == 'X':
        score = 1
    elif choice == 'Y':
        score = 2
    else:
        score = 3

    return score

def calc_result_score(result):
    if result == 'win':
        score = 6
    elif result == 'loss':
        score = 0
    else:
        score = 3

    return score
    
def play_round_part_one(round_data):
    opp_choice = round_data[0]
    my_choice = round_data[1]
    score = calc_choice_score(my_choice)

    if opp_choice == 'A':
        if my_choice == 'X': #rock
            result = 'draw'
        elif my_choice == 'Y': #paper
            result = 'win'
        else: #scissors
            result = 'loss'

    elif opp_choice == 'B':
        if my_choice == 'X': #rock
            result = 'loss'
        elif my_choice == 'Y': #paper
            result = 'draw'
        else: #scissors
            result = 'win'
    
    else:
        if my_choice == 'X': #rock
            result = 'win'
        elif my_choice == 'Y': #paper
            result = 'loss'
        else: #scissors
            result = 'draw'  

    score += calc_result_score(result)

    return score

def play_round_part_two(round_data):
    opp_choice = round_data[0]
    result = round_data[1]
    
    if result == 'X':
        score = calc_result_score('loss')
    elif result == 'Y':
        score = calc_result_score('draw')
    else:
        score = calc_result_score('win')
        

    if result == 'X':
        if opp_choice == 'A':
            my_choice = 'Z'
        elif opp_choice == 'B':
            my_choice = 'X'
        else:
            my_choice = 'Y'
    
    elif result == 'Y':
        if opp_choice == 'A':
            my_choice = 'X'
        elif opp_choice == 'B':
            my_choice = 'Y'
        else:
            my_choice = 'Z'

    else:
        if opp_choice == 'A':
            my_choice = 'Y'
        elif opp_choice == 'B':
            my_choice = 'Z'
        else:
            my_choice = 'X'

    score += calc_choice_score(my_choice)

    return score

data = read_data('./data/Day02.txt')
total_score_p1 = 0
total_score_p2 = 0

for round in data:
    round = round.split(' ')
    print(round)
    total_score_p1 += play_round_part_one(round)
    total_score_p2 += play_round_part_two(round)

print(total_score_p1)
print(total_score_p2)