import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from day_19.solution import get_available_robots, get_blueprint, part_1, part_2


class TestBase(unittest.TestCase):

    @unittest.skip
    def test_part_1(self):
        self.assertEqual(part_1(), None)

    @unittest.skip
    def test_part_2(self):
        self.assertEqual(part_2(), None)


class TestExamples(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 33)

    def test_part_2(self):
        self.assertEqual(part_2(), None)


class TestUtils(unittest.TestCase):

    def test_get_blueprint(self):
        self.assertDictEqual(get_blueprint(1, 2, 3, 4, 5, 6, 7), {
            'id': 1,
        'ore': {
            'ore': 2
        },
        'clay': {
            'ore': 3
        },
        'obsidian': {
            'ore': 4,
            'clay': 5
        },
        'geode': {
            'ore': 6,
            'obsidian': 7
        }
        })

    def test_get_available_robots(self):
        blueprint_a = get_blueprint(1, 2, 3, 4, 5, 6, 7)

        self.assertCountEqual(get_available_robots(blueprint_a, {'ore': 0, 'clay': 0, 'obsidian': 0, 'geode': 0}),
                              [])
        self.assertCountEqual(get_available_robots(blueprint_a, {'ore': 2, 'clay': 0, 'obsidian': 0, 'geode': 0}),
                              ['ore'])
        self.assertCountEqual(get_available_robots(blueprint_a, {'ore': 3, 'clay': 0, 'obsidian': 0, 'geode': 0}),
                              ['ore', 'clay'])
        self.assertCountEqual(get_available_robots(blueprint_a, {'ore': 3, 'clay': 5, 'obsidian': 0, 'geode': 0}),
                              ['ore', 'clay'])
        self.assertCountEqual(get_available_robots(blueprint_a, {'ore': 4, 'clay': 5, 'obsidian': 0, 'geode': 0}),
                              ['ore', 'clay', 'obsidian'])
        self.assertCountEqual(get_available_robots(blueprint_a, {'ore': 6, 'clay': 5, 'obsidian': 0, 'geode': 0}),
                              ['ore', 'clay', 'obsidian'])
        self.assertCountEqual(get_available_robots(blueprint_a, {'ore': 6, 'clay': 5, 'obsidian': 7, 'geode': 0}),
                              ['ore', 'clay', 'obsidian', 'geode'])
        self.assertCountEqual(get_available_robots(blueprint_a, {'ore': 6, 'clay': 0, 'obsidian': 7, 'geode': 0}),
                              ['ore', 'clay', 'geode'])


if __name__ == '__main__':
    unittest.main()
