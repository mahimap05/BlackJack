#name function

def name(card_rank):
  if card_rank == 1:
    # A 1 stands for an ace.
    card_name = "Ace"
  elif card_rank == 11:
    # An 11 stands for a jack.
    card_name = "Jack"
  elif card_rank == 12:
    # A 12 stands for a queen.
    card_name = "Queen"
  elif card_rank == 13:
    # A 13 stands for a king.
    card_name = "King"
  else:
    # All other cards are named by their
    # number, or rank.
    card_name = str(card_rank)

  if card_rank == 1 or card_rank == 8:
    drew_prefix = 'Drew an '
  else:
    drew_prefix = 'Drew a '

  if card_rank < 1 or card_rank > 13:
    print('BAD CARD')
  else:
    return (drew_prefix + card_name)


#value function

def value(card_rank):
  if card_rank == 11 or card_rank == 12 or card_rank == 13:
    # Jacks, Queens, and Kings are worth 10.
    card_value = 10
  elif card_rank == 1:
    # Aces are worth 11.
    card_value = 11
  else:
    # All other cards are worth the same as
    # their rank.
    card_value = card_rank

  if card_rank > 13 or card_rank < 1:
    print('BAD CARD')
  else:
    return card_value

from random import randint

print("-----------\nYOUR TURN\n-----------")

hand_value = 0
cards_drawn = 0
is_yes = True

while is_yes == True and hand_value < 21:
    if cards_drawn < 2:
        card_rank=randint(1,13)
        print(name(card_rank))
        hand_value += value(card_rank)
        cards_drawn += 1
    else: 
        should_hit = input('You have ' + str(hand_value) + ". Hit (y/n)? ")
        if should_hit.lower() == 'n':
            is_yes = False
        elif should_hit.lower() == 'y':
            card_rank = randint(1, 13)
            print(name(card_rank))
            hand_value+=value(card_rank)
        else:
            print("Sorry I didn't get that.")

print("Final hand: " + str(hand_value) + ".")

if hand_value == 21:
    print("BLACKJACK!")
elif hand_value > 21 and hand_value <= 31:
    print("BUST.")
  

print("-----------\nDEALER TURN\n-----------")

dealer_value = 0
num_cards = 0

while dealer_value < 17:
    if num_cards<2:
        card_rank=randint(1,13)
        print(name(card_rank))
        dealer_value+=value(card_rank)
        num_cards+=1
    else:
        print("Dealer has {}.".format(dealer_value))
        card_rank = randint(1,13)
        print(name(card_rank))
        dealer_value+=value(card_rank)

print("Final hand: " + str(dealer_value) + ".")
if dealer_value == 21:
    print("BLACKJACK!")
elif dealer_value > 21 and dealer_value <= 31:
    print("BUST.")


print("-----------\nGAME RESULT\n-----------")

if hand_value<21 and dealer_value>21:
    print("You win!")
elif hand_value == 21:
    print("You win!")
elif hand_value>21:
    print("Dealer wins!")
elif hand_value>dealer_value:
    print("You win!")
elif dealer_value>hand_value:
    print("Dealer wins!")
else:
    print("Push.")
