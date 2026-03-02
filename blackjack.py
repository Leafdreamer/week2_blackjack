import random
import time
import sys
sys.path.append('.')
import blackjackFunctions as app

# Make a sample deck for the program to use
sampleDeck = []
cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
suits = [" of Hearts", " of Diamonds", " of Clubs", " of Spades"]
# Make the sample deck into 'x' lists (x being the amount of suits), each containing one of each card with the respective suit
sampleDeck.append([a + x for a in cards for x in suits])
# Merge them all into one list
sampleDeck = sum(sampleDeck, [])

print("Welcome to Blackjack!")
time.sleep(1)

while True:
    # Start game
    # Make a copy deck to play with
    deck = sampleDeck
    # Shuffle deck
    print("Shuffling the deck...")
    random.shuffle(deck)
    time.sleep(1)

    # Set variables to their initial, blank states
    playerBusts = False
    playerHand = []
    playerScore = 0
    dealerHand = []
    dealerScore = 0
    dealerVHand = []

    # Deal 2 cards to player
    playerHand.append(deck.pop(0))
    playerHand.append(deck.pop(0))
    # Deal 2 cards to dealer
    dealerHand.append(deck.pop(0))
    dealerHand.append(deck.pop(0))
    # Dealer's first card is the only one visible
    dealerVHand.append(dealerHand[0])

    # Display hands
    print("Your hand is " + str(playerHand))
    print("The dealer's hand is " + str(dealerVHand) + " and a card face down.")
    time.sleep(1)

    # Check player score
    playerScore = app.CheckScore(playerHand)
    dealerScore = app.CheckScore(dealerHand)
    print("Your score is " + str(playerScore) + ".")
    time.sleep(1)

    # Player turn (input for hit or stand)
    while True:
        print("Make your move: ")
        print("1. Hit (receive another card)")
        print("2. Stand (finish your turn)")
        choice = input()

        # If hit, draw card and check points again (redo player input or skip to end if score above 21)
        if choice == "1":
            print("Player hits.")
            time.sleep(0.5)            
            playerHand.append(deck.pop(0))
            print("Your hand is " + str(playerHand) + ".")
            time.sleep(0.5)
            playerScore = app.CheckScore(playerHand)
            print("Your score is " + str(playerScore) + ".")
            time.sleep(2)

        # Check if player busts and skip rest of turn if so
        if playerScore > 21:
            print("Player busts.")
            playerBusts = True
            time.sleep(2)
            break

        # If stand, move on to dealer's turn
        elif choice == "2":
            print("Player stands.")
            time.sleep(2)
            break

        # Redisplay information for context in case of invalid input
        elif choice != "1" and choice != "2":
            # Display hands
            print("Your hand is " + str(playerHand) + ".")
            print("The dealer's hand is " + str(dealerVHand) + " and a card face down.")
            time.sleep(1)

            # Check player score
            playerScore = app.CheckScore(playerHand)
            print("Your score is " + str(playerScore) + ".")
            time.sleep(1)

    # Dealer turn
    # This block is skipped if the player busts
    if playerBusts == False:
        # Shows dealer's second card
        print("Dealer's turn, dealer's second card was " + dealerHand[1] + ".")
        time.sleep(1)
        print("Dealer's hand: " + str(dealerHand) + ".")
        print("Dealer's score is " + str(dealerScore) + ".")
        time.sleep(2)
        # If dealer already has 17 or wins by score, stands
        if dealerScore >= 17 or dealerScore > playerScore:
            print("Dealer stands.")
            time.sleep(2)
        # Otherwise, will hit until 17 or until higher than player's score
        # Both of these conditions must be met for the dealer to keep hitting
        while dealerScore < 17 and dealerScore <= playerScore:
            print("Dealer hits.")
            dealerHand.append(deck.pop(0))
            dealerScore = app.CheckScore(dealerHand)
            time.sleep(0.5)
            print("Dealer's hand: " + str(dealerHand) + ".")
            time.sleep(0.5)
            print("Dealer's score is " + str(dealerScore) + ".")
            time.sleep(2)        
            # Checks if dealer busts
            if dealerScore > 21:
                print("Dealer busts.")
                time.sleep(2)
            # Checks if dealer is above 17 or wins by score
            elif dealerScore >= 17 or dealerScore > playerScore:
                print("Dealer stands.")
                time.sleep(2)

    # Display scores, decide winner
    print("ROUND END.")
    time.sleep(0.25)
    print("PLAYER SCORE: " + str(playerScore))
    time.sleep(0.25)
    print("DEALER SCORE: " + str(dealerScore))
    time.sleep(0.25)

    winner = app.DetermineWinner(playerScore, dealerScore)

    if winner == 0:
        print("YOU WIN $" + str(random.randint(1, 1000)) + ".")
    elif winner == 1:
        print("YOU LOSE $" + str(random.randint(1, 1000)) + ".")
    elif winner == 2:
        print("IT'S A DRAW.")
    time.sleep(0.5)

    input("Input anything to start another round.")
    # Loops here