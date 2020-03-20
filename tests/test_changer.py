import unittest
import random


from stchger.changer import SeatChanger


class TestSeatChanger(unittest.TestCase):
    def setUp(self):
        random.seed(0)
        self.seat_places = ((0, 1), (0, 2), (1, 0), (1, 1), (1, 2))
        self.members = [{"num": i} for i in range(1, 6)]

        def initializer(*args, **kwargs):
            return list(self.seat_places)

        def loss1(*args, **kwargs):
            return 1

        def loss2(*args, **kwargs):
            return 2

        self.loss12 = loss1() + loss2()
        self.iter_num = 10
        self.step_range = (2, 3)
        self.changer = SeatChanger(
            losses=[loss1, loss2],
            initializer=initializer,
            iter_num=self.iter_num,
            ch_step_range=self.step_range,
        )

    def test_change_one(self):
        ch_place = self.changer.change_one(self.seat_places)
        self.assertEqual(len(self.seat_places), len(ch_place))
        self.assertEqual(set(self.seat_places), set(ch_place))
        diff_count = 0
        for before, after in zip(self.seat_places, ch_place):
            diff_count += before == after
        self.assertLessEqual(self.step_range[0], diff_count)
        self.assertGreaterEqual(self.step_range[1], diff_count)

    def test_cal_loss(self):
        loss = self.changer.cal_loss(self.seat_places, self.members, self.seat_places)
        self.assertAlmostEqual(loss, self.loss12)

    def test_solve(self):
        mem_places = self.changer.solve(self.seat_places, self.members)
        self.assertEqual(len(self.seat_places), len(mem_places))
        self.assertEqual(set(self.seat_places), set(mem_places))
        self.assertEqual(len(self.changer.loss_log), self.iter_num + 1)
