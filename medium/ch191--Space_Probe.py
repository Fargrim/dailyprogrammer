from __future__ import print_function
__author__ = 'Kyle'
from itertools import product
import math
import random

EMPTY_SPACE = "."
START_LOCATION = "S"
END_LOCATION = "E"
GRAVITY_WELL = "G"
ASTEROID = "A"
PATH = "O"


class Board(object):

    def __init__(self, n, start, end):
        """
        :param n: Size of the board. n by n
        :param start: Starting location of the probe. (x, y)
        :param end: Location the probe is trying to reach. (x, y)
        """
        self.n = n
        self.start = start
        self.end = end
        if math.trunc(n * n * 0.3) <= 1:
            self.asteroids = 1
        else:
            self.asteroids = math.trunc(n * n * 0.3)
        if math.trunc(n * n * 0.1) <= 1:
            self.gravity_wells = 1
        else:
            self.gravity_wells = math.trunc(n * n * 0.1)
        self._map = {(x, y): EMPTY_SPACE for x in range(n) for y in range(n)}

    def __getitem__(self, key):
        return self._map[key]

    def __setitem__(self, key, value):
        self._map[key] = value

    def __iter__(self):
        return iter(self._map)

    def __str__(self):
        lines = []
        for height in range(self.n):
            lines.append(" ".join(self._map[(width, height)] for width in range(self.n)))
        return "\n".join(lines)

    def build_board(self):
        self[self.start] = START_LOCATION
        self[self.end] = END_LOCATION
        for count, pos in enumerate(random.sample(
                {tup for tup in self if tup not in {self.start, self.end}}, self.asteroids + self.gravity_wells)):
            if count < self.asteroids:
                self[pos] = ASTEROID
            else:
                self[pos] = GRAVITY_WELL


board = Board(3, (0, 0), (2, 2))
board.build_board()
print("-" * 2 * 3)
print(board)
