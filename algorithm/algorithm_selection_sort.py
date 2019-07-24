def random_list(size):
    import random
    array = []
    for i in range(size):
        array.append(random.randint(1, size))
    return array


if __name__ == "__main__":
    # array = [8, 3, 4, 9, 7, 6, 4, 5, 2]
    array = random_list(40)

    for i in range(0, len(array)-1):
        j = i + 1
        while j < len(array):
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
            j += 1
    print(array)

