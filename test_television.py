import unittest
from television import *

class MyTestCase(unittest.TestCase):
    def test__init__(self):
        self.assertEqual(True, False)  # add assertion here

    def test_power(self):
        pass

    def test_mute(self):
        pass

    def test_channel_up(self):
        pass

    def test_channel_down(self):
        pass

    def test_volume_up(self):
        pass

    def test_volume_down(self):
        pass

if __name__ == '__main__':
    unittest.main()
