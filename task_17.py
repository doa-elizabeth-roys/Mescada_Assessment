def rotate_list(my_list, k):
    n = len(my_list)
    k = k % n

    for _ in range(k):
        my_list.append(my_list.pop(0))

    return my_list

print(rotate_list([1,2,3,4,5,6], 2))