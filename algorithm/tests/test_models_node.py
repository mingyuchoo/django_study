from django.test import TestCase
from algorithm.models import SingleLinkedNode, DoubleLinkedNode


class SingleLinkedNodeTestCase(TestCase):
    a = None

    def setUp(self) -> None:
        self.a = SingleLinkedNode('A')
        b = SingleLinkedNode('B')
        c = SingleLinkedNode('C')
        d = SingleLinkedNode('D')
        e = SingleLinkedNode('E')
        f = SingleLinkedNode('F')
        g = SingleLinkedNode('G')
        h = SingleLinkedNode('H')
        i = SingleLinkedNode('I')
        j = SingleLinkedNode('J')

        self.a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f
        f.next = g
        g.next = h
        h.next = i
        i.next = j

    def tearDown(self) -> None:
        del self.a

    def test_traversal_list(self):
        # print('>>> START test_traversal_list')
        node = self.a
        self.assertEqual(node.data, 'A')
        while node:
            # print(node.data)
            node = node.next
        self.assertEqual(node, None)

    def test_insert_node_X_after_g(self):
        """
        [제약]
        삽입할 노드는 넣을 위치를 찾은 뒤 리스트에 연결해야 한다.
        따라오는 노드의 위치만 기억하기 때문에 앞의 노드와
        뒤의 노드의 정보를 같이 기억해야 한다.
        """
        # print('>>> START test_insert_node_after_g')

        new_node = SingleLinkedNode('X')
        self.assertEqual(new_node.data, 'X')

        before_node = self.a
        after_node = self.a

        while after_node:
            # print('>>>> {}'.format(after_node.data))
            if after_node.data == 'G':
                new_node.next = after_node
                before_node.next = new_node
                break
            before_node = after_node
            after_node = after_node.next

        self.test_traversal_list()

    def test_delete_node_X(self):
        self.test_insert_node_X_after_g()

        remove_data = 'X'

        before_node = self.a
        after_node = self.a

        while after_node:
            # print('>>>> {}'.format(after_node.data))
            if after_node.data == remove_data:
                before_node.next = after_node.next
                del after_node
                del remove_data
                break
            before_node = after_node
            after_node = after_node.next
        self.test_traversal_list()



class DoubleLinkedNodeTestCase(TestCase):
    a = None

    def setUp(self):
        self.a = DoubleLinkedNode('A')
        b = DoubleLinkedNode('B')
        c = DoubleLinkedNode('C')
        d = DoubleLinkedNode('D')
        e = DoubleLinkedNode('E')
        f = DoubleLinkedNode('F')
        g = DoubleLinkedNode('G')
        h = DoubleLinkedNode('H')
        i = DoubleLinkedNode('I')
        j = DoubleLinkedNode('J')

        self.a.next = b

        b.prev = self.a
        b.next = c

        c.prev = b
        c.next = d

        d.prev = c
        d.next = e

        e.prev = d
        e.next = f

        f.prev = e
        f.next = g

        g.prev = f
        g.next = h

        h.prev = g
        h.next = i

        i.prev = h
        i.next = j

        j.prev = i
        j.next = None

    def tearDown(self):
        del self.a

    def test_traversal_list(self):
        # print('>>> START test_traversal_list')
        node = self.a
        self.assertEqual(node.data, 'A')
        while node:
            # print('test_traversal_list> {}'.format(node.data))
            node = node.next
        self.assertEqual(node, None)

    def test_traversal_reverse(self):
        node = self.a
        self.assertEqual(node.data, 'A')
        while node.data != 'J':
            node = node.next

        self.assertEqual(node.data, 'J')
        self.assertEqual(node.prev.data, 'I')

        while node:
            # print('test_traversal_reverse> {}'.format(node.data))
            self.assertIsNotNone(node)
            node = node.prev
        self.assertIsNone(node)

    def test_insert_node_X_after_g(self):
        new_node = DoubleLinkedNode('X')
        self.assertEqual(new_node.data, 'X')

        temp_node = self.a
        pointer_node = self.a
        self.assertEqual(pointer_node.data, 'A')

        while pointer_node and pointer_node.data <= new_node.data:
            temp_node = pointer_node
            pointer_node = pointer_node.next

        self.assertEqual(temp_node.prev.data, 'I')
        self.assertEqual(temp_node.data, 'J')
        self.assertIsNone(pointer_node)

        temp_node.next = new_node
        new_node.prev = temp_node

        node = self.a
        while node:
            # print('test_insert_node_X_after_g > {}'.format(node.data))
            self.assertIsNotNone(node)
            node = node.next
        self.assertIsNone(node)

    def test_delete_node_D(self):
        node = self.a
        while node.data != 'D':
            node = node.next
        self.assertEqual(node.data, 'D')
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

        node = self.a
        while node:
            # print('test_delete_node_D > {}'.format(node.data))
            node = node.next

    def test_delete_node_A(self):
        node = self.a

        node = self.a.next
        while node:
            # print('test_delete_node_A > {}'.format(node.data))
            node = node.next
        del node

    def test_delete_node_J(self):
        node = self.a
        while node.data != 'J':
            print('test_delete_node_J > {}'.format(node.data))
            node = node.next
        self.assertEqual(node.data, 'J')
        self.assertEqual(node.prev.data, 'I')
        del node
