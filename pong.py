import sys
import runpy
import pygame
import random
import time

# Library Initialization
pygame.init()
pygame.font.init()
pygame.display.set_caption("Pong")

# Colour Codes
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Board Specifications
width = 480
length = width + (width // 2)
pad_width = width // 30
pad_height = width // 5
ball_width = width // 25
screen = pygame.display.set_mode((length, width))

# Misc
game_end = False
font = pygame.font.SysFont("arial", (width // 15))
font_huge = pygame.font.SysFont("arial", (width // 5))
winner = None
win_score = 5
hits = 0
pad_score = [0, 0]
pad_position = [width // 3, width // 3]
pad_move = [0, 0]
ball_position = [length // 2 - length // 80, width // 2]
ball_move = [0, 0]


# Draws the board
def board():
    screen.fill(white)
    pygame.draw.line(screen, black, (0, 0), (length, 0))
    pygame.draw.line(screen, black, (0, width), (length, width))
    pygame.draw.line(screen, black, (0, 0), (0, width))
    pygame.draw.line(screen, black, (length, 0), (length, width))
    pygame.draw.line(screen, black, ((length // 2), 0), ((length // 2), width))


# Draws the scoreboard
def scoreboard():
    screen.blit(font_huge.render(str(pad_score[0]), True, blue), (((length // 4) * 1.6), 0))
    screen.blit(font_huge.render(str(pad_score[1]), True, red), (((length // 4) * 2.1), 0))


# Draw the end screen
def end_screen():
    screen.fill(white)
    screen.blit(font.render("GAME OVER", True, red), ((length // 3), (width // 4)))
    screen.blit(font.render("Winner:", True, blue), ((length // 3), (width // 4) + (width // 10)))
    screen.blit(font.render(str(winner), True, blue), (((length // 3) * 1.5), (width // 4) + (width // 10)))
    screen.blit(font.render("ESC - Quit", True, black), ((length // 3), (width // 2)))
    screen.blit(font.render("SPACE - Restart", True, black), ((length // 3), ((width // 2) + (width // 10))))
    screen.blit(font.render("TAB - Main Menu", True, black), ((length // 3), ((width // 2) + 2 * (width // 10))))


def p1():
    pygame.draw.rect(screen, black, ((pad_width, pad_position[0]), (pad_width, pad_height)))


def p2():
    pygame.draw.rect(screen, black, (((length - (pad_width * 2)), pad_position[1]), (pad_width, pad_height)))


def ball():
    pygame.draw.rect(screen, black, ((ball_position[0], ball_position[1],), (ball_width, ball_width)))


def random_ball_direction():
    x_direction = random.randint(0, 1)
    if x_direction == 0:
        ball_move[0] = 5
    elif x_direction == 1:
        ball_move[0] = -5
    y_direction = random.randint(0, 1)
    if y_direction == 0:
        ball_move[1] = random.randint(1, 4)
    elif y_direction == 1:
        ball_move[1] = -random.randint(1, 4)


board()
scoreboard()
p1()
p2()
ball()
pygame.display.update()
time.sleep(1)
random_ball_direction()

while not game_end:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                sys.exit()

            if event.key == pygame.K_TAB:
                runpy.run_module(mod_name="simple-minigames")

            # Move paddles
            if event.key == pygame.K_w:
                pad_move[0] = -width // 75
            if event.key == pygame.K_s:
                pad_move[0] = width // 75

            if event.key == pygame.K_UP:
                pad_move[1] = -width // 75
            if event.key == pygame.K_DOWN:
                pad_move[1] = width // 75

        # Stop paddles
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                pad_move[0] = 0
            if event.key == pygame.K_s:
                pad_move[0] = 0
            if event.key == pygame.K_UP:
                pad_move[1] = 0
            if event.key == pygame.K_DOWN:
                pad_move[1] = 0

    # Move paddles
    pad_position[0] += pad_move[0]
    pad_position[1] += pad_move[1]
    ball_position[0] += ball_move[0]
    ball_position[1] += ball_move[1]

    # Keep paddles in screen
    if pad_position[0] < 0:
        pad_position[0] = 0
    if pad_position[0] > width - pad_height:
        pad_position[0] = width - pad_height
    if pad_position[1] < 0:
        pad_position[1] = 0
    if pad_position[1] > width - pad_height:
        pad_position[1] = width - pad_height

    # Make ball bounce off walls
    if ball_position[1] <= 0:
        ball_move[1] = abs(ball_move[1])
    if ball_position[1] >= width - ball_width:
        ball_move[1] = -abs(ball_move[1])

    # Make ball bounce off paddles
    xx = 0
    for i in range(pad_width * 2):
        yy = 0
        for j in range(pad_height + ball_width):
            if ball_position == [((pad_width * 2) - xx), pad_position[0] - ball_width + yy]:
                ball_move[0] = abs(ball_move[0])
                ball_move[1] += random.randrange(-2, 3, 1)
                if hits == 4:
                    ball_move[0] += 0.5
                    hits = 0
                hits += 1
            yy += 1
        xx += 1
    xx = 0
    for i in range(pad_width * 2):
        yy = 0
        for j in range(pad_height + ball_width):
            if ball_position == [(length - (pad_width * 2) - ball_width + xx), pad_position[1] - ball_width + yy]:
                ball_move[0] = -abs(ball_move[0])
                ball_move[1] += random.randrange(-2, 3, 1)
                if hits == 4:
                    ball_move[0] -= 0.5
                    hits = 0
                hits += 1
            yy += 1
        xx += 1

    board()
    scoreboard()
    p1()
    p2()
    ball()
    pygame.display.update()
    time.sleep(0.01)

    # Add player score
    if ball_position[0] >= length:
        pad_score[0] += 1
        ball_position = [length // 2 - length // 80, width // 2]
        random_ball_direction()
    if ball_position[0] <= -pad_width:
        pad_score[1] += 1
        ball_position = [length // 2 - length // 80, width // 2]
        random_ball_direction()

    # Determine the winner
    if pad_score[0] == win_score:
        winner = "Player 1"
        game_end = True
    elif pad_score[1] == win_score:
        winner = "Player 2"
        game_end = True

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
                    runpy.run_module(mod_name="pong")

                if event.key == pygame.K_TAB:
                    runpy.run_module(mod_name="simple-minigames")
