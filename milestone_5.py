# %%
from milestone_4 import Hangman

# game1 = Hangman(['peach', 'apple', 'tomato'])
# game1.ask_for_input()

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    print('Welcome to Hangman')
    print('Try and guess the word')
    while True:
        if game.num_lives == 0:
            print('Sorry! You lost')
            break
        elif game.num_letters == 0:
            print("Congrats! You're a winner")
            break
        else:
            game.ask_for_input()
   
play_game(['peach', 'apple', 'tomato'])
