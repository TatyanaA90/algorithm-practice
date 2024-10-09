# Some example clarifying questions:

# Should our function account for a negative shift_by number? No, all shift_by values will be positive.
# What if the shift_by num is greater than the length of the list? We can still calculate a list that gets rotated
# What happens with an empty list or a list with one value? If empty, return the empty list. If the list has 1 value, return the list.
# What if the shift_by value is invalid (0, None, "")? Return None
# Will a list ever have non-numeric values? Yes, rotate a list regardless of the data types in it

def rotate_list(list, shift_by):
    pass

# Review files in the solutions directory to see example solutions for this problem.

# Example test cases
assert rotate_list([1, 2, 3, 4, 5], 6) == [5, 1, 2, 3, 4]
assert rotate_list([], 3) == []
assert rotate_list(["dog"], 4) == ["dog"]
assert rotate_list(["dog", 1, 4, "bird"], None) == None
assert rotate_list([1, 2, "!", 4, "hello"], 6) == ["hello", 1, 2, "!", 4]