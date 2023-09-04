# flashcards.py
import json

# initialize global variable 'score' as 0
score = 0

# initialize global variable 'total' as 0
total = 0

# initialize global variable 'game_started' as False
game_started = False

# function to read in the json file
def read_data(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
        return data

# function to check if user answer is correct
def grader(correct_answer, user_answer):
    global score
    #Make input case insensitive
    if correct_answer.lower() == user_answer.lower():
        # increment score up one
        score += 1
        # interpolate score and total into the response
        print(f"Correct! Current score: {score}/{total}")
        return True
    else:
        print("Incorrect! The correct answer was", correct_answer)
        print(f"Current score: {score}/{total}")
        return False
        
# function to display game messages
def start_end_message():
    if game_started:
        print("Welcome to the Capital Guessing Game. Can you guess the correct Capital?")
    else:
        print("Thank you for playing the Capital Guessing Game!")

# add an end game message as a function
def final_score(score, total):
    if score < (total / 2):
        print("Less than half correct: You need to study!")
    elif score > (total / 2) and score != total:
        print(f"Good work! You scored {score}/{total}")
    else:
        print(f"A perfect score! You scored: {score} out of {total} correct!")

# function for the actual game play
def Capital_Guessing_Game():
    global total
    game_started = True
    data = read_data('me-capitals.json')
    total = len(data["cards"])
    
    start_end_message()
    for i in data["cards"]:
        guess = input(i["q"] + " > ")
        grader(i["a"], guess)
        
    final_score(score, total)
    game_started = False
    start_end_message()

# run the game
Capital_Guessing_Game()

