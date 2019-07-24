from django.db import models


class Node(models.Model):
    def __init__(self, data):
        super(Node, self).__init__()
        self.data = data


class SingleLinkedNode(Node):
    def __init__(self, data, next=None):
        super(SingleLinkedNode, self).__init__(data)
        self.next = next


class DoubleLinkedNode(SingleLinkedNode):
    def __init__(self, data, next=None, prev=None):
        super(DoubleLinkedNode, self).__init__(data, next)
        self.prev = prev


class TreeNode(Node):
    def __init__(self, data):
        super(TreeNode, self).__init__(data)
        self.left = self.right = None 


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        """
        return value: True or False
        """
        self.root = self._insert_data(self.root, data)
        return self.root is not None

    def _insert_data(self, node, data):
        if node is None:
            node = TreeNode(data)
        else:
            if data < node.data:
                node.left = self._insert_data(node.left, data)
            else:
                node.right = self._insert_data(node.right, data)
        return node

    def delete(self, data):
        """
        return value: True or False
        """
        self.root, deleted = self._delete_data(self.root, data)
        return deleted

    def _delete_data(self, node, data):
        deleted = False
        if node is None:
            return node, deleted
        else:
            if data == node.data:
                deleted = True
                if node.left and node.right:
                    parent, child = node, node.right
                    while child.left is not None:
                        parent, child = child, child.left
                    child.left = node.left
                    if parent != node:
                        parent.left = child.right
                        child.right = node.right
                    node = child
                elif node.right or node.right:
                    node = node.left or node.right
                else:
                    node = None
            elif data < node.data:
                node.left, deleted = self._delete_data(node.left, data)
            else:
                node.right, deleted = self._delete_data(node.right, data)
            return node, deleted

    def find(self, data):
        """
        return value: True or False
        """
        return self._find_data(self.root, data)


    def _find_data(self, node, data):
        if node is None or node.data == data:
            return node is not None
        elif data < node.data:
            return self._find_data(node.left, data)
        else:
            return self._find_data(node.right, data)

    def pre_order_traversal(self):
        """
        Call stack을 이용하여 구현
        전위 표기법을 이용한 계산식에 이용함
        :return: Boolean
        """
        self._pre_order_traversal(self.root)

    def _pre_order_traversal(self, node):
        if node is None:
            pass
        else:
            print('pre_order_traversal > ', node.data)
            self._pre_order_traversal(node.left)
            self._pre_order_traversal(node.right)
    
    def in_order_traversal(self):
        """
        Call stack을 이용하여 구현
        :return: Boolean
        """
        self._in_order_traversal(self.root)

    def _in_order_traversal(self, node):
        if node is None:
            pass
        else:
            self._in_order_traversal(node.left)
            print('in_order_traversal > ', node.data)
            self._in_order_traversal(node.right)
    
    def post_order_traversal(self):
        """
        Call stack을 이용하여 구현
        :return: Boolean
        """
        self._post_order_traversal(self.root)

    def _post_order_traversal(self, node):
        if node is None:
            pass
        else:
            self._post_order_traversal(node.left)
            self._post_order_traversal(node.right)
            print('post_order_traversal > ', node.data)

    
    def level_order_traversal(self):
        """
        Queue를 이용하여 구현
        :return:  n/a
        """
        self._level_order_traversal(self.root)

    def _level_order_traversal(self, node):
        queue = [node]
        while queue:
            node = queue.pop(0)
            if node is not None:
                print('level_order_traversal > ', node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)


class GraphNode(Node):
    def __init__(self, data):
        super(GraphNode, self).__init__(data)
        self.children = []
        self.visited = False # only use in dfs_recursive


class Graph(object):
    """
    https://m.blog.naver.com/occidere/220923695595
    http://ejklike.github.io/2018/01/05/bfs-and-dfs.html
    """
    def __init__(self):
        super(Graph, self).__init__()

    def breadth_first_search(self, node):
        """
        - Queue
        """
        queue = [node]
        visited = set()

        while queue:
            node = queue.pop(0)
            if node in visited:
                continue
            print(node.data) # visit(node)
            queue.extend(node.children)

    def depth_first_search_recursive(self, node):
        """
        - Stack
        """
        if node.visited == True:
            return

        print(node.data)
        node.visited = True
        for child in node.children:
            self.depth_first_search_iterative(child)

    def depth_first_search_iterative(self, node):
        """
        - Stack
        """
        stack = []
        visited = set()
        stack.append(node)

        while stack:
            node = stack.pop()
            if node in visited:
                continue
            print(node.data)
            stack.extend(node.children)

    def dijkstra(self, node):
        """
        - BFS + PriorityQueue
        """
        pass

    def floyd_washall(self, node):
        """
        - 3 For Loop
        """
        pass