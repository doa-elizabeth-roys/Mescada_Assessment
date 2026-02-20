def print_in_frame(string_list):
    max_len = max(len(s) for s in string_list)  
    print('*' * (max_len + 4))

    for i in range(len(string_list)):
        print(f"* {string_list[i]} *\n")
    print('*' * (max_len + 4))  
    

print_in_frame( ["Hello", "World", "in", "a", "frame"])