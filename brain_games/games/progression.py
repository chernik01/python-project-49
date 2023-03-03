from random import randint, choice


game_desc = 'What number is missing in the progression?'
q = []
ra = []
for _ in range(3):
    num = randint(1, 100)
    step = randint(1, 10)
    q_cycle = [str(num)]

    for _ in range(9):
        num += step
        q_cycle.append(str(num))

    missed_num = choice(q_cycle)
    missed_index = q_cycle.index(missed_num)
    q_cycle[missed_index] = '..'
    q.append(q_cycle)
    ra.append(missed_num)

qra_list = list(zip(q, ra))
