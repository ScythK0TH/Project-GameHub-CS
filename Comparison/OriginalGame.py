import random

animals = [ 'elephant' , 'bear' , 'cheetah' , 'giraffe' , 'wolf' , 'tiger' , 'penguin' , 'rabbit' , 'lion' , 'monkey' , 'rhinoceros' , 'sheep' , 'kangaroo' , 'zebra']

fruits = [ 'apple' , 'banana' , 'grapes' , 'mango' , 'lime' , 'watermelon' , 'jectfruite' , 'guava' , 'orange' , 'papaya' , 'pear' , 'peach' , 'pomegranate' , 'strawberry']

stationery = [ 'pencil' , 'eraser' , 'sharpener' , 'envelope' , 'paper' , 'stapler' , 'folder' , 'marker' , 'inkpot' , 'calculator' , 'glue' , 'notebook' , 'scissors' , 'ruuler']

words = animals + fruits + stationery
random_word = random.choice(words)
print('Word Guessing Game')
if random_word in animals:
    print ('Hint: It is an animal')
elif random_word in fruits:
    print ('Hint: It is an fruits')
elif random_word in stationery:
    print ('Hint: It is an stationery')

user_guesses = ''
chances = 5

while chances > 0:
   wrong_guess = 0
   for ch in random_word:
    if ch in user_guesses:
       print()
    else:
       wrong_guess += 1
       print('', end ='_')
   if wrong_guess == 0:
       print('\nCongrats.you won. The word is ',random_word)
       again = input('Do you like to play again? Y or N')
       if again == 'Y':
         break
       else:
         quit()
         
   guess = input('\nMake a guess')
   user_guesses += guess

   if guess not in random_word:
       chances -= 1
       print(f'Worng. You have {chances} more chances')
       if chances == 0:
         print('Game over. You Lose. The word is ', random_word)
         restart = input('Do you like to play again? Y or N')
         if restart == 'N':
           quit()
