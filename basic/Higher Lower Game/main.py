from art import *
from game_data import data
from replit import clear
import random

def get_random_account():
  """Get data from random account """
  return random.choice(data)

def format_data(account):
  """Convert the account data into printable format """
  name=account["name"]
  description=account["description"]
  country=account["country"]
  return f"{name}, a {description} from {country}"

def more_followers(account_a,account_b):
  """Returns the account with more followers """
  if account_a["follower_count"] > account_b["follower_count"]:
    return account_a
  else:
    return account_b


def compare(guess,account_a,account_b):
  """Compares the guess with other account"""
  if guess=="a":
    account=account_a
  else:
    account=account_b
  
  if account==more_followers(account_a,account_b):
    return True
  return False


def game():
  print(logo)
  right=True
  score=0
  account_a=get_random_account()
  account_b=get_random_account()

  while right:

    account_a=account_b
    account_b=get_random_account()
    while account_a==account_b:
      account_b=get_random_account()
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    guess=input("Who has more followers? Type 'A' or 'B': ").lower()
    result=compare(guess,account_a,account_b)

    if result==False:
      clear()
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score} ")
      right=False
    else:
      score+=1
      clear()
      print(logo)
      print(f"You are right. Current score {score}")

game()


