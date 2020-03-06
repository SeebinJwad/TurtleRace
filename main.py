import pygame
import random
import time

pygame.init()
gameDisplay = pygame.display.set_mode((350, 650))
pygame.display.set_caption("Turtle Race")
white = (255, 255, 255)
black = (0, 0, 0)
light_blue = (225, 255, 255)
# darker light blue for the starting and finish line
light_blue2 = (150, 195, 255)
brown = (150, 150, 150)

# color randomize


def gameLoop():

    color_list = []
    for colors in range(4):
        color_list.append((random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))

    y_pos = 600
    x_pos = 0

    gameOver = False
    increment = 5

    min_val = 10
    move_list = []
    count = 0

    # From 550 to 50 where finish line is
    # Divided it by min_val for array storing scenario where all 4 turtles go min_val entire race
    x1, x2, x3, x4 = 0, 0, 0, 0
    for x in range(int(500/min_val)):
        # random increment 1 - 4
        rnd1, rnd2, rnd3, rnd4 = random.randrange(min_val, 31, increment), random.randrange(min_val, 31, increment),\
                                 random.randrange(min_val, 31, increment), random.randrange(min_val, 31, increment)
        move_list.append(x1 + rnd1)
        move_list.append(x2 + rnd2)
        move_list.append(x3 + rnd3)
        move_list.append(x4 + rnd4)
        x1 += rnd1
        x2 += rnd2
        x3 += rnd3
        x4 += rnd4
    print(move_list)
    while not gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True

        gameDisplay.fill(light_blue)

        for x in range(4):
            if count == 196:
                gameLoop()
            pygame.draw.rect(gameDisplay, color_list[x], [x_pos+(x * 50) + (x * 30) + 40, y_pos - move_list[x + count], 30, 30])
            time.sleep(.1)
            pygame.draw.rect(gameDisplay, color_list[x], [x_pos+(x * 50) + (x * 30) + 53, y_pos, 4, -1 * move_list[x+count]+5])
        count += 4

        pygame.draw.rect(gameDisplay, brown, [0, 600, 350, 50])
        pygame.draw.rect(gameDisplay, light_blue2, [0, 60, 350, 20])
        pygame.display.update()
    pygame.quit()
    quit()


gameLoop()
