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
