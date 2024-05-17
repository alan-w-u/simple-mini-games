import sys
import runpy
import pygame
import random

# Library Initialization
pygame.init()
pygame.font.init()
pygame.display.set_caption("Simple Mini Games")

# Colour Codes
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
purple = (255, 0, 255)

project_run = True

# Board Specifications
width = 480
rows = 20
box_width = width // rows
screen = pygame.display.set_mode((width, (width + (width // 15))))
font = pygame.font.SysFont("arial", (width // 15))
font_big = pygame.font.SysFont("arial", (width // 12))


def main_menu():
    screen.fill(white)
    title = font_big.render("[Simple Mini Games]", True, black)
    title_rect = title.get_rect(center=(width/2, width/4))
    screen.blit(title, title_rect)
    screen.blit(font.render("1 - Snake", True, blue), ((width // 3), (width // 4) + (width // 10)))
    screen.blit(font.render("2 - Tic Tac Toe", True, blue), ((width // 3), (width // 4) + 2*(width // 10)))
    screen.blit(font.render("3 - Pong", True, blue), ((width // 3), (width // 4) + 3*(width // 10)))
    screen.blit(font.render("4 - Random", True, blue), ((width // 3), (width // 4) + 4*(width // 10)))
    pygame.display.update()


while project_run:

    main_menu()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:

            c_x = 0
            c_y = 0

            if event.key == pygame.K_ESCAPE:
                sys.exit()

            if event.key == pygame.K_1:
                runpy.run_module(mod_name="snake")

            if event.key == pygame.K_2:
                runpy.run_module(mod_name="tic-tac-toe")

            if event.key == pygame.K_3:
                runpy.run_module(mod_name="pong")

            if event.key == pygame.K_4:
                num = random.randint(1, 3)
                if num == 1:
                    runpy.run_module(mod_name="snake")
                if num == 2:
                    runpy.run_module(mod_name="tic-tac-toe")
                if num == 3:
                    runpy.run_module(mod_name="pong")
