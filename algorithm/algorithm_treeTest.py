from unittest import TestCase, main

from exam11_tree import BinarySearchTree

class BinarySearchTreeTest(TestCase):

  def setUp(self):
    self.array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]
    self.bst = BinarySearchTree()

  def tearDown(self):
    del self.bst
    del self.array

  def test_insert(self):
    self.assertTrue(self.bst.insert(1))

  def test_find(self):
    for i in self.array:
      self.bst.insert(i)
    self.assertEqual(self.bst.find(15), True)
    self.assertEqual(self.bst.find(1), False)

  def test_delete(self):
    for i in self.array:
      self.bst.insert(i)
    self.assertEqual(self.bst.delete(55), True)
    self.assertEqual(self.bst.delete(2), False)

if __name__ == "__main__":
  main()
