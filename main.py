# main.py

import pygame
import sys
from screen import GameScreen

def run_game():
  pygame.init()
  screen_width = 800
  screen_height = 500
  game_screen = GameScreen(screen_width, screen_height)

  # Main game loop
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

    
    
    game_screen.clear_screen()
    game_screen.update_display()
    pygame.time.Clock().tick(60)

if __name__ == "__main__":
  run_game()
