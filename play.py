import sys
import pygame
import SnakeGame
from constants import levelDefinition
from Renderer import Renderer

# Main
if __name__ == "__main__":
  agent = "HumanAgent"
  if len(sys.argv) > 1:
    agent = sys.argv[1]

  # Load agent
  print(f"Starting agent {agent}")
  Agent = __import__(agent).Agent

  # Create env
  env = SnakeGame.Environment(levelDefinition)

  # Create renderer
  renderer = Renderer(512, 384)

  # Create agent
  agent = Agent()

  while True:
    renderer.clock.tick(10)
    agent.step(env, renderer)
    renderer.pollEvents()
    renderer.draw(env.render)