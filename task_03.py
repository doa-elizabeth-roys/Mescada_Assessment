user_1 = 'ALICE'
user_2 = 'BOB'

def greet_user(name):
    print(f"Hello {name}")

print("Enter your name")
name = input()

while name == "":
    print("Name cannot be empty")
    print("Enter your name")
    name = input()

    if name.upper() == user_1 or name.upper() == user_2:
        greet_user(name)
    else:
        print("\nHello")
