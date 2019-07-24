def random_list(size):
    import random
    array = []
    for i in range(size):
        array.append(random.randint(1, size))
    return array


if __name__ == "__main__":
    # array = [8, 3, 4, 9, 7, 6, 4, 5, 2]
    array = random_list(40)

    for i in range(1, len(array)):
        start = array[i]
        j = i
        while j > 0 and array[j-1] > start:
            array[j] = array[j-1]
            j -= 1
        array[j] = start

    print(array)
