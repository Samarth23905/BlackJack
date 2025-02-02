import random 
def dealCard():
    """returns a random card from the list"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculateScore(cards):
    """take up the list of cards and calculate the score"""
    if sum(cards) == 21 and 11 in cards and len(cards) == 2:
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
    return sum(cards)

def comparing(uScore, cScore):
    if uScore == cScore:
        return "It's a Draw!"
    elif uScore == 0:
        return "You Win! You have a black jack"
    elif cScore == 0:
        return "You Lose! Computer has a black jack"
    elif uScore > 21:
        return "You Lose!"
    elif cScore > 21:
        return "You Win!"
    elif cScore > 21 and uScore > 21:
        return "Both computer and you exeeded the max score!"
    elif uScore > cScore:
        return "You Win!"
    else:
        return "You Lose!"

userCard = []
computerCard = []
computerScore = -1
userScore = -1

gameOver = True
for _ in range(2):
    userCard.append(dealCard())
    computerCard.append(dealCard())
# for user play to draw the cards unless they type n or till the get the score exceeded over 21 
while gameOver:
    userScore = calculateScore(userCard)
    computerScore = calculateScore(computerCard)
    print(f"Your cards: {userCard} and your current score: {userScore}")
    print(f"Computer's first card is {computerCard[0]}")

    if userScore == 0 or computerScore == 0 or userScore > 21 or computerScore > 21:
        gameOver = False
    else:
        choice = input("Type 'Y' to draw another card or type 'N' to pass.").lower()
        if choice == "y":
            userCard.append(dealCard())
        else:
            gameOver = False

# for computer play
while computerScore != 0 and computerScore < 17:
    computerCard.append(dealCard())
    computerScore = calculateScore(computerCard)

print(f"Your final cards: {userCard} and your final score: {userScore}")
print(f"Computer's final cards are {computerCard} and computer's final score: {computerScore}")
print(comparing(userScore, computerScore))