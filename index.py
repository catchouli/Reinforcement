import random
import pygame
import collections
from enum import Enum

# Direction type
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

# Game state type
GameState = collections.namedtuple('GameState',
  'snakePos snakeDir snakeLength snakeBlocks foodPos')

# Game logic
class SnakeGame:
  defaultSnakePos = (16, 12)

  def __init__(self, fieldWidth, fieldHeight, levelDefinition):
    self._fieldDimensions = (fieldWidth, fieldHeight)
    self._levelDefinition = levelDefinition
    self._gameState = self._newGame()

  def update(self, snakeDir):
    self._gameState = self._updateGame(self._gameState, snakeDir)

  def draw(self, screen):
    gameState = self._gameState

    # Game objects
    wallSprite = pygame.Surface((16, 16))
    wallSprite.fill((255, 255, 255), pygame.Rect((1, 1), (14, 14)))
    snakeSprite = pygame.Surface((16, 16))
    snakeSprite.fill((0, 0, 255), pygame.Rect((1, 1), (14, 14)))
    foodSprite = pygame.Surface((16, 16))
    foodSprite.fill((0, 255, 0), pygame.Rect((1, 1), (14, 14)))

    # Draw walls
    for y, row in enumerate(self._levelDefinition):
      for x, char in enumerate(row):
        if char == '#':
          screen.blit(wallSprite, (x * 16, y * 16))

    # Draw food
    screen.blit(foodSprite, (gameState.foodPos[0] * 16, gameState.foodPos[1] * 16))

    # Draw snake
    for snakePos in gameState.snakeBlocks:
      screen.blit(snakeSprite, (snakePos[0] * 16, snakePos[1] * 16))

  def _newGame(self):
    return GameState(
      snakePos = SnakeGame.defaultSnakePos,
      snakeDir = Direction.up,
      snakeLength = 1,
      snakeBlocks = [SnakeGame.defaultSnakePos],
      foodPos = self._randomFoodPos())

  def _randomFoodPos(self):
    return (random.randint(3, 28), random.randint(3, 20))

  def _snakeDead(self, gameState):
    block = self._levelDefinition[gameState.snakePos[1]][gameState.snakePos[0]]
    touchingSelf = gameState.snakePos in gameState.snakeBlocks[1:]
    touchingWall = block == '#'
    return touchingSelf or touchingWall

  def _updateGame(self, gameState, snakeDir):
    gameState = self._updateSnakeDir(gameState, snakeDir)
    gameState = self._updateSnakePos(gameState)
    gameState = self._updateFood(gameState)

    if self._snakeDead(gameState):
      return self._newGame()
    else:
      return gameState

  def _updateSnakeDir(self, gameState, snakeDir):
    if snakeDir != None and gameState.snakeDir != snakeDir.opposite():
      return gameState._replace(snakeDir = snakeDir)
    else:
      return gameState

  def _updateSnakePos(self, gameState):
    movement = gameState.snakeDir.toVector()
    oldPos = gameState.snakePos
    newPos = (oldPos[0] + movement[0], oldPos[1] + movement[1])
    snakeLength = gameState.snakeLength
    newSnakeBlocks = [newPos] + gameState.snakeBlocks[:snakeLength-1]
    return gameState._replace(snakePos = newPos, snakeBlocks = newSnakeBlocks)

  def _updateFood(self, gameState):
    if gameState.snakePos == gameState.foodPos:
      return gameState._replace(
        snakeLength = gameState.snakeLength + 1,
        foodPos = self._randomFoodPos())
    else:
      return gameState

# Main
if __name__ == "__main__":
  # Configuration
  fieldWidth = 32
  fieldHeight = 24

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
  game = SnakeGame(fieldWidth, fieldHeight, levelDefinition)

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
