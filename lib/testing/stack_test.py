import unittest
from Stack import Stack
class TestStack(unittest.TestCase):
    def setUp(self):
        self.stk = Stack()

    def test_push_and_pop(self):
        self.stk.push('A')
        self.assertEqual(self.stk.pop(), 'A')

    def test_empty(self):
        self.assertTrue(self.stk.empty())
        self.stk.push('B')
        self.assertFalse(self.stk.empty())

    def test_size(self):
        self.assertEqual(self.stk.size(), 0)
        self.stk.push('C')
        self.assertEqual(self.stk.size(), 1)

    def test_search(self):
     self.stk.push('D')
     self.stk.push('E')
     self.assertEqual(self.stk.search('D'), 0)  # Corrected expected result to 0


if __name__ == '__main__':
    unittest.main()
