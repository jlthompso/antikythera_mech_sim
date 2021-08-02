import unittest
import gears


class MyTestCase(unittest.TestCase):
    def test_create_gear(self):
        gear = gears.Gear(10, "p1")
        self.assertEqual(gear.get_id(), "p1")
        self.assertEqual(gear.get_num_teeth(), 10)
        self.assertEqual(gear.get_angle(), 0)


if __name__ == '__main__':
    unittest.main()
