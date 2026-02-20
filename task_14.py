#compute sum using for loop
def sum_with_for_loop(my_list):
    sum_using_for: int = 0

    for i in range(len(my_list)):
        sum_using_for += my_list[i] 
    return sum_using_for

#compute sum using while loop
def sum_with_while_loop(my_list):
    sum_using_while: int = 0
    i : int = 0
    while(i < len(my_list)):
        sum_using_while += my_list[i] 
        i +=1
    return sum_using_while

#compute sum using recursion
def sum_with_recursion(my_list):
    if len(my_list) == 0:
        return 0
    else: 
        return my_list[0]+  sum_with_recursion(my_list[1:])


# Test cases 
print("Testing for loop")
print(sum_with_for_loop([1, 2, 3, 4, 5, 6]))  
print(sum_with_for_loop([10]))  
print(sum_with_for_loop([]))  
print(sum_with_for_loop([-1, 2, -3, 4, 5])) 

print("Testing while")
print(sum_with_while_loop([1, 2, 3, 4, 5, 6]))  
print(sum_with_while_loop([10]))  
print(sum_with_while_loop([]))  
print(sum_with_while_loop([-1, 2, -3, 4, 5])) 

print("Testing recursion")
print(sum_with_recursion([1, 2, 3, 4, 5, 6]))  
print(sum_with_recursion([10]))  
print(sum_with_recursion([]))  
print(sum_with_recursion([-1, 2, -3, 4, 5]))  
