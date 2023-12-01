import random

class Hangman:
    '''Class contains all attributes and methods for classic hangman game. 
    Intended to be called using the play_game function in milestone_5.py'''

    def __init__(self, word_list: list, num_lives = 5):
        '''Class constructor to instantiate objects

        Arguments:
        word_list: List - list of words the game uses to pick random word for user to guess
        num_lives: int, default = 5. Number of lives the player starts with'''
        #attributes from the class constructor:
        self.word_list = word_list
        self.num_lives = num_lives

        #Other attributes to be instantiated
        self.word = random.choice(word_list) #Random word generated from the word_list
        self.hangman_list = ['_' for letter in self.word] #Provides list of '_' replacing the letters of the random word.
        self.num_letters = int(len(set(self.word))) #Calculates number of unique letters in the word
        self.guessed_letters_list = [] #Empty list which will contain all letters guessed by user

    def check_guess(self, guess):
        '''Method called from inside the ask_for_input method.

        Used to check if the guessed letter is in the random word and what happens if it is and is not.
        If letter is included, the for loop is used to replace '_' with the guessed letter and
        the num_letters attribute is reduced by 1.
        If letter is not included in the random word, num_lives is reduced by 1. Guessed letter is appended to guessed_letters_list

        Arguments:
        guess (str) - the letter provided by the user'''
        guess = guess.lower()
        self.word = self.word.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word')
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.hangman_list[index] = letter
            print(self.hangman_list)
            self.num_letters -= 1
            
        else:
            self.num_lives -= 1
            print('Sorry, bad guess')
            print(f'You have {self.num_lives} lives left')
            self.guessed_letters_list.append(guess)
            print(f'Letters guessed so far: {self.guessed_letters_list}')
            # return self.num_lives
      
    def ask_for_input(self):
        '''ask_for_input method is called within the play_game function
        
        ask_for_input method asks the user to input their guess, 
        checks whether the input is valid and will ask the user 
        to try again if not or if the letter has already been used.
        
        If the guess is valid and unique the check_guess method is called and we break out of the loop'''
        while True:
            guess = str(input('Guess a letter in the word: '))

            if not (guess.isalpha() and len(guess) == 1):
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.guessed_letters_list:
                print('You already tried that letter')
                print(f'Letters guessed so far {self.guessed_letters_list}')
            else:
                self.check_guess(guess) # If the guess is valid and unique check_guess method is called
                self.guessed_letters_list.append(guess)
                break


# game1 = Hangman(['peach', 'apple', 'fruit'])
# game1.ask_for_input()
