# time: O(n), where n is the length of the list, since we must visit each height in the list
# space: O(n), where n is the length of the list, since we make a copy for the result
def skyline(building_list):
    is_visible = []
    if building_list:
        for i in range(0, len(building_list)):
            if ((building_list[i] > 0 and is_visible == [])
                or (building_list[i] > 0 and building_list[i] > is_visible[-1])):
                is_visible.append(building_list[i])
    
    return is_visible