import pygame

# pygame renderer
class Renderer:
  def __init__(self, width, height):
    self.width = width
    self.height = height

    # initialise pygame
    successes, failures = pygame.init()
    print(f'{successes} successses and {failures} failures')

    self.screen = pygame.display.set_mode((width, height))
    self.clock = pygame.time.Clock()

  def pollEvents(self):
    events = pygame.event.get()
    if any(x for x in events if x.type == pygame.QUIT):
      return quit()
    else:
      return events

  def draw(self, f):
    self.screen.fill((0, 0, 0))
    f(self.screen)
    pygame.display.update()