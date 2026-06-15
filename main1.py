
        
import random

# 1 = Snake
# -1 = Water
# 0 = Gun

computer = random.choice([1, -1, 0])

youStr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()

youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Check for valid input
if youStr not in youDict:
    print("Invalid choice! Please enter s, w, or g.")
else:
    you = youDict[youStr]

    print(f"You chose {reverseDict[you]}")
    print(f"Computer chose {reverseDict[computer]}")

    if computer == you:
        print("It's a draw!")

    elif (you == 1 and computer == -1) or \
         (you == -1 and computer == 0) or \
         (you == 0 and computer == 1):
        print("You win!")

    else:
        print("You lose!")
        