import pygame
import SnakeGame
from constants import levelDefinition
from Renderer import Renderer

# Main
if __name__ == "__main__":
  # Create env
  env = SnakeGame.Environment(levelDefinition)

  # Create renderer
  renderer = Renderer(512, 384)

  while True:
    renderer.clock.tick(10)

    # Get snake dir from input
    snakeDir = None

    # Handle input
    for event in renderer.pollEvents():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
          snakeDir = env.Direction.up
        elif event.key == pygame.K_DOWN:
          snakeDir = env.Direction.down
        elif event.key == pygame.K_LEFT:
          snakeDir = env.Direction.left
        elif event.key == pygame.K_RIGHT:
          snakeDir = env.Direction.right
        elif event.key == pygame.K_r:
          env.reset()

    # Update game
    env.step(env.Action(snakeDir = snakeDir))

    # Clear screen and draw game
    renderer.draw(env.render)