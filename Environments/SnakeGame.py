import math
import pygame
import random
import collections

from Action import Action, Direction
import constants

# State type
State = collections.namedtuple('State',
  'snakeAlive snakePos snakeDir snakeLength snakeBlocks foodPos')

# Environment
class Environment:
  def __init__(self):
    self.levelDefinition = constants.levelDefinition
    self.levelDimensions = (len(self.levelDefinition[0]), len(self.levelDefinition))
    self.reset()

  # Reset to default state
  def reset(self):
    self.state = self._newGame()

  # Return whether the snake is alive
  def alive(self):
    return self.state.snakeAlive

  # Step the game state
  def step(self, gameInput):
    self.state = self._updateGame(self.state, gameInput)
    return self.state

  # Draw the game to a pygame screen
  def render(self, screen):
    # Game objects
    wallSprite = pygame.Surface((16, 16))
    wallSprite.fill((255, 255, 255), pygame.Rect((1, 1), (14, 14)))
    snakeSprite = pygame.Surface((16, 16))
    snakeSprite.fill((243, 128, 128), pygame.Rect((1, 1), (14, 14)))
    foodSprite = pygame.Surface((16, 16))
    foodSprite.fill((0, 255, 0), pygame.Rect((1, 1), (14, 14)))

    # Draw walls
    for y, row in enumerate(self.levelDefinition):
      for x, char in enumerate(row):
        if char == '#':
          screen.blit(wallSprite, (x * 16, y * 16))

    # Draw food
    screen.blit(foodSprite, (self.state.foodPos[0] * 16, self.state.foodPos[1] * 16))

    # Draw snake
    for snakePos in self.state.snakeBlocks:
      screen.blit(snakeSprite, (snakePos[0] * 16, snakePos[1] * 16))
  
  # generate a new game state
  def _newGame(self):
    defaultSnakePos = tuple(map(lambda x: math.floor(x / 2), self.levelDimensions))
    return State(
      snakeAlive = True,
      snakePos = defaultSnakePos,
      snakeDir = Direction.up,
      snakeLength = 1,
      snakeBlocks = [defaultSnakePos],
      foodPos = Environment._randomFoodPos())

  # generate a new random position for the food
  def _randomFoodPos():
    return (random.randint(3, 28), random.randint(3, 20))

  # update game state
  def _updateGame(self, gameState, gameInput):
    if not gameState.snakeAlive:
      return gameState

    gameState = self._updateSnakeDir(gameState, gameInput)
    gameState = self._updateSnakePos(gameState)
    gameState = self._updateFood(gameState)
    gameState = self._updateSnakeAlive(gameState)
    return gameState

  # update the snake's direction
  def _updateSnakeDir(self, gameState, gameInput):
    if gameInput.direction != None and gameState.snakeDir != gameInput.direction.opposite():
      return gameState._replace(snakeDir = gameInput.direction)
    else:
      return gameState

  # update the snake's position
  def _updateSnakePos(self, gameState):
    movement = gameState.snakeDir.toVector()
    oldPos = gameState.snakePos
    newPos = (oldPos[0] + movement[0], oldPos[1] + movement[1])
    snakeLength = gameState.snakeLength
    newSnakeBlocks = [newPos] + gameState.snakeBlocks[:snakeLength-1]
    return gameState._replace(snakePos = newPos, snakeBlocks = newSnakeBlocks)

  # let the player collect food
  def _updateFood(self, gameState):
    if gameState.snakePos == gameState.foodPos:
      return gameState._replace(
        snakeLength = gameState.snakeLength + 1,
        foodPos = Environment._randomFoodPos())
    else:
      return gameState

  # check if the snake should be dead due to a self or wall collision
  def _updateSnakeAlive(self, gameState):
    block = self.levelDefinition[gameState.snakePos[1]][gameState.snakePos[0]]
    touchingSelf = gameState.snakePos in gameState.snakeBlocks[1:]
    touchingWall = block == '#'
    return gameState._replace(snakeAlive = not (touchingSelf or touchingWall))