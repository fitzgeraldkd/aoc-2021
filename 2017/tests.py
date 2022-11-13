import unittest

import day_01.tests as day_01
import day_02.tests as day_02
import day_03.solution as day_03
import day_04.solution as day_04
import day_05.solution as day_05
import day_06.solution as day_06
import day_07.tests as day_07
import day_08.tests as day_08
import day_09.tests as day_09
import day_10.tests as day_10
import day_11.tests as day_11
import day_12.tests as day_12
import day_13.tests as day_13
import day_14.tests as day_14
import day_15.tests as day_15

TEST_MODULES = [
    day_01, day_02, day_07, day_08, day_09, day_10, day_11, day_12, day_13, day_14, day_15
]


class Test2017Challenges(unittest.TestCase):

    def test_day_3(self):
        self.assertEqual(day_03.part_1(), 419)
        self.assertEqual(day_03.part_2(), 295229)

    def test_day_4(self):
        self.assertEqual(day_04.part_1(), 466)
        self.assertEqual(day_04.part_2(), 251)

    def test_day_5(self):
        self.assertEqual(day_05.part_1(), 374269)
        self.assertEqual(day_05.part_2(), 27720699)

    def test_day_6(self):
        self.assertEqual(day_06.part_1(), 11137)
        self.assertEqual(day_06.part_2(), 1037)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    for test_module in TEST_MODULES:
        suite.addTests(loader.loadTestsFromTestCase(test_module.TestBase))

    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    unittest.main()
