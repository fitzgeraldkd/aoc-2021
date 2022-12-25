import unittest
from unittest.mock import patch

from utils.setup import read_inputs
from year_2015.day_13.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 709)

    def test_part_2(self):
        self.assertEqual(part_2(), 668)


class TestExamples(unittest.TestCase):

    def test_part_1(self):
        with patch('year_2015.day_13.solution.read_inputs', return_value=read_inputs(__file__, 'sample.txt')):
            self.assertEqual(part_1(), 330)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
