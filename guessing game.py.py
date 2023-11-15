import random
print("Welcome to the guess the number game!")
print("I've selected a random number between 1 and 100")
print("Can you guess what it is?")

correct_number = random.randint(1, 100)
counter = 1
guess = int(input("Enter your guess"))

while guess != correct_number:
    if guess > correct_number:
        print("Too high! Try again")
    else:
        print("Too low! Try again")
    counter = counter + 1
    print()
    guess = int(input("Enter a guess"))
    
print(f"Congradulations!You guessed the {correct_number} in {counter} attempts!")