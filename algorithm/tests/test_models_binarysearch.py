from django.test import TestCase
from algorithm.models import BinarySearchTree


class BinarySearchTestCase(TestCase):

    def setUp(self) -> None:
        self.bst = BinarySearchTree()
        self.array = [21, 14, 28,11, 18, 25, 32, 5, 12, 15, 19, 23, 27, 30, 37]
    def tearDown(self) -> None:
        pass

    def test_insert(self):
        for i in self.array:
            self.bst.insert(i)
        self.assertIsNotNone(self.bst)

    def test_find(self):
        self.test_insert()
        print('test_find > 15 = ', self.bst.find(15))
        print('test_find > 17 = ', self.bst.find(17))

    def test_delete(self):
        self.test_insert()
        print('test_delete > 14 = ', self.bst.delete(14))

    def test_pre_order_traversal(self):
        self.test_insert()
        self.bst.pre_order_traversal()

    def test_in_order_traversal(self):
        self.test_insert()
        self.bst.in_order_traversal()

    def test_post_order_traversal(self):
        self.test_insert()
        self.bst.in_order_traversal()

    def test_level_order_traversal(self):
        self.test_insert()
        self.bst.level_order_traversal()