def digit_to_list(digit):
    digit_list = []
    digit_len = len(str(digit))
    
    while digit > 0:
        num = digit % 10
        digit_list.append(num)
        digit = digit // 10     #remove last digit
    digit_list.reverse()

    return digit_list


print(digit_to_list(2342))
print(digit_to_list(345678))