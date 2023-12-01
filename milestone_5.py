
from milestone_4 import Hangman

# game1 = Hangman(['peach', 'apple', 'tomato'])
# game1.ask_for_input()

def play_game(word_list):
    '''call this function to play the game
    
    Play game function instantiates the game object of the Hangman class. 
    Using a while loop it checks the status of play, 
    if the game has not yet been won or lost, 
    it calls the ask_for_input method from Hangman class.
    
    Arguments:
    word_list (List) - list of words that the Hangman class will use to select a random word'''
    num_lives = 5
    game = Hangman(word_list, num_lives)
    print('Welcome to Hangman')
    print('Try and guess the word')
    while True:
        if game.num_lives == 0: #Checks if player has any lives left
            print('Sorry! You lost')
            break
        elif game.num_letters == 0: #Checks if player has already guessed all the letters
            print("Congrats! You're a winner")
            break
        else:
            game.ask_for_input() 
   
fruits = ['pear', 'apple', 'orange', 'plum', 'tangerine']
play_game(fruits)
