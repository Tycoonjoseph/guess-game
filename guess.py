import random
computer_guess = random.randint(1, 100)
user_guess = None

guess_count = 0
max_guesses = 10


while user_guess != computer_guess:
    user_guess = int(input('Guess a number between 1 and 100: '))
    guess_count += 1
    if user_guess < computer_guess:
        print('Too low! Try again.')
    elif user_guess > computer_guess:
        print('Too high! Try again.')
    else:
        print('Congratulations! You guessed the number!')
    max_guesses = 10
    if guess_count >= max_guesses:
        print(f'Sorry! The number was {computer_guess}.')
        break

while True:
    try:
        user_guess = int(input('Guess a number between 1 and 100: '))
        break
    except ValueError:
        print("Please enter a valid number!")
print(f'It took you {guess_count} guesses.')
