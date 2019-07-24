def random_list(size):
    import random
    array = []
    for i in range(size):
        array.append(random.randint(1, size))
    return array


if __name__ == "__main__":
    # array = [8, 3, 4, 9, 7, 6, 1, 5, 2]
    array = random_list(40)

    for i in range(1, len(array)):
        for j in range(0, len(array) - i):
            if array[j] > array[j+1]:
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp
    
    print(array)

