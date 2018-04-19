import sys
from typing import List, Tuple


def max_sub_array(start: int, end: int, the_array: List) -> Tuple[int, int, int]:
    if start == end:
        return start, end, the_array[start]
    else:
        middle: int = (end - start)//2
        print(middle)
        print(start)
        print(end)
        max_left = max_sub_array(start, middle, the_array);
        max_right = max_sub_array(middle + 1, end, the_array)
        max_middle = max_sub_middle_include(start, middle, end, the_array)
        if max_left[2] >= max_right[2] and max_left[2] >= max_middle[2]:
            return max_left
        elif max_right[2] >= max_left[2] and max_right[2] >= max_middle[2]:
            return max_right
        else:
            return max_middle


def max_sub_middle_include(start: int, middle: int, end: int, the_array: List) ->Tuple[int, int, int]:
    max_left = -sys.maxsize - 1
    max_right = -sys.maxsize - 1
    cur_left = 0
    left_index = middle
    for i in range(middle, start-1, -1):
        cur_left = cur_left + the_array[i]
        if cur_left>max_left:
            max_left = cur_left
            left_index = i
    cur_right = 0
    right_index = middle + 1
    for i in range(middle+1, end + 1):
        cur_right = cur_right + the_array[i]
        if cur_right > max_right:
            max_right = cur_right
            right_index = i
    return left_index, right_index , max_left + max_right


if __name__ == '__main__':

    result = max_sub_array(0, 2, [1, 2, 3])
    print(result)


