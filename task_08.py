import random

secret_num = random.randint(1, 100)
previous_guess = []  
total_tries = 0  

def guess_game(user_guess):
    global total_tries 
    
    if user_guess in previous_guess:
        print("You already guessed this number. Try again.")
        return 
   
    previous_guess.append(user_guess)
    total_tries += 1  

    if user_guess > secret_num:
        print("Your guess is too large. Try again.")
    elif user_guess < secret_num:
        print("Your guess is too small. Try again.")
    else:
        print(f"Congratulations! You guessed the secret number {secret_num} in {total_tries} tries.")
        print(f"Previous guesses: {previous_guess}")


def get_user_input():
    while True:
        try:
           
            num = int(input("Guess a secret number between 1 and 100: "))
            guess_game(num)  
         
            if num == secret_num:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")


get_user_input()
