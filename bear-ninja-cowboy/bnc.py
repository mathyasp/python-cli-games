# cli-games/bnc.py

# Import the random library
from random import randint

# Make an array
roles = ["Bear", "Ninja", "Cowboy"]

# Global variable for computer, player, player score
computer = roles[randint(0,2)]
player = False
score = 0

# Create a function to display a starting message
def get_ready():
    print("Get ready to play Bear, Ninja, Cowboy!")

# Create a function for instructions
def instructions(yes_no):
    if yes_no.lower() == "yes":
        print("Bear, Ninja, Cowboy is an exciting game of strategy and skill! Pit your wit against the computer! Choose a player: Bear, Ninja, or Cowboy. The computer chooses a player. Bear eats Ninja, Ninja defeats Cowboy and cowboy shoots bear.")
    else: 
        return

# Create a function to test if the user entry is valid
def valid_entry(user_entry):
    user_entry = user_entry.lower()

    if user_entry == "bear" or user_entry == "ninja" or user_entry == "cowboy":
        return True
    else:
        print(f"{user_entry} is not a valid entry. Please try again.")
        return False


# Create a function for the action that the winner takes
def winner_action(winner):
    winner = winner.lower()
    
    if winner == "bear":
        return("eats")
    elif winner == "ninja":
        return("defeats")
    elif winner == "cowboy":
        return("shoots")

# Create a function for winner or loser script that changes the score
def win_lose_script(user):
    global score
    if user == player:
        score += 1
        action = winner_action(player)
        print(f"You win! {player} {action} {computer}. Your score is: {score}")
    else:
        score -= 1
        action = winner_action(computer)
        print(f"You lose! {computer} {action} {player}. Your score is: {score}")

# Create a function to check if it's a tie
def check_winner(computer, player):
    global score, winner
    computer = computer.lower()
    player = player.lower()

    if computer == player:
        print("DRAW!")
    elif computer == "cowboy":
        if player == "bear":
            win_lose_script(computer)
        else: # computer is cowboy, player is ninja
            win_lose_script(player)
    elif computer == "bear":
        if player == "cowboy":
            win_lose_script(player)
        else: # computer is bear, player is ninja
            win_lose_script(computer)
    elif computer == "ninja":
        if player == "cowboy":
            win_lose_script(computer)
        else: # computer is ninja, player is bear
            win_lose_script(player)

def bear_ninja_cowboy():
    global player, computer
    get_ready()
    instructions(input("Would you like instructions? (yes/no) > "))
    computer = roles[randint(0,2)]

    while player == False:
        # Get player input
        player = input("Bear, Ninja, or Cowboy? > ")

        # Check if entry is valid
        if valid_entry(player) == False:
            player = False
            computer = roles[randint(0,2)]
        else:

            # Check for winner
            check_winner(computer, player)

            play_again = input("Would you like to play again? (yes/no) > ")
            if play_again == 'yes':
                player = False
                computer = roles[randint(0,2)]
            else:
                print("Thank you for playing.")
                break

bear_ninja_cowboy()