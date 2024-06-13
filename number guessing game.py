import random
print("\n   ***** WELCOME TO THE NUMBER GUESSING GAME *****\n\n")
print("Guess a number between 1-50 numbers.")
number = random.randint(1,50)
guess = 0

while guess != number:
    guess = int(input("Enter your Guess: "))
    
    if guess < number:
        print("\nYOUR GUESS IS LOW...!\n")
        
    elif guess > number:
        print("\nYOUR GUESS IS HIGH...!\n")
        
    else:
        print("\n\n*** YOU WON THE GAME ***\n\n")
        