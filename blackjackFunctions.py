# Function for checking is an inputted value is a whole number
def isInt(x):
    try:
        int(x)
        return True
    except:
        return False

# Function for removing letters from a string, to get the numerical value of numbered cards
def RemoveLetters(x):
    y = ""

    for character in x:
        if isInt(character):
            y = y + character

    return y

# Function for updating the player's/dealer's score
def CheckScore(handToCheck):
    score = 0
    aceCount = 0
    
    for a in handToCheck:
        # Kings, Queens, and Jacks give +10 to the score
        if ("King" in a) or ("Queen" in a) or ("Jack" in a):
            score = score + 10
        # Numbered cards give their numerical value to the score
        elif isInt(a[0]):
            number = RemoveLetters(a)
            score = score + int(number)
        # Aces give either +1 or +11, whichever is highest and won't lead to a bust
        # Since this is a little more complex, there is a segment below dedicated to this
        # But for now we just want the amount of Aces
        elif ("Ace" in a):
            aceCount = aceCount + 1
    
    if aceCount > 0:
        # If there is 1 Ace and the score won't bust, give +11
        if aceCount == 1 and (score + 11) <= 21:
            score = score + 11
        # If there are 2 Aces and the score won't bust, give +12 (11 + 1)
        # Note that you can never get 11 + 11 from 2 Aces since that would bust
        # This also applies to if there's 3 or 4 Aces
        elif aceCount == 2 and (score + 12) <= 21:
            score = score + 12
        # If there are 3 Aces and the score won't bust, give +13 (11 + 1 + 1)
        elif aceCount == 3 and (score + 13) <= 21:
            score = score + 13
        # If there are 4 Aces and the score won't bust, give +14 (11 + 1 + 1 + 1)
        elif aceCount == 4 and (score + 14) <= 21:
            score = score + 14
        # If any Ace giving 11 would bust, simply give +1 for each Ace
        else:
            score = score + aceCount

    return score

# Function that determines the winner, the closest to 21
def DetermineWinner(pScore, dScore):
    # 0 = Player win state
    # 1 = Dealer win state
    # 2 = Draw state

    # Check for busts first
    if pScore > 21:
        return 1
    elif dScore > 21:
        return 0
    
    # If no busts, calculate score's distance from 21
    pDistance = 21 - pScore
    dDistance = 21 - dScore

    # Lowest distance wins, draw if equal
    if pDistance > dDistance:
        return 1
    elif dDistance > pDistance:
        return 0
    else:
        return 2