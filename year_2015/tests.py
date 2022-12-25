import unittest

import year_2015.day_01.tests as day_01
import year_2015.day_02.tests as day_02
import year_2015.day_03.tests as day_03
import year_2015.day_04.tests as day_04
import year_2015.day_05.tests as day_05
import year_2015.day_06.solution as day_06
import year_2015.day_07.solution as day_07
import year_2015.day_08.solution as day_08
import year_2015.day_09.solution as day_09
import year_2015.day_10.solution as day_10
import year_2015.day_11.solution as day_11
import year_2015.day_12.solution as day_12
import year_2015.day_13.solution as day_13
import year_2015.day_14.solution as day_14
import year_2015.day_15.solution as day_15
import year_2015.day_16.solution as day_16
import year_2015.day_17.solution as day_17
import year_2015.day_18.solution as day_18
import year_2015.day_19.solution as day_19
import year_2015.day_20.solution as day_20
import year_2015.day_21.solution as day_21
import year_2015.day_22.solution as day_22
import year_2015.day_23.solution as day_23
import year_2015.day_24.solution as day_24
import year_2015.day_25.solution as day_25

TEST_MODULES = [day_01, day_02, day_03, day_04, day_05]


class Test2015Challenges(unittest.TestCase):

    def test_day_14(self):
        self.assertEqual(day_14.part_1(), 2640)
        self.assertEqual(day_14.part_2(), 1102)

    def test_day_15(self):
        self.assertEqual(day_15.part_1(), 13882464)
        self.assertEqual(day_15.part_2(), 11171160)

    def test_day_16(self):
        self.assertEqual(day_16.part_1(), 103)
        self.assertEqual(day_16.part_2(), 405)

    def test_day_17(self):
        self.assertEqual(day_17.part_1(), 4372)
        self.assertEqual(day_17.part_2(), 4)

    def test_day_18(self):
        self.assertEqual(day_18.part_1(), 814)
        self.assertEqual(day_18.part_2(), 924)

    def test_day_19(self):
        self.assertEqual(day_19.part_1(), 576)
        self.assertEqual(day_19.part_2(), 207)

    def test_day_20(self):
        self.assertEqual(day_20.part_1(), 776160)
        self.assertEqual(day_20.part_2(), 786240)

    def test_day_21(self):
        self.assertEqual(day_21.part_1(), 111)
        self.assertEqual(day_21.part_2(), 188)

    def test_day_22(self):
        self.assertEqual(day_22.part_1(), 900)
        self.assertEqual(day_22.part_2(), 1216)

    def test_day_23(self):
        self.assertEqual(day_23.part_1(), 170)
        self.assertEqual(day_23.part_2(), 247)

    def test_day_24(self):
        self.assertEqual(day_24.part_1(), 10439961859)
        self.assertEqual(day_24.part_2(), 72050269)

    def test_day_25(self):
        self.assertEqual(day_25.part_1(), 2650453)


if __name__ == '__main__':

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    for test_module in TEST_MODULES:
        suite.addTests(loader.loadTestsFromTestCase(test_module.TestBase))

    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    unittest.main()
