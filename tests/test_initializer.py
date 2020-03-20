import unittest
import random

from stchger.initializer import RandomInitializer


class TestRandomInitializer(unittest.TestCase):
    def setUp(self):
        random.seed(0)
        self.seat_places = ((0, 1), (0, 2), (1, 0), (1, 1), (1, 2))
        self.members = [{"num": i} for i in range(1, 6)]
        self.random_initializer = RandomInitializer()

    def test_call(self):
        mem_places = self.random_initializer(self.seat_places, self.members)
        self.assertEqual(len(mem_places), len(self.seat_places))
        self.assertEqual(set(mem_places), set(self.seat_places))
