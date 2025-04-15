""""
## Skyline Problem
Imagine a skyline of buildings and you were standing in front of them at ground level 0. How many of these buildings could you see?

Given a list [-1, 1, 3, 7, 7, 3] determine which values could be "seen."

The output should be: [1,3,7]

Write your clarifying questions and implementation in `skyline.py`. To execute your code, run `python3 skyline.py` in the terminal.

![Image representing person looking at a skyline of buildings](assets/skyline_problem_image.png)
"""

# Add your clarifying questions here
# What if the list is empty? Return an empty list.
# What is expected the input and output format? A list of integers representing building heights.
# How do we define visibility? A building is visible if it is taller than all the buildings to its left.
# How should we return the result? We need to return the list of visible buildings in the order they are seen from left to right.
# What if the list has only one building? Return a list with that building's height.
# What if the list has negative values? Ignore them, as they don't represent valid building heights.
# What if the list has duplicate values? Only include unique heights in the output.
# What if the list has non-integer values? Ignore them, as they don't represent valid building heights.
# What if the list has a mix of:  positive and negative values, integers and floats(strings, None) ? Only consider positive integers and floats, and ignore negative values, strings, and None.

def skyline(building_list):

    if not building_list:
        return []
    
    visible_buildings = []
    max_height = 0
    
    for height in building_list:
        try:
            # Raise an exception if height is invalid (either negative or not a number)
            if height <= 0:
                raise ValueError("Invalid height: must be a positive number.")
            
            if height > max_height:
                visible_buildings.append(height)
                max_height = height
        except (ValueError, TypeError):
            continue
            
    return visible_buildings

print(skyline([-1, 1, 3, 7, 7, 3, 'a', None, 5.5, 6]))

print(skyline([1, 3, 2, 5, 4]))
