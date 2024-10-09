# time: O(n), where n is the length of the list, since we must visit each height in the list
# space: O(n), where n is the length of the list, since we make a copy for the result
def skyline(building_list):
    highest_value = 0  # can't see anything until it's taller than 0
    result = []

    for height in building_list:
        if height > highest_value:
            result.append(height)

            # update the tallest height to what we just found
            highest_value = height

    return result
