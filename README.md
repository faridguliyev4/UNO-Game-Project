UNO Game Project 

Description: 
This project is a Python console-based implementation of the popular UNO card game. It simulates a 2-4 player game, handling core game mechanics such as deck creation, dealing cards, turn management, special cards, and winning conditions.   

Key Features and Functionality: 
Deck Creation (create_deck): Generates a 108-card deck consisting of four colors (Red, Green, Yellow, Blue), numbers from 0 to 9, action cards (Draw Two, Skip, Reverse), and wild cards (Wild, Wild Draw Four).   
Shuffling Mechanism (shuffle_deck): Shuffles the cards randomly using randint from Python's random module.   
Game Flow and Moves: 
Each player starts with 5 cards.   
The valid_move function checks whether a player's card matches the color or value of the top card on the discard pile.   
If a player does not have a suitable card, they must draw a card from the deck.   
Special Cards: Includes functional rules for Reverse (reverses turn order), Skip (skips the next player's turn), Draw Two/Four (forces the next player to draw extra cards), and Wild (allows changing the active color).   
Winning Condition: The game ends and announces a winner when a player successfully discards all the cards in their hand.   

Challenges and Solutions: 
Color Issue: Initially, running the code always resulted in the same color cards being dealt; this was resolved by fixing the index-swapping logic inside the shuffle_deck function using random.randint.   
Deletion Bug: Originally used the remove method to delete the top card of the discard pile, which was corrected and replaced with the more appropriate pop method.
