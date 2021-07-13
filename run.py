# Heading
print("\n")
print("               *************************")
print("               ****                 ****")
print("               **  GK Quiz Challenge  **")
print("               ****                 ****")
print("               *************************")

# Welcome message
print("\nWelcome to my Computer Quiz\n")

# confirmation whether the user want to play the game
confirm = input("Do you want to play a Game?(yes/no): ")
confirm = confirm.upper()

if confirm in ("Y", "YES"):
    pass
else:
    print("Thank You! Come back later")
    quit()

"""
Enter Name of the user, Game doesnot start without
Name details.
"""
while True:
    name = input("Please Enter Your Name: ")
    if not name:
        print("Please Enter your Name before start: ")
    else:
        print("Hi", name, "Let's start the Game")
        break


def start():
    """
    Game Start and answer the questions
    """
    question_num = 1

    for key in questions:
        print("****************************************************")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        question_num += 1


questions = {
    "1. which Country is known as the 'land of Raising Sun'?\n ": "A",
    "2. Which Country is known as the 'Playground of Europe'?\n": "C",
    "3. What percentage of the human body is water?\n": "B",
    "4. What is the hottest Chilli Pepper in the World?\n": "A",
    "5. Which Country has the biggest Land Area?\n": "D",
    "6. How many legs does a butterfly have?\n": "B",
    "7. What is the popular spice in the world?\n": "A",
    "8. What kind of tree do acorns grow on?\n": "C",
    "9. Which Country has the most Volcanoes?\n": "D",
    "10. What is the most spoken language in the world?\n": "B",
    "11. Which is the hottest planet is the Solar system?\n": "D",
    "12. Which European Country was the first to allow women to vote?\n": "A",
    "13. What is the degree of triangle?\n": "C",
    "14. What is the Chemical symbol for table salt?\n": "D",
    "15. What is the largest three digit prime Number?\n": "B"

}

options = [
    ["A. Japan", "B. New Zealand", "C. Fiji", "D. China\n"],
    ["A. Austria", "B. France", "C. Switzerland", "D. Italy"],
    ["A. 75%", "B. 60%", "C. 69%", "D. 65%\n"],
    ["A. The Carolina Reaper", "B. Ghost Pepper", "C. Pot Barrackpore"
     "D. Pot Red\n"],
    ["A. China", "B. India", "C. Africa", "D. Russia\n"],
    ["A. Four", "B. Six", "C. Eight", "D. Two\n"],
    ["A. Pepper", "B. Paprika", "C. Thyme", "D. Chilli\n"],
    ["A. Ash", "B. Birch", "C. Oak", "D. Rowan\n"],
    ["A. Japan", "B. Russia", "C. Chile", "D. Indonesia\n"],
    ["A. English", "B. Chinese", "C. German", "D. French\n"],
    ["A. Jupitar", "B. Mars", "C. Mercury", "D. Venus\n"],
    ["A. Finland", "B. Germany", "C. France", "D. Ireland\n"],
    ["A. 240 degree", "B. 360 degree", "C. 180 degree", "D. 90 degree\n"],
    ["A. Sodium hydroxide", "B. Sodium bicarbonate", "C. Sodium Carbonate",
     "D. Sodium Chloride\n"],
    ["A. 995", "B. 997", "C. 999", "D. 993\n"],
]


start()
