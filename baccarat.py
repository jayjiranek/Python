#calculates winning probability for baccarat (simulates 1000 games)

import random


def computeScore(hand):
    total_value = 0
    for card in hand:
        if(card.value < 10):
            total_value += card.value
    return total_value % 10

def play(deck):
    #Shuffle Deck
    random.shuffle(deck)
   
    #Pass out hands
    player_hand = [
        deck.pop(0), deck.pop(0)
    ]
    banker_hand = [
        deck.pop(0), deck.pop(0)
    ]
   
    #compute scores
    player_score = computeScore(player_hand)
    banker_score = computeScore(banker_hand)
    #print("The players score is: " + str(player_score))
    #print("The bankers score is: " + str(banker_score))
   
    #check for "natural"
    if player_score in [8, 9] or banker_score in [8, 9]:
        if player_score in [8, 9] and banker_score not in [8, 9]:
            #print('Player Wins')
            return 0
        elif banker_score in [8, 9] and player_score not in [8, 9]:
            #print("Banker Wins")
            return 1
        else:
            #print("Tie")
            return 2
           
    #check if player has low hand and give third card
    if player_score <= 5:
        player_hand.append(deck.pop(0))
        #print("Player gets a new card: " + str(player_hand[2].value) + " of " + player_hand[2].color)
       
        #check if banker needs third card
        if (banker_score == 6 and player_hand[2].value in [6, 7]) or (banker_score == 5 and player_hand[2].value in [4, 5, 6, 7]) or  (banker_score == 4 and player_hand[2].value in [2, 3, 4, 5, 6, 7]) or (banker_score == 3 and player_hand[2].value != 8) or (banker_score <= 2):
            banker_hand.append(deck.pop(0))
            #print("Banker gets a new card: " + str(banker_hand[2].value) + " of " + banker_hand[2].color)
   
    elif player_score in [6, 7]:
        if banker_score <= 5:
            banker_hand.append(deck.pop(0))
            #print("Banker gets a new card: " + str(banker_hand[2].value) + " of " + banker_hand[2].color)
           
    player_score = computeScore(player_hand)
    #print("Players score: " + str(player_score))
    banker_score = computeScore(banker_hand)
    #print("Bankers score: " + str(banker_score))
   
    if(player_score > banker_score):
        #print('Player Wins')
        return 0
    elif(banker_score > player_score):
        #print("Banker Wins")
        return 1
    else:
        #print("Tie")
        return 2
       
class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color

colors = ['hearts', 'diamonds', 'spades', 'clubs']

total_player_wins = 0
total_banker_wins = 0
total_ties = 0
for i in range(1000):
    deck = [Card(value, color) for value in range(1, 14) for color in colors]
    result = play(deck)
    if(result == 0):
        total_player_wins += 1
    elif(result == 1):
        total_banker_wins += 1
    else:
        total_ties += 1
       

prob_player = total_player_wins / 1000
prob_banker = total_banker_wins / 1000
prob_tie = total_ties / 1000

print("After running a 1000 trials the results are: ")
print("The probability the player will win is: " + str(prob_player))
print("The probability the banker will win is: " + str(prob_banker))
print("The probability of a tie is: " + str(prob_tie))
   
