def random_list(size):
    import random
    array = []
    for i in range(size):
        array.append(random.randint(1, size))
    return array


def insertion_sort_partition(array, inc, gap):
    for i in range(gap + inc, len(array), gap):
        start = array[i]
        j = i
        while j > 0 and array[j-gap] > start:
            array[j] = array[j-gap]
            j -= gap
        array[j] = start


if __name__ == "__main__":
    # array = [8, 3, 4, 9, 7, 6, 1, 5, 2]
    array = random_list(40)

    gap = len(array) // 2
    while gap > 0:
        for inc in range(gap):
            result = insertion_sort_partition(array, inc, gap)
        gap = gap // 2

    print(array)