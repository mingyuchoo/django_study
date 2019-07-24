def random_list(size):
    import random
    array = []
    for i in range(size):
        array.append(random.randint(1, size))
    return array


def binary_search_loop(array, value):
    """
    1. 중간의 인덱스를 찾는다.
    2. 찾고자하는 값이 중간 인덱스의 값보다 작으면 끝 인덱스를 중간인덱스로 좁힌다.
    3. 찾고자하는 값이 중간 인덱스의 값과 같으면 찾은 위치의 인덱스를 반환하고 끝낸다.
    4. 찾고자하는 값이 중간 인덱스의 갑보다 크면 시작 인덱스를 중간인덱스로 좁힌다.
    """
    start_index = 0
    end_index = len(array) - 1
    while start_index <= end_index:
        middle_index = ((end_index - start_index) // 2) + start_index
        if value < array[middle_index]:
            end_index = middle_index - 1
        elif value == array[middle_index]:
            return middle_index
        elif value > array[middle_index]:
            start_index = middle_index + 1
    return -1


def binary_search_recursion_1(array, start_index, end_index, value):
    if start_index <= end_index:
        middle_index = ((end_index - start_index) // 2) + start_index
        if value < array[middle_index]:
            return binary_search_recursion_1(array, start_index, middle_index - 1, value)
        elif value == array[middle_index]:
            return middle_index
        elif value > array[middle_index]:
            return binary_search_recursion_1(array, middle_index + 1, end_index, value)
    else:
        return -1


def binary_search_recursion_2(array, start_index, end_index, value):
    if start_index > end_index:
        return -1

    middle_index = ((end_index - start_index) // 2) + start_index
    if value < array[middle_index]:
        return binary_search_recursion_2(array, start_index, middle_index - 1, value)
    elif value == array[middle_index]:
        return middle_index
    elif value > array[middle_index]:
        return binary_search_recursion_2(array, middle_index + 1, end_index, value)


if __name__ == "__main__":
    array = sorted(random_list(10))
    # array = [2, 2, 2, 3, 4, 5, 6, 6, 6, 8]
    print(array)
    index_loop = binary_search_loop(array, 3)
    index_recur_1 = binary_search_recursion_1(array, 0, len(array)-1, 3)
    index_recur_2 = binary_search_recursion_1(array, 0, len(array) - 1, 3)
    # print(index_recur)
    print(index_loop, index_recur_1, index_recur_2)
