import pygame
from Action import Direction, Action

class Agent:
  def step(self, env, renderer):
    # Get direction from input
    dir = None

    # Whether we should reset after the next iteration
    shouldReset = False

    # Handle input
    for event in renderer.pollEvents():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
          dir = Direction.up
        elif event.key == pygame.K_DOWN:
          dir = Direction.down
        elif event.key == pygame.K_LEFT:
          dir = Direction.left
        elif event.key == pygame.K_RIGHT:
          dir = Direction.right
        elif event.key == pygame.K_r:
          # Delay reset until after we update so we aren't immediately started on the second iteration
          shouldReset = True

    # Update game
    env.step(Action(direction = dir))

    # Reset if dead
    if shouldReset or not env.alive():
      shouldReset = False
      env.reset()
