def alternate_merge(list1, list2):
    new_list = []
    min_len = min(len(list1), len(list2))
    
    for i in range(len(list1)):
        new_list.append(list1[i])
        new_list.append(list2[i])
    
    new_list.extend(list1[min_len:]) 
    new_list.extend(list2[min_len:])

    return new_list

print(alternate_merge([1,2,3], ['a',5,'b']))
print(alternate_merge([11,12,13], ['a',5,'b','d']))
