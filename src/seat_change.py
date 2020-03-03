import random
from typing import List, Iterable, Union, Tuple


class SeatChange:

    def __init__(self, seat_places: List[Tuple[int, int]], loss: object, initializer: object, iter_num: int = 10000, ch_step_range: Tuple[int, int] =(2, 5)):
        self.seat_places = seat_places
        self.loss = loss
        self.initializer = initializer
        self.iter_num = iter_num
        self.ch_step_range = ch_step_range
        self.loss_log = []

    def transform(self, members: List[dict]):
        num = len(members)
        self.loss_log = []
        places = self.initializer.transform(members)
        loss = self.loss(members, places)
        l, h = self.ch_step_range
        self.loss_log.append(loss)
        for _ in range(iter_num):
            ch_num = random.choice(range(l, h+1))
            ch_idx = random.sample(range(num), ch_num)
