# -------------------------------------------------------------------------------------------------
# --- PREAMBLE ---
import random
import math

# used for the map drawing
EMPTY_SPACE = "."
START_LOCATION = "S"
END_LOCATION = "E"
GRAVITY_WELL = "G"
GRAVITY = "#"
ASTEROID = "A"
PATH = "O"


# -------------------------------------------------------------------------------------------------
# --- CONVENIENCE STUFF ---
def add(vec1, vec2):
    """vector addition on tuples (or lists)"""
    return tuple(sum(x) for x in zip(vec1, vec2))


def neighbours(vec, prox=1, bounds=1000):
    """returns vectors within 'prox' distance of vec, inside a grid of (bounds x bounds)"""
    return {add(vec, grid_vec) for grid_vec in
            {(x, y) for x in range(-prox, 1 + prox) for y in range(-prox, 1 + prox)
             if x or y} if 0 <= add(vec, grid_vec)[0] < bounds and 0 <= add(vec, grid_vec)[1] < bounds}


def d_tc(vec1, vec2):
    """the taxi-cab metric on real n-space---you can only move horizontally/vertically"""
    return sum(abs(x1 - x2) for x1, x2 in zip(vec1, vec2))


def d_ch(vec1, vec2):
    """the Chebyshev metric---when you can move diagonally as well as horizontal/vertical"""
    return d_tc(vec1, vec2) - min(abs(x1 - x2) for x1, x2 in zip(vec1, vec2))


# -------------------------------------------------------------------------------------------------
# --- THE HEART OF THE BEAST ---
class Galaxy:
    """
    Implements a 2D grid class, representing the map of our Galaxy. Has a populate method to
    populate the Galaxy according to the arguments passed to a particular instance, and a path_find
    method which returns a new Galaxy instance whose map shows the path.
    """

    def __init__(self, size, start, end, astrds, grav_wells):
        self.size = size
        self.start = start
        self.end = end
        self.astrds = 20
        self.grav_wells = 5
        self._map = {(x, y): EMPTY_SPACE for x in range(size) for y in range(size)}

    def __getitem__(self, key):
        return self._map[key]

    def __setitem__(self, key, value):
        self._map[key] = value

    def __iter__(self):
        return iter(self._map)

    def __str__(self):
        lines = []
        for height in range(self.size):
            lines.append(" ".join(self._map[(width, height)] for width in range(self.size)))
        return "\n".join(lines)

    def populate(self):
        self[self.start] = START_LOCATION
        self[self.end] = END_LOCATION

        for count, pos in enumerate(random.sample(
                {tup for tup in self if tup not in {self.start, self.end}}, self.astrds + self.grav_wells)):
                if count < self.astrds:
                    self[pos] = ASTEROID
                else:
                    self[pos] = GRAVITY_WELL
                    gravity_neighbors = neighbours(self[pos], bounds=self.size)
                    for each in gravity_neighbors:
                        self[self.each] = GRAVITY

    def path_find(self):
        unpathable_pos = {pos for pos in self if (self[pos] in {ASTEROID, GRAVITY_WELL}) or
                          ({self[nearby] for nearby in neighbours(pos, bounds=self.size)} & {GRAVITY_WELL})}
        # _closed contains fully-investigated nodes
        _closed = {}
        # _open contains node-(parent, dist-from-start) key-value pairs, for nodes still under
        # investigation
        _open = {self.start: (None, 0)}

        success = False

        while _open:
            # get the most promising node in _open
            cur_node = min(_open, key=lambda vec: _open[vec][1] + d_ch(vec, self.end))

            _closed.update({cur_node: _open[cur_node]})
            del _open[cur_node]

            if cur_node == self.end:
                success = True
                break

            for nbr in neighbours(cur_node, prox=1, bounds=self.size):
                nbr_dist = _closed[cur_node][1] + 1
                # if the neighbour node is unpathable then disregard it!
                if nbr in unpathable_pos | set(_closed):
                    pass
                # else for the neighbours: if it's new (or it's old and we've found a better path to
                # it), update our records accordingly
                elif nbr not in _open or (nbr in _open and nbr_dist < _open[nbr][1]):
                    _open.update({nbr: (cur_node, nbr_dist)})

        # allows us to backtrack from any node to the start
        def parents(node, data, children=[]):
            if data[node][0]:
                return parents(data[node][0], data, [node] + children)
            else:
                return [node] + children

        new_galaxy = Galaxy(self.size, self.start, self.end, self.astrds, self.grav_wells)
        new_galaxy._map = self._map

        # show the best path we've got on new_galaxy's map
        if success:
            path = parents(self.end, _closed)
            for pos in path[1:-1]:
                new_galaxy._map[pos] = PATH
        else:
            closest_node = min(_closed, key=lambda vec: d_ch(vec, self.end))
            path = parents(closest_node, _closed)
            for pos in path[1:]:
                new_galaxy._map[pos] = PATH

        return new_galaxy, success, len(path)


# -------------------------------------------------------------------------------------------------
# --- MAIN FUNCTION ---
def main():
    # layout stores the dimensions (10 x 10), as well as start (0, 0) and end (9, 9) positions
    layout = 10, (0, 0), (9, 9)
    # properties stores the number of asteroids (20%) and gravity wells (5%) to put on the map
    properties = tuple(round((num / 100) * layout[0] ** 2) for num in [20, 5])

    space = Galaxy(*layout + properties)
    space.populate()

    print("-" * 2 * layout[0])
    print(space)

    pathed_space, success, length = space.path_find()

    print("-" * 2 * layout[0])
    print(pathed_space)
    print("The probe was {}succesful; the best path (shown above) has length {}.".format(
        ["un", ""][int(success)], length))

if __name__ == "__main__":
    main()
