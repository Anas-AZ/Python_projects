#Number Guessing Game Objectives:

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5

def guessFunction(difficulty,number):
  if difficulty=='easy':
    guessCount=EASY_LEVEL_TURNS #10 guess attempts for easy
  else:
    guessCount=HARD_LEVEL_TURNS  #5 guess attempts for hard

  for i in range (0,guessCount):
    print(f"You have {guessCount-i} attempts remaining to guess the number.")
    guess=int(input("Make a Guess: "))
    if guess < number:
      print("Too low")
    elif guess > number:
      print(f"Too high")
    else:
      print(f"You got it! The answer was {number}")
      return
    if i < guessCount-1:
      print("Guess again")
  print("You've run out of guesses, You lose")
  return


def game():
  print(logo)
  print("Welcome to the number guessing game!")
  print("I'm thinking of a number between 1 and 100")
  number=random.randint(1,100)
  #print(f"psst the correct answer is {number}")
  difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")
  guessFunction(difficulty,number)

game()
