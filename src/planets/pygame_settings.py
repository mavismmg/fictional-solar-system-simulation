import pygame

pygame.font.init()

width, height = 800, 800
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Criei um Sistema Solar para você Pâmela')

white = (255, 255, 255)
yellow = (255, 255, 0)
purple = (128, 0, 128)
blue = (0, 0, 255)
red = (188, 39, 50)
green = (0, 255, 0)
dark_grey = (80, 78, 81)
black = (0, 0, 0)

font_ = pygame.font.SysFont('consolas', 16)
sub_font_ = pygame.font.SysFont('consolas', 10)