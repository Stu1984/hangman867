# Hangman AI Core Project
Hangman is a classic game where the player has to try and guess a word by guessing whether a letter is in the word or not. In this project, we will be creating a version of Hangman where the player plays against the computer directly from their terminal. All code will be written in Python to be played directly in the Terminal.

This hangman game uses a list of fruits and will randomly select one of these fruits. The player needs to try and guess the fruit by trying different letters of the alphabet. The game will inform the player if their guess is correct and keep a list of letters already guessed by the player. 

The player begins with 5 lives. If they can guess all the letters in the word before they run out of lives they WIN the game. If they run out of lives, they LOSE the game.

# To play the game:

1. Ensure you have milestone_4.py and milestone_5.py files in your directory of choice.
2. From your terminal, navigate to the directory where these files are saved
3. Type: python milestone_5.py into the terminal andf hit enter to run the game
4. Let the gameplay commence

The game will then ask you to enter a single letter and will tell you if the letter is in the word or not. The game will print a list with underscores representing the letters still to be guessed and the letters completed for the guesses you have made correctly.

For example, if the word is 'apple' and your first guess was 'p' you will see ['_','p','p','_','_'] in the terminal.

Another list will be printed to the terminal that shows you the letters you have guessed so far.

## Dependencies:

- Python 3.xx

## File structure:

- milestone_4.py - The main game logic containing the Hangman class
- milestone_5.py - The python script the player uses to run the play_game() funtion to play the game.