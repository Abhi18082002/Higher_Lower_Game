#displayART
from art import logo, vs
from game_data import data
import random


def format_data(account):
    """format the acc data into printable format"""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return (f"{account_name},{account_desc},{account_country}")



def check_answer(user_guess, a_followers, b_followers):

    """ take the users guess and follower acc and returns  if got it right"""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    #generate a random acc from the data

    # Making accounts at pos B at A

    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # guess who has more followers
    guess = input("Who has more followers? Type 'A' or 'B':").lower()

    #clear the screen
    print("\n" * 15)
    print(logo)

    # check if user is correct
    ## get follower count of each acc
    a_follower_account = account_a["follower_count"]
    b_follower_account = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_account,b_follower_account)


    # use if statement to check if user is correct
    if is_correct:
        score += 1
        print(f"You are right: Current score is {score} ")
    else:
        print(f"oopppssss....That's wrong: Final score {score}")
        game_should_continue = False




