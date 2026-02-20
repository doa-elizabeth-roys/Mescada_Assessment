#  returns the largest element in a list. 

def largest_element(input_list):
    if len(input_list) == 0:
        return None
    elif len(input_list) > 0:
        try:
            input_list.sort(reverse=True)
            return input_list[0]
        except TypeError:
            return "TypeError: Check the list"
            

print(largest_element([3,5,2,6,7,55,66,2,4,8,34,10])) #expects 66
print(largest_element([])) # None 
print(largest_element([3,5,2,6,7,55,66,'a'])) # typeError
