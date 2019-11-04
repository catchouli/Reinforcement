import collections
from enum import Enum

# Direction enum
class Direction(Enum):
  up = 1
  down = 2
  left = 3
  right = 4

  def toVector(self):
    return {
      Direction.up: (0, -1),
      Direction.down: (0, 1),
      Direction.left: (-1, 0),
      Direction.right: (1, 0)
    }.get(self)

  def opposite(self):
    return {
      Direction.up: Direction.down,
      Direction.down: Direction.up,
      Direction.left: Direction.right,
      Direction.right: Direction.left
    }.get(self)

# Action type
Action = collections.namedtuple('Action', 'direction')