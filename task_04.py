def sumOfNumbers(n):
    total_sum: int = 0

    for i in range(1,n+1):
        total_sum += i
    return total_sum

try:
    num = int(input("Enter a number: "))
    print(f"Sum of numbers from 1 to {num} is {sumOfNumbers(num)}")

except ValueError:
    print("Invalid input")



