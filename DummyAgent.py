import SnakeGame
import random

class Agent:
  def __init__(self):
    self._framerate = 10

  def step(self, env, renderer):
    randomDirection = random.choice(list(SnakeGame.Direction))
    env.step(env.Action(snakeDir = randomDirection))

    if not env.state.snakeAlive:
      env.reset()