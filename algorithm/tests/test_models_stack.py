from django.test import TestCase


class StackTestCase(TestCase):
    stack = []

    def setUp(self) -> None:
        self.stack = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J']

    def tearDown(self) -> None:
        del self.stack

    def test_push_X(self):
        self.stack.append('X')
        self.assertTrue(self.stack.count('X'))

    def test_pop(self):
        item = self.stack.pop()
        self.assertEqual(item, 'J')


class StackCalcTestCase(TestCase):
    expression = []
    stack = []

    def setUp(self) -> None:
        self.expression = list('2*3+4')
        for i in self.expression:
            self.stack.append(i)

    def tearDown(self) -> None:
        pass

    def test_first(self):
       for i in range(len(self.stack)):
           print('>> {}'.format(self.stack[i]))
