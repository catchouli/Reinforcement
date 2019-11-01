import pygame
from SnakeGame import SnakeGame, Direction, GameState, GameInput
from constants import levelDefinition
from Renderer import Renderer

# Main
if __name__ == "__main__":
  # Create game object
  game = SnakeGame(levelDefinition)

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
          snakeDir = Direction.up
        elif event.key == pygame.K_DOWN:
          snakeDir = Direction.down
        elif event.key == pygame.K_LEFT:
          snakeDir = Direction.left
        elif event.key == pygame.K_RIGHT:
          snakeDir = Direction.right

    # Update game
    game.update(GameInput(snakeDir = snakeDir))

    # Clear screen and draw game
    renderer.draw(game.draw)