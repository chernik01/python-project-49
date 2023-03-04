from random import randint, choice

q = []
ra = []
for _ in range(3):
    num1 = str(randint(1, 6))
    op = choice('*-+')
    num2 = str(randint(1, 6))
    q.append(f'{num1} {op} {num2}')
    ra.append(str(eval(num1 + op + num2)))

qra_list = list(zip(q, ra))
game_desc = 'What is the result of the expression?'
