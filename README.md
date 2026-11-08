🎮 UNO Game in Python

A classic console-based UNO card game written in Python for 2 to 4 players.

🎮 Game Rules & Flow

Setup: Each player receives 5 cards at the start.

Gameplay: Match the color or number of the top card on the discard pile. If you have no valid moves, you must draw a card.

Victory: The first player to clear all cards from their hand wins!

🛠️ Features & Implementation

Deck Creation: Generates a full 108-card deck including numbers, action cards (Skip, Reverse, Draw Two), and Wild cards.

Shuffling & Drawing: Dynamic deck shuffling using random.randint and smooth card extraction with .pop().

Special Cards: Includes working logic for Reverse, Skip, Draw Two/Four, and Wild color changes.

Move Validation: Automated checks to ensure only valid cards are played based on color, value, or Wild type.

🎴 Special Card Effects

Reverse – Reverses the turn order.

Skip – Skips the next player's turn.

Draw Two / Draw Four – Forces the next player to draw additional cards.

Wild – Allows the active player to change the current color.

⚠️ Challenges & Solutions

Deck Shuffling Issue: Fixed identical card distribution by refactoring shuffle_deck logic using random.randint.

Card Removal: Swapped out .remove() for .pop() to cleanly discard and manage cards from the top deck.
