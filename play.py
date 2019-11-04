import sys
from Renderer import Renderer

# Imports a module even if it's a submodule e.g. a.b.c returns the module 'c'
def importModule(modpath):
  mod = __import__(modpath)
  submodules = modpath.split(".")[1:]
  for submodule in submodules:
    mod = getattr(mod, submodule)
  return mod

# Main
if __name__ == "__main__":
  envName = "SnakeGame"
  if len(sys.argv) > 1:
    envName = sys.argv[1]

  agentName = "HumanAgent"
  if len(sys.argv) > 2:
    agentName = sys.argv[2]

  # Create env
  print (f"Creating env {envName}")
  Environment = importModule(f'Environments.{envName}').Environment
  env = Environment()

  # Load agent
  print(f"Starting agent {agentName}")
  Agent = importModule(f'Agents.{agentName}').Agent
  agent = Agent()

  # Create renderer
  renderer = Renderer(512, 384)

  while True:
    renderer.clock.tick(10)
    agent.step(env, renderer)
    renderer.pollEvents()
    renderer.draw(env.render)