# time: O(n^2), where n is the length of the list, since this rotates by 1 position (n moves) up to (n-1) offsets. n * (n-1) => O(n^2)
# space: O(1), the only extra memory we make are scalar (not lists). We only copy a single extra list value at any given time, and we modify in place
def rotate_list(list, shift_by):
    # handle shift_by being larger than the list length
    shift_by %= len(list)

    # outer loop runs shift_by - 1 times, but we don't need the number. _ is commonly used as a throw away variable
    for _ in range(0, shift_by):
        temp = list[-1]  # set aside the value at the end

        # shift everything to the right by one place
        for i in range(len(list) - 1, 0, -1):
            list[i] = list[i - 1]

        list[0] = temp  # replace the first value with the value that rotated of the end

    return list