import unittest

from year_2015.day_23.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 170)

    def test_part_2(self):
        self.assertEqual(part_2(), 247)


class TestExamples(unittest.TestCase):
    pass


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
