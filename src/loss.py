import copy
from abc import ABC, abstractmethod
from typing import Sequence, Tuple, List


class AbstractLoss(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def calculate(
        self,
        seat_places: Sequence[Tuple[int, int]],
        members: Sequence[dict],
        mem_places: List[Tuple[int, int]],
    ) -> float:
        pass


class HopeLoss(AbstractLoss):
    def __init__(self, metric="euclid", power=2):
        super().__init__()

    def calculate(
        self,
        seat_places: Sequence[Tuple[int, int]],
        members: Sequence[dict],
        mem_places: List[Tuple[int, int]],
    )-> float:
        pass


class GrassLoss(AbstractLoss):
    def __init__(self):
        super().__init__()

    def calculate(
        self,
        seat_places: Sequence[Tuple[int, int]],
        members: Sequence[dict],
        mem_places: List[Tuple[int, int]],
    ) -> float:
        pass
