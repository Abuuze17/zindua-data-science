import random
number = random.randint(1, 100)

level = input("Choose difficulty (Easy/Medium/Hard): ").lower()

if level == "easy":
    attempts = 10
elif level == "medium":
    attempts = 7
elif level == "hard":
    attempts = 5
else:
    print("Invalid difficulty. Defaulting to Hard.")
    attempts = 5

for i in range(attempts):
    guess = int(input("Guess a number between 1 and 100: "))

    if guess == number:
        print(f" Congratulations! You guessed the number {number}.")
        break
    elif guess < number:
        print("Too Low")
    else:
        print("Too High")

    print(f"Guesses remaining: {attempts - i - 1}")

else:
    print(f"Game Over! The correct number was {number}.")