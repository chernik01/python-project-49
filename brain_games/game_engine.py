import prompt


def game_engine(list, desc):
    flag = True
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(desc)
    for q, ra in list:
        print(f'Question: {q}')
        a = prompt.string('Your answer: ')
        if ra == a:
            print('Correct!')
        else:
            print(f"'{a}' is wrong answer ;(. Correct answer was '{ra}'")
            print(f"Let's try again, {name}!")
            flag = False
            break
    if flag is True:
        print(f'Congratulations, {name}!')
