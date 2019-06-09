import random

def graphics(tries):
    if tries == 0:
        print('------')
        print('|   0 ')
        print('|  /I\\')
        print('|  / \\')
        print('|')
        print('-----')
    elif tries == 1:
        print('------')
        print('|   0 ')
        print('|  /I\\')
        print('|  /')
        print('|')
        print('-----')
    elif tries == 2:
        print('------')
        print('|   0 ')
        print('|  /I\\')
        print('|')
        print('|')
        print('-----')
    elif tries == 3:
        print('------')
        print('|   0 ')
        print('|  /I')
        print('|')
        print('|')
        print('-----')
    elif tries == 4:
        print('------')
        print('|   0 ')
        print('|   I')
        print('|')
        print('|')
        print('-----')
    elif tries == 5:
        print('------')
        print('|   0 ')
        print('|')
        print('|')
        print('|')
        print('-----')
    else:
        print('------')
        print('|')
        print('|')
        print('|')
        print('|')
        print('-----')

def user_input(word):
    print(word)
    for l in word:
        print('_', end=" ")
    print()
    letter = input('Enter a letter: ')
    return letter

def check(word, letter):
    if letter in word:
        return True
    else:
        return False

def update_lose(tries):
    if tries == 0:
        return True
    else:
        return False

def update_win(blanks):
    if blanks == 0:
        return True
    else:
        return False

def init():
    l = ["giraffe", "python", "zebra", "lion", "squirrel"]
    for x in range(1):
        random.randint(1,5)
    return l[x]

word = init()
tries = 6
graphics(tries)
letter = user_input(word)
win = False
lose = False
while (not win) or (not lose):
    if check(word, letter):
        print('correct')
    else:
        tries -= 1
        print('incorrect')
    win = update_win(word.count('_'))
    lose = update_lose(tries)
    graphics(tries)
    letter = user_input(word)
  
