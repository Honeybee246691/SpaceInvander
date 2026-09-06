import math
import random
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load('galaxy.jpg')

pygame.display.set_caption("space Invader")
icon = pygame.image.load('Spaceship.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('FighterJet.png')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for _i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('SpaceShip.png'))
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))

    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

    bulletImg = pygame.image.load('Bullet.png')
    bulletX = 0
    bulletX = 0
    bulletY = PLAYER_START_Y
    bulletX_change = 0
    bulletY_chnage = BULLET_SPEED_Y
    bullet_state = "ready"

    score_value = 0
    font = pygame.font.Font('freesansbold.ttf', 32)
    textX = 10
    textY = 10

over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
        score = font.render("Score:" + str(score_value), True, (255, 255, 255))
        screen.blit(score,(x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text,(200, 250))        