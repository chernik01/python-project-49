from random import randint

game_desc = 'Answer "yes" if given number is prime. Otherwise answer "no".'
q = []
ra = []


for _ in range(3):
    num = str(randint(11, 100))

    q.append(f'{num}')
    k = 0
    for i in range(2, int(num) // 2 + 1):
        if int(num) % i == 0:
            k += 1
    if k <= 0:
        prime = 'yes'
    else:
        prime = 'no'

    ra.append(str(prime))

qra_list = list(zip(q, ra))
