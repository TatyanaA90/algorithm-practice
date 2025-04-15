import pytest
from skyline import skyline


def test_empty_list():
    input_data = []
    assert skyline(input_data) == []


def test_skyline_input_output_format():
    input_data = [1, 3, 2, 5, 4]
    expected_output = [1, 3, 5]  # Only 1, 3, and 5 should be visible

    result = skyline(input_data)

    assert isinstance(result, list), f"Expected result to be a list, but got {type(result)}"
    
    # Check if each item in the result is a positive integer
    for height in result:
        assert isinstance(height, int) and height > 0, f"Invalid height {height}: Expected a positive integer"
    
    # Check if the result matches the expected output
    assert result == expected_output
    

def test_single_building():
    result = skyline([5])
    assert result == [5]  # The single building is visible


def test_all_visible_buildings():
    result = skyline([1, 2, 3, 4, 5])
    assert result == [1, 2, 3, 4, 5]  # All buildings are visible

def test_visible_buildings_order():
    result = skyline([1, 3, 2, 5, 4, 7])
    assert result == [1, 3, 5, 7] 

def test_no_visible_buildings():
    result = skyline([-1, -2, -3])
    assert result == []  # No buildings are visible


def test_mixed_buildings():
    result = skyline([-1, 1, 3, 7, 7, 3])
    assert result == [1, 3, 7]  # Only the taller buildings are visible


def test_mixed_types():
    result = skyline([-1, 1, 3, 7, 7, 3, 'a', None, 5.5, 6])
    assert result == [1, 3, 7]  # Only the taller buildings are visible


def test_negative_values():
    result = skyline([-1, -2, -3, 4, 5])
    assert result == [4, 5]  # Only the positive buildings are visible


def test_duplicate_values():
    result = skyline([1, 2, 2, 3, 3, 4])
    assert result == [1, 2, 3, 4]  # Only unique heights are visible


