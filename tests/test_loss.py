import unittest

from stchger.loss import HopeLoss, WeightedHopeLoss, GlassesLoss


class TestHopeLoss(unittest.TestCase):
    def setUp(self):
        self.seat_places = ((0, 1), (0, 2), (1, 0), (1, 1), (1, 2))
        self.members = (
            {"num": 1, "hopes": [(0, 1)]},
            {"num": 2, "hopes": [(1, 0)]},
            {"num": 3, "hopes": [(0, 2), (1, 2)]},
            {"num": 4, "hopes": [(0, 1), (0, 2), (1, 2)]},
            {"num": 5, "hopes": list(self.seat_places)},
        )
        self.mem_places = list(self.seat_places)

    def test_call_(self):
        euclid_loss_f = HopeLoss(metric="euclid", power=2)
        euclid_ans = 0 + 5 + 4 + 1 + 0
        euclid_loss = euclid_loss_f(self.seat_places, self.members, self.mem_places)
        self.assertAlmostEqual(euclid_loss, euclid_ans)
        man_loss_f = HopeLoss(metric="manhattan", power=2)
        man_ans = 0 + 9 + 4 + 1 + 0
        man_loss = man_loss_f(self.seat_places, self.members, self.mem_places)
        self.assertAlmostEqual(man_loss, man_ans)

class TestWeightedHopeLoss(unittest.TestCase):
    def setUp(self):
        self.seat_places = ((0, 1), (0, 2), (1, 0), (1, 1), (1, 2))
        self.members = (
            {"num": 1, "hopes": [(0, 1)], "hope_weight": 3.0},
            {"num": 2, "hopes": [(1, 0)], "hope_weight": 2.0},
            {"num": 3, "hopes": [(0, 2), (1, 2)], "hope_weight": 1.0},
            {"num": 4, "hopes": [(0, 1), (0, 2), (1, 2)], "hope_weight": 0.5},
            {"num": 5, "hopes": list(self.seat_places), "hope_weight": 0.2},
        )
        self.mem_places = list(self.seat_places)

    def test_call_(self):
        euclid_loss_f = WeightedHopeLoss(metric="euclid", power=2)
        euclid_ans = 0 * 3.0 + 5 * 2.0 + 4 * 1.0 + 1 * 0.5 + 0 * 0.2
        euclid_loss = euclid_loss_f(
            self.seat_places, self.members, self.mem_places)
        self.assertAlmostEqual(euclid_loss, euclid_ans)
        man_loss_f = WeightedHopeLoss(metric="manhattan", power=2)
        man_ans = 0 * 3.0 + 9 * 2.0 + 4 * 1.0 + 1 * 0.5 + 0 * 0.2
        man_loss = man_loss_f(self.seat_places, self.members, self.mem_places)
        self.assertAlmostEqual(man_loss, man_ans)


class TestGlassesLoss(unittest.TestCase):
    def setUp(self):
        self.seat_places = ((0, 1), (0, 2), (1, 0), (1, 1), (1, 2))
        self.members = (
            {"num": 1, "glasses": []},
            {"num": 2, "glasses": []},
            {"num": 3, "glasses": [(0, 1), (1, 0)]},
            {"num": 4, "glasses": [(0, 1), (1, 0)]},
            {"num": 5, "glasses": [(1, 2)]},
        )
        self.mem_places = list(self.seat_places)

    def test_call_(self):
        weight = 10000
        f = GlassesLoss(weight=weight)
        ans = (0 + 0 + 0 + 1 + 0) * weight
        loss = f(self.seat_places, self.members, self.mem_places)
        self.assertAlmostEqual(loss, ans)
