"""
Multiple choice question and answers game
"""
import sys
import time
import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Gk_Quiz_Challenge')

score_details = SHEET.worksheet('score_details')


# Heading
print(' ')
print('               *************************')
print('               **                     **')
print('               **  GK Quiz Challenge  **')
print('               **                     **')
print('               *************************')
time.sleep(1)
# Welcome message
print('\nWelcome to my Computer Quiz\n')

# confirmation whether the user want to play the game
confirm = input('Do you want to play a Game?(yes/no): \n')
confirm = confirm.upper()


if confirm in ('Y', 'YES'):
    pass
else:
    print('Thank You! Come back later')
    sys.exit()

time.sleep(0.5)
# Enter Name of the user, Game doesnot start without Name details.
while True:
    name = input('Please Enter Your Name: \n')
    if not name:
        print('Please Enter your Name before start: \n')
    else:
        print("Hi", name, "Let's start the Game")
        print('There are 15 questions to answer. Best of Luck!!!\n')
        break
time.sleep(0.5)


def start():
    """
    Game Starts here and answer the questions
    """
    choices = []
    correct_choices = 0
    question_num = 1

    for key in questions:
        print('**********************************************************')
        print(key)
        for i in options[question_num - 1]:
            print(i)

        while True:
            choice = input('Enter Your Answer (A,B,C or D): \n')
            if choice not in ('A', 'B', 'C', 'D', 'a', 'b', 'c', 'd'):
                print("Please Enter a Valid options")
            else:
                break
        choice = choice.upper()
        choices.append(choice)
        correct_choices += check_answer(questions.get(key), choice)
        question_num += 1
    display_score(correct_choices)


time.sleep(0.5)


def check_answer(answer, choice):
    """
    Feedback given for right and wrong answer
    """
    if answer == choice:
        print('\n Well done! Correct Answer!\n')
        return True
    print('\n Incorrect Answer\n')
    return False


def display_score(correct_choices):
    """
    Score display in terms of number of questions been answer correctly.
    And Calculate the score in percentage too
    """
    print('**********************************************************')
    print('             ---------------------------')
    print('             |       Quiz Results      |')
    print('             ---------------------------\n')
    score = int(correct_choices)
    print('Thank you for playing! You got', score, '/',
          len(questions), 'questions correct.')
    mark = int(score/len(questions) * 100)
    print('Hi', name, ', Your Score is:', str(mark), '%.\n')
    marks = mark / 100

    user = [name, score, marks]
    score_details.append_row(user)
    result = score_details.get_all_values()
    print("Other Players Scores are below:\n")
    pprint(result)


time.sleep(1)


def play_again():
    """
    Choice given the player repeat the game
    """
    response = input('Do you want to Play again:(yes or no): \n')
    response = response.upper()
    if response in ('Y', 'YES'):
        return True
    if response in ('N', 'NO'):
        return False
    print('Please Enter Valid option (yes or no).')
    return play_again()


# questions and correct answer in dictionaries method
questions = {
    '1. What is the square root of 144?\n ': 'A',
    "2. Which Country is known as the 'Playground of Europe'?\n": 'C',
    '3. What percentage of the human body is water?\n': 'B',
    '4. What is the hottest Chilli Pepper in the World?\n': 'A',
    '5. Which Country has the biggest Land Area?\n': 'D',
    '6. How many legs does a butterfly have?\n': 'B',
    '7. What is the popular spice in the world?\n': 'A',
    '8. What kind of tree do acorns grow on?\n': 'C',
    '9. Which Country has the most Volcanoes?\n': 'D',
    '10. Which country is the largest producer of Coffee??\n': 'B',
    '11. Which is the hottest planet is the Solar system?\n': 'D',
    '12. Which European Country was the first to allow women to vote?\n':
    'A',
    '13. What is the degree of triangle?\n': 'C',
    '14. What is the Chemical symbol for table salt?\n': 'D',
    '15. What is the largest three digit prime Number?\n': 'B'

}


# multiple choice answers in list methods
options = [
    ['A. 12', 'B. 22', 'C. 14', 'D. 11\n'],
    ['A. Austria', 'B. France', 'C. Switzerland', 'D. Italy\na'],
    ['A. 75%', 'B. 60%', 'C. 69%', 'D. 65%\n'],
    ['A. The Carolina Reaper', 'B. Ghost Pepper', 'C. Pot Barrackpore',
     'D. Pot Red\n'],
    ['A. China', 'B. India', 'C. Africa', 'D. Russia\n'],
    ['A. Four', 'B. Six', 'C. Eight', 'D. Two\n'],
    ['A. Pepper', 'B. Paprika', 'C. Thyme', 'D. Chilli\n'],
    ['A. Ash', 'B. Birch', 'C. Oak', 'D. Rowan\n'],
    ['A. Japan', 'B. Russia', 'C. Chile', 'D. Indonesia\n'],
    ['A. Vietnam', 'B. Brazil', 'C. Colombia', 'D. Ethiopia\n'],
    ['A. Jupitar', 'B. Mars', 'C. Mercury', 'D. Venus\n'],
    ['A. Finland', 'B. Germany', 'C. France', 'D. Ireland\n'],
    ['A. 240 degree', 'B. 360 degree', 'C. 180 degree', 'D. 90 degree\n'],
    ['A. Sodium hydroxide', 'B. Sodium bicarbonate', 'C. Sodium Carbonate',
     'D. Sodium Chloride\n'],
    ['A. 995', 'B. 997', 'C. 999', 'D. 993\n'],
]


start()

while play_again():
    start()

print('Thanks for Playing this Game!')
