# screen.py

import pygame

class GameScreen:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pygame Window")

  def clear_screen(self):
    self.screen.fill((38, 70, 83))  # RGB values for #264653

  def update_display(self):
    pygame.display.flip()
