import random

'''create_deck function generates 108 cards in the deck'''
def create_deck():
    deck = []
    #example card: Red 7, Green 8, Blue Skip
    colours = ["Red","Green","Yellow","Blue"]
    values = [0,1,2,3,4,5,6,7,8,9,"Draw Two", "Skip", "Reverse"]
    wilds = ["Wild","Wild Draw Four"]
    for colour in colours:
        for value in values:
            card_value = "{} {}".format(colour, value)
            deck.append(card_value)
            if value != 0:
                deck.append(card_value)
    for i in range(4):
        deck.append(wilds[0])
        deck.append(wilds[1])      
    return deck

'''shuffle_deck function shuffles the cards in the deck'''
def shuffle_deck(deck):
    for card_pos in range(len(deck)):
        rand_pos = random.randint(0,107)
        deck[card_pos], deck[rand_pos] = deck[rand_pos], deck[card_pos]
    return deck

'''draw_cards function draws cards for players form the deck'''
def draw_cards(num_cards):
    cards_drawn = []
    for x in range(num_cards):
        cards_drawn.append(uno_deck.pop(0))
    return cards_drawn

'''show_hand function shows players' hands'''
def show_hand(player, player_hand):
    print("Player {}'s Turn".format(player+1))
    print("Your Hand")
    print("------------------")
    y = 1
    for card in player_hand:
        print("{}) {}".format(y,card))
        y+=1
    print("")

'''can_play function detects that player can play a card or not'''
def can_play(colour, value, player_hand):
    for card in player_hand:
        if "Wild" in card:
            return True
        elif colour in card or value in card:
            return True
    return False

uno_deck = create_deck()
uno_deck = shuffle_deck(uno_deck)
uno_deck = shuffle_deck(uno_deck)
discard_pile = []

players = []
colours = ["Red","Green","Yellow","Blue"]
num_players = int(input("How many players? "))
while num_players<2 or num_players>4:
    num_players = int(input("Invalid. Please enter a number between 2-4. How many players? "))
for player in range(num_players):
    players.append(draw_cards(5))

play_turn = 0
play_direction = 1
playing = True
discard_pile.append(uno_deck.pop(0))
split_card = discard_pile[0].split(" ", 1)
current_colour = split_card[0]
if current_colour != "Wild":
    card_value = split_card[1]
else:
    card_value = "Any"

while playing:
    show_hand(play_turn,players[play_turn])
    print("Card on top of discard pile: {}".format(discard_pile[-1]))
    if can_play(current_colour, card_value,players[play_turn]):
        card_chosen = int(input("Which card do you want to play? "))
        while not can_play(current_colour, card_value,[players[play_turn][card_chosen-1]]):
            card_chosen = int(input("Not a valid card. Which card do you want to play? "))
        print("You played {}".format(players[play_turn][card_chosen-1]))
        discard_pile.append(players[play_turn].pop(card_chosen-1))
        #Check if player won
        if len(players[play_turn])==0:
            playing = False
            winner = "Player {}".format(play_turn+1)
        else:
            #Check for special cards
            split_card = discard_pile[-1].split(" ", 1)
            current_colour = split_card[0]
            if len(split_card) == 1:
                card_value = "Any"
            else:
                card_value = split_card[1]
            if current_colour == "Wild":
                for x in range(len(colours)):
                    print("{}) {}".format(x+1, colours[x]))
                new_colour = int(input("What colour would you like to choose? "))
                while new_colour < 1 or new_colour > 4:
                    new_colour = int(input("Invalid option. What colour would you like to choose? "))
                current_colour = colours[new_colour-1]
            if card_value == "Reverse":
                play_direction = play_direction * -1
            elif card_value == "Skip":
                play_turn += play_direction
                if play_turn >= num_players:
                    play_turn = 0
                elif play_turn < 0:
                    play_turn = num_players-1
            elif card_value == "Draw Two":
                player_draw = play_turn+play_direction
                if player_draw == num_players:
                    player_draw = 0
                elif player_draw < 0:
                    player_draw = num_players-1
                players[player_draw].extend(draw_cards(2))
            elif card_value == "Draw Four":
                player_draw = play_turn+play_direction
                if player_draw == num_players:
                    player_draw = 0
                elif player_draw < 0:
                    player_draw = num_players-1
                players[player_draw].extend(draw_cards(4))
            print("")
    else:
        print("You can't play. You have to draw a card.")
        players[play_turn].extend(draw_cards(1))

    play_turn += play_direction
    if play_turn >= num_players:
        play_turn = 0
    elif play_turn < 0:
        play_turn = num_players-1
    
print("Game Over")
print("{} is the Winner!".format(winner))