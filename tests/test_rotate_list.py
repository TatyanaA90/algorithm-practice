import pytest
from rotate_list import rotate_list

def test_rotate_right():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

def test_empty_list():
    with pytest.raises(ZeroDivisionError):
        rotate_list([], 1)

def test_single_element():    
    assert rotate_list ([9], 1) == [9]

def test_negative_shift():
    list_to_rotate = [1, 2]
    shift_value = -1

    try:
        rotate_list(list_to_rotate, shift_value) 
        assert False, "Expected ValueError was not raised" 
    except ValueError as excepted:
        assert str(excepted) == "shift value must be positive", f"Expected 'shift value must be positive', but got {str(excepted)}"

def test_shift_greater_than_length():

    list_to_rotate = [1, 2, 3, 4, 5]
    shift_value = 7 
    
    expected_result = [4, 5, 1, 2, 3]  
    
    result = rotate_list(list_to_rotate, shift_value)
    
    assert result == expected_result, f"Expected {expected_result}, but got {result}"