# -*- coding: utf-8 -*-

"""

Spyder Editor

 

This is a temporary script file.

"""

import random

teams = [[['Reds','Cardinals','Cubs','Pirates','Brewers'],['Mets','Marlins','Braves','Nationals','Phillies'],['Dodgers','Giants','Rockies','Padres','Diamondbacks']],

[['Blue Jays','Red Sox','Yankees','Rays','Orioles'],['White Sox','Guardians','Tigers','Twins','Royals'],['Astros','Angels','Athletics','Mariners','Rangers']]]

random_league = random.randint(0,1)

random_division = random.randint(0, 2)

random_team = random.randint(0,4)

answer = teams[random_league][random_division][random_team]

#print(random_league)

#print(random_division)

#print(random_team)

#print(answer)

i = 1

while i < 5:

    remaining_trys = 4-i

    guess = input('Please guess a Major League Baseball team. ').title()

    if (guess in teams[random_league][random_division]):

        if guess == answer:

            break

        else:

            print(f'You have the correct division. Wrong team. Keep Guessing, you have {remaining_trys} tries remaining')

            i = i+1

    else:

        if any(guess in i for i in teams[0]) or any(guess in i for i in teams[1]):

            if any(guess in i for i in teams[random_league]):

                print(f'Correct league, Wrong division, keep guessing, you have {remaining_trys} tries remaining.')

                i = i+1

            else:

                 print(f'Wrong league, Wrong division, keep guessing, you have {remaining_trys} tries remaining.')

                 i = i+1

        else:

            print('That is not a valid MLB team.')

if guess == answer:

    print(f'You are correct, the answer is {answer}! You are a baseball genious :). Thank you for playing Baseballdle')

else:

    print(f'Sorry you did not get the answer. The team was {answer}')