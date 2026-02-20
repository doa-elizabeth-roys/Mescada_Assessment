def multiplication_table(multiplicand):
    for m in range(1, 13):
        print(f"{multiplicand} * {m} = {multiplicand * m}" )
        m +=1

try:
    num = int(input("Enter a number: "))
    multiplication_table(num)
except ValueError:
        print("Invalid input")