# Heading
print("\n")
print("               *************************")
print("               ****                 ****")
print("               **  GK Quiz Challenge  **")
print("               ****                 ****")
print("               *************************")

# Welcome message
print("\nWelcome to my Computer Quiz\n")

confirm = input("Do you want to play a Game?(yes/no): ")
confirm = confirm.upper()

if confirm in ("Y", "YES"):
    pass
else:
    print("Thank You! Come back later")
    quit()
