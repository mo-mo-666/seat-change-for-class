import random
from typing import Iterable, Union, Tuple, List, Sequence
from .initializer import RandomInitializer


class SeatChanger:
    """
    Seat change for classes.
    """

    def __init__(
        self,
        losses: Iterable[object],
        initializer: object = RandomInitializer(),
        iter_num: int = 10000,
        ch_step_range: Tuple[int, int] = (2, 4),
    ):
        """
        Parameters
        ----------
        losses : Iterable[object]
            List of Loss function (instance).

        initializer : object, optional
            Initializer function (instance), by default RandomInitializer().

        iter_num : int, optional
            The number of iteration, by default 10000.

        ch_step_range : Tuple[int, int], optional
            The number of people to interchange in one step, by default (2, 4).
        """
        self.losses = losses
        self.initializer = initializer
        self.iter_num = iter_num
        self.ch_step_range = ch_step_range
        self.loss_log = []

    def change_one(
        self, mem_places: Sequence[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        """
        One step change of the member's place.

        Parameters
        ----------
        mem_places : Sequence[Tuple[int, int]]
            The place of the members.

        Returns
        -------
        List[Tuple[int, int]]
            The new place of the members.
        """
        num = len(mem_places)
        l, h = self.ch_step_range
        ch_num = random.randint(l, h)
        ch_idx = random.sample(range(num), ch_num)
        ch_before = sorted(ch_idx)
        if ch_idx != ch_before:
            ch_idx = ch_idx[::-1]
        idx = list(range(num))
        for i, k in zip(ch_before, ch_idx):
            idx[i] = k
        new_mem_places = [mem_places[i] for i in idx]
        return new_mem_places

    def cal_loss(
        self,
        seat_places: Sequence[Tuple[int, int]],
        members: Sequence[dict],
        mem_places: Sequence[Tuple[int, int]],
    ) -> float:
        """
        Calculate loss using loss instances.

        Parameters
        ----------
        seat_places : Sequence[Tuple[int, int]]
            The places of seats.

        members : Sequence[dict]
            Member list.

        mem_places : Sequence[Tuple[int, int]]
            The place of members.

        Returns
        -------
        float
            Loss.
        """
        loss = 0
        for loss_func in self.losses:
            loss += loss_func(seat_places, members, mem_places)
        return loss

    def solve(
        self, seat_places: Sequence[Tuple[int, int]], members: Sequence[dict]
    ) -> Tuple[Tuple[int, int]]:
        """
        Search the appropriate seat place of each member.

        Parameters
        ----------
        seat_places : Sequence[Tuple[int, int]]
            The place of seats.

        members : Sequence[dict]
            Member list.

        Returns
        -------
        List[Tuple[int, int]]
            The place of members.
        """
        self.loss_log = []
        mem_places = self.initializer(seat_places, members)
        loss = self.cal_loss(seat_places, members, mem_places)
        self.loss_log.append(loss)

        for _ in range(self.iter_num):
            new_mem_places = self.change_one(mem_places)
            new_loss = self.cal_loss(seat_places, members, new_mem_places)
            if loss >= new_loss:
                mem_places = new_mem_places
                loss = new_loss
            self.loss_log.append(loss)
        mem_places = tuple(mem_places)
        return mem_places
