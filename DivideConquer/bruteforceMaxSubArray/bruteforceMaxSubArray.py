import sys
from typing import Tuple, List


def brute_force_max_sub_array(the_array: List)->Tuple[int, int, int]:

    maximum = -sys.maxsize - 1
    the_result: Tuple[int, int, int] = (0, 0, maximum)
    for i in range(len(the_array)-1):
        total = the_array[i];
        if total > maximum:
            maximum = total
            the_result = (i, i, maximum)
        for j in range(i+1, len(the_array)):
            total = total + the_array[j]
            if total > maximum:
                maximum = total
                the_result = (i, j, maximum)
    return the_result


if __name__ == "__main__":

    result = brute_force_max_sub_array([1, 2, 3])
    print(result)




