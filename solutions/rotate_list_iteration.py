# time: O(n), where n is the length of the list, since we must visit each value
# space: O(n), where n is the length of the list, since we make a copy for the result
def rotate_list(list, shift_by):
    result = []
    list_len = len(list)
    shift_by = shift_by % list_len  # remove any repetition in the rotations
    start_pos = list_len - shift_by

    # we don't need the iteration varibale, so a common convention is to call it _
    for _ in range(list_len):
        # wrap if the source location moves beyond the end of the list
        if start_pos >= list_len:
            start_pos = 0

        result.append(list[start_pos])
        start_pos += 1

    return result
