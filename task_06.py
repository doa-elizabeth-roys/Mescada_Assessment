# Write a program that asks the user for a number n and gives them the possibility to                 
# choose between computing the sum and computing the product of 1,…, n 

def user_choice():
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input")
        
    user_choice = input("For addition, enter A and for multiplication enter M: ").upper()
    if user_choice == 'A':
        compute_sum(num)
    elif user_choice == 'M':
        compute_pdt(num)
    else:
        print("Invalid option")

def compute_sum(n):
    total_sum: int = 0

    for i in range(1,n+1):
        total_sum += i
    return display_ans(total_sum)

def compute_pdt(n):
    total_pdt: int = 1

    for i in range(1,n+1):
        total_pdt *= i
    return display_ans(total_pdt)

def display_ans(answer):
    print(answer)


user_choice()
