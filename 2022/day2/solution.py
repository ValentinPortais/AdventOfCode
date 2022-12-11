#!/usr/bin/env python
code = { 'Rock': ['A','X'],
         'Paper': ['B','Y'],
         'Scissors': ['C','Z']
}
score = {
        'Rock': 1,
        'Paper': 2,
        'Scissors': 3
        }
winner = {
    'Rock': 'Scissors',
    'Paper': 'Rock',
    'Scissors': 'Paper'
}
p1_total, p2_total, round_result = 0, 0, 0

for round in open("input.txt",mode="r").read().splitlines():
    c_user = round.split()[1]
    c_opponent = round.split()[0]
    user = [k for k, v in code.items() if c_user in v]
    opponent = [k for k, v in code.items() if c_opponent in v]
    if  winner[user[0]] == opponent[0]:
        round_result = 6
    elif user[0] == opponent[0]:
        round_result = 3
    else:
        round_result = 0
    p1_total += score[user[0]] + round_result

# Part 2
    match c_user:
        case 'X':
            p2_total += score[winner[opponent[0]]]
        case 'Y':
            p2_total += score[opponent[0]] + 3
        case 'Z':
            win_value = list(winner.keys())[list(winner.values()).index(opponent[0])]
            p2_total += score[win_value] + 6

print(p1_total)
print(p2_total)