def random_list(size):
    import random
    array = []
    for i in range(size):
        array.append(random.randint(1, size))
    return array


def partition(array, first_index, last_index):
    pivot_value = array[(first_index + last_index) // 2]  # choose pivot value
    print("{0}: [{1}] ~ {2} ~ [{3}]".format(array, first_index, pivot_value, last_index), end='')
    while first_index <= last_index:
        while array[first_index] < pivot_value: first_index += 1    # move first_index forward
        while array[last_index]  > pivot_value: last_index  -= 1    # move last_index backward
        if first_index <= last_index:
            array[first_index], array[last_index] = array[last_index], array[first_index]   # swap array value
            first_index, last_index = first_index+1, last_index-1                           # make exit criteria

    print(' --> {}'.format(array))
    return first_index


def sort(level, array, first_index, last_index):
    print('LEVEL > {}'.format(level))    ##  이진트리의  Depth, Level 확인을 위해 출력함
    if first_index < last_index:
        middle = partition(array, first_index, last_index)
        sort(level+'L', array, first_index, middle-1)
        sort(level+'R', array, middle, last_index)


if __name__ == "__main__":
    # array = random_list(5)
    array = [3, 2, 5, 1, 4, 6, 9, 8]
    # print(array)
    sort('', array, 0, len(array)-1)
    # print(array)


