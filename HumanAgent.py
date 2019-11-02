import pygame
import SnakeGame

class Agent:
  def step(self, env, renderer):
    # Get snake dir from input
    snakeDir = None

    # Whether we should reset after the next iteration
    shouldReset = False

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
          # Delay reset until after we update so we aren't immediately started on the second iteration
          shouldReset = True

    # Update game
    env.step(env.Action(snakeDir = snakeDir))

    # Reset if dead
    if shouldReset or not env.state.snakeAlive:
      shouldReset = False
      env.reset()
