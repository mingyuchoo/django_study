def random_list(size):
    import random
    array = []
    for i in range(size):
        array.append(random.randint(1, size))
    return array


def merge_sort(array):
    """
    1. divide
    2. conquer
    """
    if len(array) < 2:  # exit criteria
        return array

    # divide section
    middle_index = len(array) // 2
    left_array = array[:middle_index]
    right_array = array[middle_index:]
    merge_sort(left_array)
    merge_sort(right_array)

    # conquer section
    main_index = 0
    left_index = 0
    right_index = 0

    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] < right_array[right_index]:
            array[main_index] = left_array[left_index]
            left_index += 1
        else:
            array[main_index] = right_array[right_index]
            right_index += 1
        main_index += 1
    if left_index != len(left_array):
        array[main_index:] = left_array[left_index:]
    else:
        array[main_index:] = right_array[right_index:]


if __name__ == "__main__":
    array = [8, 3, 1, 9, 7, 6, 4, 5, 2]
    # array = random_list(40)
    print(array)
    merge_sort(array)
    print(array)