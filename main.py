import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Basic game')

game_stat = ''
gravity = 1
difficulty = 1

player_img = pygame.image.load("jogging.png")
playerY = 286
playerX = 50
going = ''
t = 0

obstacleX = []
obstacleY = 300
obstacleX_change = 0.3
num_of_obstacle = 3
for i in range(num_of_obstacle):
    obstacleX.append(random.randint(800 * (i + 1) - 20, 800 * (i + 2)))

# to check if character is already jumping
pressed = False


def player(x, y):
    screen.blit(player_img, (x, y))


def obstacle(x, y):
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x, y, 20, 50))


def game_over_text():
    over_font = pygame.font.Font('freesansbold.ttf', 64)
    game_over = over_font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(game_over, (200, 250))


def is_collision(x1, y1, x2, y2):
    if x2 - 55 <= x1 <= x2 + 1 and y1 >= y2 - 60:
        return True
    else:
        return False


running = True

while running:

    # making background
    screen.fill((135, 206, 235))
    pygame.draw.rect(screen, (156, 52, 0), pygame.Rect(0, 350, 800, 300))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # checking if space bar is pressed
            if event.key == pygame.K_SPACE:
                if not pressed:
                    pressed = True
                    going = 'up'

    # check if game is still going on
    if game_stat == 'lost':
        game_over_text()

    else:

        # Assignment 1:
        if difficulty:
            if obstacleX_change < 0.4:
                obstacleX_change += 0.00001

        # Displaying and managing obstacles
        for i in range(num_of_obstacle):

            obstacle(obstacleX[i], 300)
            obstacleX[i] -= obstacleX_change

            # Re-displaying obstacles when they cross screen
            if obstacleX[i] <= -20:
                obstacleX[i] = random.randint(800 * (i + 1) + 20, 800 * (i + 2) - 40)

            # Check for Collisions
            if is_collision(playerX, playerY, obstacleX[i], obstacleY):
                game_stat = 'lost'

        # Assignment 3:
        if not gravity:
            playerY_change = (1 - 2 * obstacleX_change) / 2
            if pressed and playerY > 180 and going == 'up':
                playerY -= playerY_change
            if playerY <= 180:
                going = ''
                t = 0

            if pressed and playerY >= 286:
                pressed = False
            elif pressed and going == '':
                playerY += playerY_change

        else:
            playerY_change = (1.2 - 2 * obstacleX_change) * t
            max_speed = ((2 * (1.2 - 2 * obstacleX_change) * 100)/1000) ** (1/2)

            if pressed and playerY > 180 and going == 'up':
                playerY -= (max_speed - playerY_change)

            if pressed and playerY <= 180:
                going = ''
                t = 0

            if pressed and playerY > 286:
                pressed = False
                t = 0

            elif pressed and going == '':
                playerY += playerY_change

            if pressed:
                t += 0.001
            else:
                t = 0

        # Displaying player
        player(playerX, playerY)

    pygame.display.update()
