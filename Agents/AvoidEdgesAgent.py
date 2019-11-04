import random
from Action import Action, Direction

class Agent:
  def step(self, env, renderer):
    (x, y) = env.state.snakePos
    curDir = env.state.snakeDir
    levelDef = env.levelDefinition

    directions = []

    # Pick a direction only if there's no wall that way
    # and it's not the opposite direction we're currently going
    if levelDef[y-1][x] != '#' and curDir != Direction.down:
      directions += [Direction.up]
    if levelDef[y+1][x] != '#' and curDir != Direction.up:
      directions += [Direction.down]
    if levelDef[y][x-1] != '#' and curDir != Direction.right:
      directions += [Direction.left]
    if levelDef[y][x+1] != '#' and curDir != Direction.left:
      directions += [Direction.right]

    env.step(Action(direction = random.choice(directions)))

    if not env.state.snakeAlive:
      env.reset()
