import pygame
from SnakeGame import SnakeGame, Direction

# Main
if __name__ == "__main__":
  levelDefinition = [ "                                "
                    , " ############################## "
                    , " #                            # "
                    , " #                            # "
                    , " #                            # "
                    , " #                            # "
                    , " #                            # "
                    , " #                            # "
                    , " #                            # "
                    , " #                            # "
                    , " #                            # "
                    , " #                            # "
                    , " #                            # "
                    , " #                            # "
                    , " #                            # "
                    , " #                            # "
                    , " #                            # "
                    , " #                            # "
                    , " #                            # "
                    , " #                            # "
                    , " #                            # "
                    , " #                            # "
                    , " ############################## "
                    , "                               "
                    ]

  # Create game object
  game = SnakeGame(levelDefinition)

  # Initialise pygame
  successes, failures = pygame.init()
  print(f'{successes} successses and {failures} failures')

  # The pygame screen and image
  screen = pygame.display.set_mode((512, 384))

  # The timing clock
  clock = pygame.time.Clock()

  while True:
    clock.tick(10)

    snakeDir = None

    # Handle input
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        quit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
          snakeDir = Direction.up
        elif event.key == pygame.K_DOWN:
          snakeDir = Direction.down
        elif event.key == pygame.K_LEFT:
          snakeDir = Direction.left
        elif event.key == pygame.K_RIGHT:
          snakeDir = Direction.right

    # Update game
    game.update(snakeDir)

    # Clear screen and draw game
    screen.fill((0, 0, 0))
    game.draw(screen)

    pygame.display.update()
