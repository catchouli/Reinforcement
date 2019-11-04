import random
from Action import Action, Direction

class Agent:
  def step(self, env, renderer):
    env.step(Action(direction = random.choice(list(Direction))))
    if not env.alive():
      env.reset()
