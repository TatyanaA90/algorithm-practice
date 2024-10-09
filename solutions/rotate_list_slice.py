# time: O(n), where n is the length of the list, since we must concatenate the lists (which visits each one). The slice itself will also be O(n)
# space: O(n), where n is the length of the list, since we make a copy for the joined lists and for the result
def rotate_list(list, shift_by):
    # by concatenating two copies, we can ignore the need to wrap at the end
    result = list + list
    list_len = len(list)
    shift_by = shift_by % list_len  # remove any repetition in the rotations
    start_pos = list_len - shift_by

    return result[start_pos:start_pos + len(list)]
