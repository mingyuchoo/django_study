class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data) -> bool:
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, current_node, data) -> Node:
        if current_node is None:
            current_node = Node(data)
        else:
            if current_node.data >= data:
                current_node.left = self._insert_value(current_node.left, data)
            else:
                current_node.right = self._insert_value(current_node.right, data)
        return current_node

    def find(self, key) -> bool:
        return self._find_value(self.root, key)

    def _find_value(self, current_node, key) -> bool:
        if current_node is None or current_node.data == key:
            return current_node is not None
        elif key < current_node.data:
            return self._find_value(current_node.left, key)
        else:
            return self._find_value(current_node.right, key)

    def delete(self, key) -> bool:
        self.root, is_deleted = self._delete_value(self.root, key)
        return is_deleted

    def _delete_value(self, current_node, key) -> bool:
        """
        1) 삭제할 node의 Right Tree를 기준으로 잡는다.
        2) Right Tree의 가장 왼쪽에 있는 node를 찾는다.
        3) 삭제할 node의 Left Tree를 2)에서 찾은 node의 Left Tree로 붙인다.
        4) 2)에서 찾은 node의 Right Tree를 2)에서 찾는 node의 부모 node의 Left Tree로 붙인다.
        5) 삭제할 node의 Right Tree를 2)에서 찾은 node의 Right Tree로 붙인다.
        6) 삭제할 node를 2)에서 찾는 node로 대체한다.
        """
        if current_node is None:
            return current_node, False

        is_deleted = False
        if key == current_node.data:
            is_deleted = True
            if current_node.left and current_node.right:
                # replace the current_node to the leftmost of current_node.right
                parent, child = current_node, current_node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = current_node.left
                if parent != current_node:
                    parent.left = child.right
                    child.right = current_node.right
                current_node = child
            elif current_node.left or current_node.right:
                current_node = current_node.left or current_node.right
            else:
                current_node = None
        elif key < current_node.data:
            current_node.left, is_deleted = self._delete_value(current_node.left, key)
        else:
            current_node.right, is_deleted = self._delete_value(current_node.right, key)
        return current_node, is_deleted

if __name__ == "__main__":
    array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]

    bst = BinarySearchTree()
    for i in array:
        bst.insert(i)

    # Find
    print(bst.find(15))
    print(bst.find(17))

    # Delete
    print(bst.delete(55))
    print(bst.delete(14))
    print(bst.delete(11))
