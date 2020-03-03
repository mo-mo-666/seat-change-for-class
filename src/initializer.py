import random
from typing import List


class RandomInitializer:
    def __init__(self, seat_places: List[Tuple[int, int]]):
        self.seat_places = seat_places

    def transform(self, members: List[dict]):
        places = random.sample(seat_places, len(members))
        return places
