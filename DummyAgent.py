import SnakeGame
import random

class Agent:
  def step(self, env, renderer):
    (x, y) = env.state.snakePos
    curDir = env.state.snakeDir
    levelDef = env.levelDefinition

    directions = []

    # Pick a direction only if there's no wall that way
    # and it's not the opposite direction we're currently going
    if levelDef[y-1][x] != '#' and curDir != env.Direction.down:
      directions += [env.Direction.up]
    if levelDef[y+1][x] != '#' and curDir != env.Direction.up:
      directions += [env.Direction.down]
    if levelDef[y][x-1] != '#' and curDir != env.Direction.right:
      directions += [env.Direction.left]
    if levelDef[y][x+1] != '#' and curDir != env.Direction.left:
      directions += [env.Direction.right]

    env.step(env.Action(snakeDir = random.choice(directions)))

    if not env.state.snakeAlive:
      env.reset()
