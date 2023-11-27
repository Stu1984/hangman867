import random

class Hangman:

    def __init__(self, word_list: list, num_lives = 5):

        #attributes from the class constructor:
        self.word_list = word_list
        self.num_lives = num_lives

        #Other attributes to be instantiated
        self.word = random.choice(word_list)
        self.hangman_list = ['_' for letter in self.word]
        self.num_letters = int(len(set(self.word)))
        self.guessed_letters_list = []

    def check_guess(self, guess):
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
            print(f'You have {self.num_lives} left')
            self.guessed_letters_list.append(guess)
            print(f'Letters guessed so far: {self.guessed_letters_list}')
            
            

    def ask_for_input(self):
        while True:
            guess = str(input('Guess a letter in the word: '))

            if not (guess.isalpha() and len(guess) == 1):
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.guessed_letters_list:
                print('You already tried that letter')
                self.guessed_letters_list.append(guess)
                print(self.guessed_letters_list)
            else:
                self.check_guess(guess)
                self.guessed_letters_list.append(guess)


game1 = Hangman(['peach', 'apple', 'fruit'])
game1.ask_for_input()
