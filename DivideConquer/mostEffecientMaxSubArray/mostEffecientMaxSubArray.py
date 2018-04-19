from typing import Tuple,List

'''the complexity is o(n)'''


def max_sub_array(the_input: List)-> Tuple[int, int, int]:
    max_so_far: int = the_input[0]
    total: int = the_input[0]
    start_index: int = 0
    end_index: int = 0
    for index in range(1, len(the_input)):
        if total < 0:
            start_index = index
            total = the_input[index]
        else:
            total = total + the_input[index]
            if total > max_so_far:
                max_so_far = total
                end_index = index
    return start_index, end_index, max_so_far


if __name__ == "__main__":
    result = max_sub_array([1, -3, 2, 5, 8, -1, -2])
    print(result)