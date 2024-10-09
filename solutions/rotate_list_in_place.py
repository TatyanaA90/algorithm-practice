from math import gcd  # greatest common divisor

# time: O(n), where n is the length of the list, since we must visit each value in the list
# space: O(1), the only extra memory we make are scalar (not lists). We only copy a single extra list value at any given time.
def rotate_list(list, shift_by):
    list_len = len(list)
    shift_by = shift_by % list_len  # remove any repetition in the rotations
    offset = list_len - shift_by

    # find the number of interleaved bands we need to rotate
    bands = gcd(list_len, shift_by)  # O(log(min of the two args)), both are no larger than the len (n), so at most this is O(log n), which is less than the O(n) this appraoch otherwise takes

    # process each band (we could move the loop body to a helper function to rotate one band)
    # Notice that even though there is a nested list, this will not become quadratic.
    # If there are N items, and B bands (outer loop), then each band will have N / B items for a total of N items processed overall.
    for start in range(bands):
        last_pos = start
        first_value = list[last_pos]  # set aside the value at the current start
        next_pos = (start + offset) % list_len

        # loop until we reach the end of this band (where next_pos would loop back to start)
        while next_pos != start:
            # copy from next value back to opening made by moving the last value
            list[last_pos] = list[next_pos]
    
            last_pos = next_pos
    
            # advance the position, accounting for wrapping past the end of the list
            next_pos = (next_pos + offset) % list_len
    
        # fill in the last shifted value with the value we originally set aside
        list[last_pos] = first_value
