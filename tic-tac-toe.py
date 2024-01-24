import sys
import runpy
import pygame
import random
import time

# Library Initialization
pygame.init()
pygame.font.init()
pygame.display.set_caption("Tic Tac Toe")

# Colour Codes
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Board Specifications
width = 480
rows = 3
box_width = width // rows
screen = pygame.display.set_mode((width, (width + (width // 15))))

# Misc
game_end = False
font = pygame.font.SysFont("arial", (width // 15))
font_huge = pygame.font.SysFont("arial", (width // 3))
winner = None
x_position = []
o_position = []


# Board grid
# 1 2 3
# 4 5 6
# 7 8 9


# Draws the board
def board():
    xx = 0
    yy = 0

    screen.fill(white)
    pygame.draw.line(screen, black, (0, 0), (width, 0))
    pygame.draw.line(screen, black, (0, width), (width, width))
    pygame.draw.line(screen, black, (0, 0), (0, width))
    pygame.draw.line(screen, black, (width, 0), (width, width))

    for i in range(rows):
        xx = xx + box_width
        yy = yy + box_width
        pygame.draw.line(screen, black, (xx, 0), (xx, width))
        pygame.draw.line(screen, black, (0, yy), (width, yy))


# Draws the XO
def draw_xo():
    order = 0

    for i in range(2):

        ii = 0

        if order == 0:
            position = x_position
        elif order == 1:
            position = o_position

        for j in range(len(position)):

            char_width = 0
            char_height = 0

            # Determine the horizontal position of the X or O
            if position[ii] == 1 or position[ii] == 4 or position[ii] == 7:
                char_width = 6
            if position[ii] == 2 or position[ii] == 5 or position[ii] == 8:
                char_width = 2
            if position[ii] == 3 or position[ii] == 6 or position[ii] == 9:
                char_width = (6 / 5)

            # Determine the vertical position of the X or O
            if position[ii] == 1 or position[ii] == 2 or position[ii] == 3:
                char_height = 6
            if position[ii] == 4 or position[ii] == 5 or position[ii] == 6:
                char_height = 2
            if position[ii] == 7 or position[ii] == 8 or position[ii] == 9:
                char_height = (6 / 5)

            # Draw either the X or O
            if position == x_position:
                x_icon = font_huge.render("X", True, red)
                x_icon_rect = x_icon.get_rect(center=(width // char_width, width // char_height))
                screen.blit(x_icon, x_icon_rect)
            if position == o_position:
                o_icon = font_huge.render("O", True, blue)
                o_icon_rect = o_icon.get_rect(center=(width // char_width, width // char_height))
                screen.blit(o_icon, o_icon_rect)

            ii += 1

        order += 1


# Draws the scoreboard
def scoreboard():
    pygame.draw.rect(screen, white, ((0, (width + 1)), (width, 65)))
    screen.blit(font.render("Turn:", True, black), (width // 200, width))
    screen.blit(font.render(XO.upper(), True, black), ((width // 6), width))


# Draw the end screen
def end_screen():
    screen.fill(white)
    screen.blit(font.render("GAME OVER", True, red), ((width // 4), (width // 4)))
    screen.blit(font.render("Winner:", True, blue), ((width // 4), (width // 4) + (width // 10)))
    screen.blit(font.render(str(XO.upper()), True, blue), (((width // 4) * 2), (width // 4) + (width // 10)))
    screen.blit(font.render("ESC - Quit", True, black), ((width // 4), (width // 2)))
    screen.blit(font.render("SPACE - Restart", True, black), ((width // 4), ((width // 2) + (width // 10))))
    screen.blit(font.render("TAB - Main Menu", True, black), ((width // 4), ((width // 2) + 2 * (width // 10))))


# Randomize who starts
XO_num = random.randint(0, 1)
if XO_num == 0:
    XO = "x"
elif XO_num == 1:
    XO = "o"

while not game_end:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                sys.exit()

            if event.key == pygame.K_TAB:
                runpy.run_module(mod_name="Simple Mini Games")

        if event.type == pygame.MOUSEBUTTONDOWN:

            # Mouse click position
            if 0 < pygame.mouse.get_pos()[0] < (width // 3) and 0 < pygame.mouse.get_pos()[1] < (width // 3):
                if XO == "x":
                    if 1 in o_position:
                        pass
                    else:
                        x_position.append(1)
                        XO = "o"
                elif XO == "o":
                    if 1 in x_position:
                        pass
                    else:
                        o_position.append(1)
                        XO = "x"
            if 0 < pygame.mouse.get_pos()[1] < (width // 3) < pygame.mouse.get_pos()[0] < ((width // 3) * 2):
                if XO == "x":
                    if 2 in o_position:
                        pass
                    else:
                        x_position.append(2)
                        XO = "o"
                elif XO == "o":
                    if 2 in x_position:
                        pass
                    else:
                        o_position.append(2)
                        XO = "x"
            if ((width // 3) * 2) < pygame.mouse.get_pos()[0] < width and 0 < pygame.mouse.get_pos()[1] < (width // 3):
                if XO == "x":
                    if 3 in o_position:
                        pass
                    else:
                        x_position.append(3)
                        XO = "o"
                elif XO == "o":
                    if 3 in x_position:
                        pass
                    else:
                        o_position.append(3)
                        XO = "x"
            if 0 < pygame.mouse.get_pos()[0] < (width // 3) < pygame.mouse.get_pos()[1] < ((width // 3) * 2):
                if XO == "x":
                    if 4 in o_position:
                        pass
                    else:
                        x_position.append(4)
                        XO = "o"
                elif XO == "o":
                    if 4 in x_position:
                        pass
                    else:
                        o_position.append(4)
                        XO = "x"
            if (width // 3) < pygame.mouse.get_pos()[0] < ((width // 3) * 2) and (width // 3) < pygame.mouse.get_pos()[1] < ((width // 3) * 2):
                if XO == "x":
                    if 5 in o_position:
                        pass
                    else:
                        x_position.append(5)
                        XO = "o"
                elif XO == "o":
                    if 5 in x_position:
                        pass
                    else:
                        o_position.append(5)
                        XO = "x"
            if (width // 3) < pygame.mouse.get_pos()[1] < ((width // 3) * 2) < pygame.mouse.get_pos()[0] < width:
                if XO == "x":
                    if 6 in o_position:
                        pass
                    else:
                        x_position.append(6)
                        XO = "o"
                elif XO == "o":
                    if 6 in x_position:
                        pass
                    else:
                        o_position.append(6)
                        XO = "x"
            if 0 < pygame.mouse.get_pos()[0] < (width // 3) and ((width // 3) * 2) < pygame.mouse.get_pos()[1] < width:
                if XO == "x":
                    if 7 in o_position:
                        pass
                    else:
                        x_position.append(7)
                        XO = "o"
                elif XO == "o":
                    if 7 in x_position:
                        pass
                    else:
                        o_position.append(7)
                        XO = "x"
            if (width // 3) < pygame.mouse.get_pos()[0] < ((width // 3) * 2) < pygame.mouse.get_pos()[1] < width:
                if XO == "x":
                    if 8 in o_position:
                        pass
                    else:
                        x_position.append(8)
                        XO = "o"
                elif XO == "o":
                    if 8 in x_position:
                        pass
                    else:
                        o_position.append(8)
                        XO = "x"
            if ((width // 3) * 2) < pygame.mouse.get_pos()[0] < width and ((width // 3) * 2) < pygame.mouse.get_pos()[1] < width:
                if XO == "x":
                    if 9 in o_position:
                        pass
                    else:
                        x_position.append(9)
                        XO = "o"
                elif XO == "o":
                    if 9 in x_position:
                        pass
                    else:
                        o_position.append(9)
                        XO = "x"

    board()
    draw_xo()
    scoreboard()
    pygame.display.update()

    # Check for win
    # Check row
    if 1 in x_position and 2 in x_position and 3 in x_position or 1 in o_position and 2 in o_position and 3 in o_position:
        pygame.draw.line(screen, black, ((width // 30), (width // 6)), ((width - (width // 30)), (width // 6)), (width // 50))
        if XO == "x":
            XO = "o"
        elif XO == "o":
            XO = "x"
        pygame.display.update()
        time.sleep(1)
        game_end = True
    if 4 in x_position and 5 in x_position and 6 in x_position or 4 in o_position and 5 in o_position and 6 in o_position:
        pygame.draw.line(screen, black, ((width // 30), ((width // 6) * 3)), ((width - (width // 30)), ((width // 6) * 3)), (width // 50))
        pygame.display.update()
        if XO == "x":
            XO = "o"
        elif XO == "o":
            XO = "x"
        time.sleep(1)
        game_end = True
    if 7 in x_position and 8 in x_position and 9 in x_position or 7 in o_position and 8 in o_position and 9 in o_position:
        pygame.draw.line(screen, black, ((width // 30), ((width // 6) * 5)), ((width - (width // 30)), ((width // 6) * 5)), (width // 50))
        pygame.display.update()
        if XO == "x":
            XO = "o"
        elif XO == "o":
            XO = "x"
        time.sleep(1)
        game_end = True
    # Check columns
    if 1 in x_position and 4 in x_position and 7 in x_position or 1 in o_position and 4 in o_position and 7 in o_position:
        pygame.draw.line(screen, black, ((width // 6), (width // 30)), ((width // 6), (width - (width // 30))), (width // 50))
        if XO == "x":
            XO = "o"
        elif XO == "o":
            XO = "x"
        pygame.display.update()
        time.sleep(1)
        game_end = True
    if 2 in x_position and 5 in x_position and 8 in x_position or 2 in o_position and 5 in o_position and 8 in o_position:
        pygame.draw.line(screen, black, (((width // 6) * 3), (width // 30)), (((width // 6) * 3), (width - (width // 30))), (width // 50))
        pygame.display.update()
        if XO == "x":
            XO = "o"
        elif XO == "o":
            XO = "x"
        time.sleep(1)
        game_end = True
    if 3 in x_position and 6 in x_position and 9 in x_position or 3 in o_position and 6 in o_position and 9 in o_position:
        pygame.draw.line(screen, black, (((width // 6) * 5), (width // 30)), (((width // 6) * 5), (width - (width // 30))), (width // 50))
        pygame.display.update()
        if XO == "x":
            XO = "o"
        elif XO == "o":
            XO = "x"
        time.sleep(1)
        game_end = True
    # Check diagonals
    if 1 in x_position and 5 in x_position and 9 in x_position or 1 in o_position and 5 in o_position and 9 in o_position:
        pygame.draw.line(screen, black, ((width // 30), (width // 30)), ((width - (width // 30)), (width - (width // 30))), (width // 50))
        pygame.display.update()
        if XO == "x":
            XO = "o"
        elif XO == "o":
            XO = "x"
        time.sleep(1)
        game_end = True
    if 3 in x_position and 5 in x_position and 7 in x_position or 3 in o_position and 5 in o_position and 7 in o_position:
        pygame.draw.line(screen, black, ((width - (width // 30)), (width // 30)), ((width // 30), (width - (width // 30))), (width // 50))
        pygame.display.update()
        if XO == "x":
            XO = "o"
        elif XO == "o":
            XO = "x"
        time.sleep(1)
        game_end = True

    # Check for draw
    if len(x_position) + len(o_position) == 9 and not game_end:
        time.sleep(0.5)
        XO = "draw"
        game_end = True

    time.sleep(0.1)

    while game_end:

        end_screen()
        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    sys.exit()

                if event.key == pygame.K_SPACE:
                    game_end = False
                    runpy.run_module(mod_name="Tic Tac Toe")

                if event.key == pygame.K_TAB:
                    runpy.run_module(mod_name="Simple Mini Games")
 