import copy
from abc import ABC, abstractmethod
from typing import Sequence, Tuple, List


class AbstractLoss(ABC):
    """
    Abstract class for loss class.
    You must inherit this class if you want to make new loss classes.
    """

    class_type = "Loss"

    def __init__(self):
        pass

    @abstractmethod
    def __call__(
        self,
        seat_places: Sequence[Tuple[int, int]],
        members: Sequence[dict],
        mem_places: List[Tuple[int, int]],
    ) -> float:
        """
        Calculate loss.

        Parameters
        ----------
        seat_places : Sequence[Tuple[int, int]]
            All seat places.
        members : Sequence[dict]
            Members, i.e., students.
        mem_places : List[Tuple[int, int]]
            Members' seat places.

        Returns
        -------
        float
            The loss value.
        """
        raise NotImplementedError("This method must be override and return float.")


class HopeLoss(AbstractLoss):
    """
    Hope loss.

    Note
    ----------
    Member directories must have 'hopes' key.
    member['hopes'] == Sequence[Tuple[int, int]].
    """

    def __init__(self, metric: str = "euclid", power: int = 2):
        super().__init__()
        metrics = ["manhattan", "euclid"]
        if metric not in metrics:
            raise ValueError(f"The argument 'metric' must be selected in {metrics}.")

        self.metric = metric
        self.power = power
        if self.metric == "manhattan":
            self._cal_one = self._manhattan_cal_one
        elif self.metric == "euclid":
            self._cal_one = self._euclid_cal_one

    def _manhattan_cal_one(
        self, hopes: Sequence[Tuple[int, int]], mem_place: Tuple[int, int]
    ) -> float:
        if not hopes:
            return 0.0
        loss = min(
            [
                abs(hope[0] - mem_place[0]) + abs(hope[1] - mem_place[1])
                for hope in hopes
            ]
        )
        return loss

    def _euclid_cal_one(
        self, hopes: Sequence[Tuple[int, int]], mem_place: Tuple[int, int]
    ) -> float:
        if not hopes:
            return 0.0
        loss = min(
            [
                ((hope[0] - mem_place[0]) ** 2 + (hope[1] - mem_place[1]) ** 2)
                ** (1 / 2)
                for hope in hopes
            ]
        )
        return loss

    def __call__(
        self,
        seat_places: Sequence[Tuple[int, int]],
        members: Sequence[dict],
        mem_places: List[Tuple[int, int]],
    ) -> float:
        loss = 0
        for mem, place in zip(members, mem_places):
            hopes = mem.get("hopes", -1)
            if hopes == -1:
                raise KeyError("Some member does not have 'hopes' key.")
            else:
                loss += self._cal_one(hopes, place) ** self.power
        return loss


class WeightedHopeLoss(HopeLoss):
    def __call__(
        self,
        seat_places: Sequence[Tuple[int, int]],
        members: Sequence[dict],
        mem_places: List[Tuple[int, int]],
    ) -> float:
        loss = 0
        for mem, place in zip(members, mem_places):
            hopes = mem.get("hopes", -1)
            if hopes == -1:
                raise KeyError("Some member does not have 'hopes' key.")
            weight = mem.get("hope_weight", 1)
            loss += (self._cal_one(hopes, place) ** self.power) * weight
        return loss


class GlassesLoss(AbstractLoss):
    """
    Glasses loss.

    Note
    ----------
    Member directories must have 'glasses' key.
    member['glasses'] == Sequence[Tuple[int, int]].
    """

    def __init__(self, weight: float = 10000):
        super().__init__()
        self.weight = weight

    def _cal_one(
        self, glasses: Sequence[Tuple[int, int]], mem_place: Tuple[int, int]
    ) -> float:
        if not glasses:
            return 0
        return (mem_place not in glasses) * self.weight

    def __call__(
        self,
        seat_places: Sequence[Tuple[int, int]],
        members: Sequence[dict],
        mem_places: List[Tuple[int, int]],
    ) -> float:
        loss = 0
        for mem, place in zip(members, mem_places):
            glasses = mem.get("glasses", -1)
            if glasses == -1:
                raise KeyError("Some member does not have 'glasses' key.")
            else:
                loss += self._cal_one(glasses, place)
        return loss
