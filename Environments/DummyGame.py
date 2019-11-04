import math
import pygame
import random
import collections

from Action import Action, Direction
import constants

# State type
State = collections.namedtuple('State', 'pos')

# Environment
class Environment:
  def __init__(self):
    self.reset()

  # Reset to default state
  def reset(self):
    self.state = self._newGame()

  # Return whether the we are alive
  def alive(self):
    return True

  # Step the game state
  def step(self, gameInput):
    self.state = self._updateGame(self.state, gameInput)
    return self.state

  # Draw the game to a pygame screen
  def render(self, screen):
    # Game objects
    sprite = pygame.Surface((16, 16))
    sprite.fill((243, 128, 128), pygame.Rect((1, 1), (14, 14)))

    screen.blit(sprite, (self.state.pos[0] * 16, self.state.pos[1] * 16))
  
  # generate a new game state
  def _newGame(self):
    return State(pos = (10, 10))

  # update game state
  def _updateGame(self, gameState, gameInput):
    gameState = self._updatePos(gameState, gameInput)
    return gameState

  # update the position
  def _updatePos(self, gameState, gameInput):
    if gameInput.direction == None:
      return gameState

    movement = gameInput.direction.toVector()
    oldPos = gameState.pos
    newPos = (oldPos[0] + movement[0], oldPos[1] + movement[1])
    return gameState._replace(pos = newPos)