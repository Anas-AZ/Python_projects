
import random
from replit import clear
from art import logo

def dealCard():
  """Returns a random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)


def calculateScore(arr):
  """Take a list of cards and return the score calculated from the cards"""
  score=sum(arr)   #sum() calculates the sum of all elements in the list
  
  if len(arr)==2  and score==21:
    return 0  
  if 11 in arr and score > 21:    
    arr.remove(11)  #The remove() method removes the first matching element
    arr.append(1)
    
  return sum(arr) 

  
def compare(userScore,computerScore):
  """Compares the Scores of User and Computer"""
  if userScore==computerScore:
    return "Draw"
  elif computerScore==0:
    return "Lose, opponent has Blackjack"
  elif userScore==0:
    return "Win with a Blackjack"
  elif userScore > 21:
    return "You went over, You Lose"
  elif computerScore > 21:
    return "Computer went over, You Win"
  elif userScore > computerScore:
    return "You Win"
  else:
    return "You Lose"

def playGame():
  print(logo)
  #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
  user_cards = []
  computer_cards = []
  gameOver=False

  for i in range(2):
    user_cards.append(dealCard())
    computer_cards.append(dealCard())
    
  while not gameOver:
    userScore=calculateScore(user_cards)
    computerScore=calculateScore(computer_cards)
    print(f"your cards: {user_cards}  current score: {userScore}")
    print(f"Computer's first card: {computer_cards[0]}")
    if computerScore==0 or userScore==0 or userScore > 21:
      gameOver=True
    else:
      drawAgain=input("Type 'y' to get another card, type 'n' to pass: ")
      if drawAgain=='y':
        user_cards.append(dealCard())
      else:
        gameOver=True

        
  while computerScore != 0 and computerScore <=17:
    computer_cards.append(dealCard()) 
    computerScore=calculateScore(computer_cards)

  print(f"Your final hand: {user_cards}, final score: {userScore} ")
  print(f"Computer's final hand: {computer_cards}, final score: {computerScore} ")
  print(compare(userScore,computerScore))
 

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")=='y':
  clear()
  playGame()


