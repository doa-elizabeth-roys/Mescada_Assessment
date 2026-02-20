def check_element(target, input_list):
    if len(input_list) == 0:
        return "Empty List"

    if target not in input_list:
        return f"{target} is not in list"

    if target == input_list[0]:
        return f"{target} is in list"
    else:
        return check_element(target, input_list[1:])


print(check_element(4, [2,4,5,6,8,9,12,33]))
print(check_element(20,[]))
print(check_element("grape", [1, "apple", 70, "banana"]))  
