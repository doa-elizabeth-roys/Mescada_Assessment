def odd_position_element(input_list):
    if len(input_list) == 0:
        return "Empty List"
    else:
        return input_list[1::2]
    

print(odd_position_element([1,2,3,4,5,6,7,8,9]))
print(odd_position_element([]))
print(odd_position_element(["hello", "world", "good", "morning","thanks"]))
print(odd_position_element([10]))