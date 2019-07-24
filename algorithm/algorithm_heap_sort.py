def left_node(index):
    return ((index+1) << 1) - 1


def right_node(index):
    return (index+1) << 1


def up_heap(array, index, heap_size):

    left_node_index = left_node(index)
    right_node_index = right_node(index)

    if left_node_index <= heap_size and array[left_node_index] > array[index]:
        largest_index = left_node_index
    else:
        largest_index = index

    if right_node_index <= heap_size and array[right_node_index] > array[largest_index]:
        largest_index = right_node_index
    if largest_index != index:
        array[index], array[largest_index] = array[largest_index], array[index]
        up_heap(array, largest_index, heap_size)


def build_heap(array):
    heap_size = len(array) - 1
    for i in reversed(range(len(array) // 2)):
        up_heap(array, i, heap_size)


def heap_sort(heap):
    tmp_array = list()
    for i in range(len(heap)):
        tmp_array.append(heap.pop(0))
        up_heap(heap, 0, len(heap)-1)
    return tmp_array


if __name__ == "__main__":
    import random
    array = [random.randint(1, 10) for i in range(int(10))]
    print(array)
    build_heap(array)
    sorted_array = heap_sort(array)
    print(sorted_array)