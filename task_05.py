def sumOfNumbers(n):
    total_sum: int = 0

    for i in range(1,n+1):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i
    return total_sum

try:
    num = int(input("Enter a number: "))
    print(f"Sum of numbers from 1 to {num} which is divisible by 3 or 5 is {sumOfNumbers(num)}")

except ValueError:
    print("Invalid input")
