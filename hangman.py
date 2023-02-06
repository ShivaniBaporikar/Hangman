import random

from pywebio.input import *
from pywebio.output import *

name = input('what is your name')

print('Good luck', name)

words = ('Colonel', 'Worcestershire' ,'Mischievous' ,'Draught', 'Quinoa' ,'Onomatopoeia' ,'Scissors', 'Anemone', 'rainbow', 'hypoxia', 'scoliosis', 'garden', 'Meiosis', 'somatic', 'refraction')

word = random.choice(words)

print('Guess the characters of the word, good luck!!!')

guesses = ''
turns = 12

while turns > 0:
    failed = 0

    for char in word:

        if char in guesses:
            print(char)

        else:
             print("_")
             failed += 1

    if failed == 0:
        print(' you won, congrats', 'the word is' , word)

        break 

    guess = input('guess the character')

    guesses += guess

    if guess not in word:
        turns -= 1

        print('wrong you', turns, ' turns left')

        if turns == 0:

            print('better luck next time')





    

    

        

         

