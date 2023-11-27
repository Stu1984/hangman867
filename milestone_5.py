# %%
from milestone_4 import Hangman

# game1 = Hangman(['peach', 'apple', 'tomato'])
# game1.ask_for_input()

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    pass
    # while True:
    #     print('Choose your category: ')
    #     print('1. Movies')
    #     print('2. Fruits')
    #     print('3. TV Shows')
    #     print('4. Countries')
play_game(['stuart', 'mary'])
