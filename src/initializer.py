import random
import copy
from abc import ABC, abstractmethod
from typing import Sequence, Tuple


class AbstractInitializer(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def transform(
        self, seat_places: Sequence[Tuple[int, int]], members: Sequence[dict]
    ):
        pass


class RandomInitializer(AbstractInitializer):
    def __init__(self):
        super().__init__()

    def transform(
        self, seat_places: Sequence[Tuple[int, int]], members: Sequence[dict]
    ):
        mem_places = random.sample(seat_places, len(members))
        return mem_places
