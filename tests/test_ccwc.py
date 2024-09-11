import unittest
from ccwc.ccwc import count_chars, count_lines, count_words

class TestCcwc(unittest.TestCase):
    def test_count_chars(self):
        self.assertEqual(count_chars('data/test.txt'), 1000)

    def test_count_lines(self):
        self.assertEqual(count_lines('data/test.txt'), 50)

if __name__ == '__main__':
    unittest.main()
