import sys
sys.path.append('.')
import blackjackFunctions as app

# Open terminal in \blackjack
# Run tests with the following command:
# $ pytest -q blackjackTests.py

def test_isInt1():
    # string is '108', result should be True
    string = '108'
    assert app.isInt(string) == True

def test_isInt2():
    # string is '108.1', result should be False
    string = '108.1'
    assert app.isInt(string) == False

def test_isInt3():
    # string is '108i', result should be False
    string = '108i'
    assert app.isInt(string) == False

def test_RemoveLetters1():
    # input is '7 of Diamonds', output should be '7'
    input = '7 of Diamonds'
    assert app.RemoveLetters(input) == '7'

def test_RemoveLetters2():
    # input is 'Hearts suit, 10 card', output should be '10'
    input = 'Hearts suit, 10 card'
    assert app.RemoveLetters(input) == '10'

def test_RemoveLetters3():
    # input is 'Qu33n 0f Sp4d35', output should be '330435'
    input = 'Qu33n 0f Sp4d35'
    assert app.RemoveLetters(input) == '330435'

def test_RemoveLetters4():
    # input is 'Four, Eight, 15, Sixteen, 23, Forty-two', output should be '1523'
    input = 'Four, Eight, 15, Sixteen, 23, Forty-two'
    assert app.RemoveLetters(input) == '1523'

def test_RemoveLetters5():
    # input is a string of randomly-typed letters, output should be an empty string ('')
    input = 'gkjseogjfiosjgfoiejfkopiaskfoieakoifajgioejkiaog'
    assert app.RemoveLetters(input) == ''

def test_checkScore1():
    # hand is 2, 1, 1, 10, result should be 13
    testHand = ['2 of Clubs', 'Ace of Spades', 'Ace of Clubs', 'Queen of Clubs']
    assert app.CheckScore(testHand) == 14

def test_checkScore2():
    # hand is 3, 11, 1, result should be 15
    testHand = ['3 of Spades', 'Ace of Hearts', 'Ace of Diamonds']
    assert app.CheckScore(testHand) == 15

def test_checkScore3():
    # hand is 2, 11, 1, 1, 1, 5, result should be 21
    testHand = ['2 of Clubs', 'Ace of Spades', 'Ace of Clubs', 'Ace of Diamonds', 'Ace of Hearts', '5 of Hearts']
    assert app.CheckScore(testHand) == 21

def test_checkScore4():
    # hand is 10, 10, result should be 20
    testHand = ['Clubs suit, King card', 'Hearts suit, Jack card']
    assert app.CheckScore(testHand) == 20

def test_DetermineWinner1():
    # Both scores are 21, result should be draw (2)
    testpScore = 21
    testdScore = 21
    assert app.DetermineWinner(testpScore, testdScore) == 2

def test_DetermineWinner2():
    # Despite having a lower score, result should be player win (0) since dealer busts
    testpScore = 12
    testdScore = 22
    assert app.DetermineWinner(testpScore, testdScore) == 0

def test_DetermineWinner3():
    # Result should be dealer win (1) because their score is closer to 21
    testpScore = 15
    testdScore = 16
    assert app.DetermineWinner(testpScore, testdScore) == 1