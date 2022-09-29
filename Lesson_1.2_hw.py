from random import randrange, choice

a1 = 0
a2 = 0


def door(door_num, decision):
    global a1, a2, door_b
    score = 0
    if decision:
        b1 = [1, 2, 3]
        b1.remove(door_num)
        door_b = randrange(b1[0], b1[1])
        a1 += 1
    if not decision:
        door_b = door_num
        a2 += 1
    if door_b == win_door:
        score = 1
    else:
        score = 0
    return score


score_def = 0
list = [True, False]
for i in range(1000):
    win_door = randrange(1, 4)
    door_random = randrange(1, 4)
    decision_random = choice(list)
    a = door(door_random, decision_random)
    score_def += a

print(score_def, a1, a2)

