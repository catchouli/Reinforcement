import random
import pygame
import collections

successes, failures = pygame.init()
print(f'{successes} successses and {failures} failures')

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

# The pygame screen and image
screen = pygame.display.set_mode((512, 384))

# Game objects
wallSprite = pygame.Surface((16, 16))
wallSprite.fill((255, 255, 255), pygame.Rect((1, 1), (14, 14)))
snakeSprite = pygame.Surface((16, 16))
snakeSprite.fill((0, 0, 255), pygame.Rect((1, 1), (14, 14)))
foodSprite = pygame.Surface((16, 16))
foodSprite.fill((0, 255, 0), pygame.Rect((1, 1), (14, 14)))

# The timing clock
clock = pygame.time.Clock()

def randomFoodPos():
  return (random.randint(3, 28), random.randint(3, 20))

def foodGet():
  global snakeLength, foodPos
  snakeLength += 1
  foodPos = randomFoodPos()

def resetGame():
  global snakePos, snakeDir, snakeLength, snakeBlocks, foodPos
  snakePos = (16, 12)
  snakeDir = (0, -1)
  snakeLength = 1
  snakeBlocks = [snakePos]
  foodPos = randomFoodPos()

resetGame()

while True:
  clock.tick(10)

  # Update game
  if snakePos == foodPos:
    foodGet()
  snakePos = (snakePos[0] + snakeDir[0], snakePos[1] + snakeDir[1])

  wallBlock = levelDefinition[snakePos[1]][snakePos[0]]
  if wallBlock == '#':
    resetGame()

  if snakePos in snakeBlocks:
    resetGame()

  snakeBlocks += [snakePos]
  while len(snakeBlocks) > snakeLength:
    snakeBlocks.pop(0)

  # Handle input
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      quit()
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP and (snakeLength == 1 or snakeDir != (0, 1)):
        snakeDir = (0, -1)
      elif event.key == pygame.K_DOWN and (snakeLength == 1 or snakeDir != (0, -1)):
        snakeDir = (0, 1)
      elif event.key == pygame.K_LEFT and (snakeLength == 1 or snakeDir != (1, 0)):
        snakeDir = (-1, 0)
      elif event.key == pygame.K_RIGHT and (snakeLength == 1 or snakeDir != (-1, 0)):
        snakeDir = (1, 0)

  # Clear screen
  screen.fill((0, 0, 0))

  # Draw walls
  for y, row in enumerate(levelDefinition):
    for x, char in enumerate(row):
      if char == '#':
        screen.blit(wallSprite, (x * 16, y * 16))

  # Draw food
  screen.blit(foodSprite, (foodPos[0] * 16, foodPos[1] * 16))

  # Draw snake
  for snakePos in snakeBlocks:
    screen.blit(snakeSprite, (snakePos[0] * 16, snakePos[1] * 16))

  pygame.display.update()
