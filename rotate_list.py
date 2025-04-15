# Add your clarifying questions here
# Should our function account for a negative shift_by number? No, all shift_by values will be positive.
# What if the shift_by num is greater than the length of the list? We can still calculate a list that gets rotated
# What happens with an empty list or a list with one value? If empty, return the empty list. If the list has 1 value, return the list.
# What if the shift_by value is invalid (0, None, "")? Return None
# Will a list ever have non-numeric values? Yes, rotate a list regardless of the data types in it
# Will the shift always to the right? Yes, always to the right



def rotate_list(list, shift_by):
    if shift_by < 0:
        raise ValueError("shift value must be positive")
    
    shift_by %= len(list) #[0, len(list)-1] keep the shift_by == length of the list
    
    rotated_list = []
    start =len(list) - shift_by

    for _ in range(len(list)):
        if start >= len(list):
            start = 0
        rotated_list.append(list[start])
        start += 1  
    
    return rotated_list

print(rotate_list([1, 2, 3, 4, 5], 2)) 
print(rotate_list([1, 2, 3, 4, 5], 0)) 