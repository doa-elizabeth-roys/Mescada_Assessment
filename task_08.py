import random
previous_guess = []
secret_num = random.randint(0, 100)
print(secret_num)

def guess_game(user_guess):
    total_tries: int = 0
    
    previous_guess.append(user_guess)
    if user_guess not in previous_guess:    
        total_tries +=1

    # while (secret_num != user_guess):
    if user_guess > secret_num:
            print("Your guess is too large. Try again")
            get_userInput()
    elif user_guess < secret_num:
            print("Your guess is too small. Try again")
            get_userInput()
    elif  user_guess in previous_guess:
            print("You already guessed this number.Try again")
            get_userInput()
    else:
            print(f"You have correctly guessed the secret number {secret_num} in {total_tries} tries")
            print(previous_guess)


def get_userInput():
    try:
        num = int(input("Guess a secret number between 1 to 100: "))
        guess_game(num)
    except ValueError:
        print("Invalid input")
        get_userInput()

get_userInput()