import random
from abc import ABC, abstractmethod
from typing import Sequence


class AbstractInitializer(ABC):

    class_type = "Initializer"

    def __init__(self):
        pass

    @abstractmethod
    def __call__(
        self, seat_places: Sequence[tuple[int, int]], members: Sequence[dict]
    ) -> float:
        raise NotImplementedError("This method must be override and return float.")


class RandomInitializer(AbstractInitializer):
    def __init__(self):
        super().__init__()

    def __call__(
        self, seat_places: Sequence[tuple[int, int]], members: Sequence[dict]
    ) -> list[tuple[int, int]]:
        mem_places = random.sample(seat_places, len(members))
        return mem_places


class RandomGlassesInitializer(AbstractInitializer):
    """
    Random Glasses Initializer.

    Note
    ----------
    members directory must have 'glasses' key.
    """

    def __init__(self):
        super().__init__()

    def __call__(
        self, seat_places: Sequence[tuple[int, int]], members: Sequence[dict]
    ) -> list[tuple[int, int]]:
        # TODO write this
        pass
