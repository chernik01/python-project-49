import math
from random import randint

game_desc = 'Find the greatest common divisor of given numbers.'
q = []
ra = []


for _ in range(3):
    num1 = str(randint(1, 10))
    num2 = str(randint(1, 10))
    q.append(f'{num1} {num2}')
    gcd_value = math.gcd(int(num1), int(num2))
    ra.append(str(gcd_value))

qra_list = list(zip(q, ra))
