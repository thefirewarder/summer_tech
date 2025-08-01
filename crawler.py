import pygame
import sys
import random
import time
# Var init
world = []
for i in range(97):
    world.append([])
    for j in range(141):
        rand = random.randint(0,1)
        if rand == 0:
            world[i].append("w")
        else:
            world[i].append("h")
xPos = 0
yPos = 0
board = []
for i in range(48):
    board.append([])
    for j in range(70):
        board[i].append("")
playerX = xPos + len(board[0])/2
playerY = yPos + len(board)/2
print(playerX)
print(playerY)
# Pygame init
pygame.init()
# Screen init
infoObject = pygame.display.Info()
width = infoObject.current_w
height = infoObject.current_h-60
screen = pygame.display.set_mode((width,height))
# Font init
pygame.font.init()
firaFont = pygame.font.Font(r"C:\Users\User\Downloads\joey\FiraCode-Regular.ttf", 15)
#/////////////////////////
# Functions
def text(string, X, Y, ySpacing=10):
    lines = string.split('\n', -1)
    for i in range(len(lines)):
        txt = firaFont.render(lines[i],True,(0,255,0))
        screen.blit(txt,(X,Y + (ySpacing * i)))
def update():
    pygame.display.flip()
    screen.fill((0,0,0))
def stringArray(array):
    txt = ""
    for i in range(len(array)):
        for j in range(len(array[i])):
            txt = txt + array[i][j]
        txt = txt + "\n"
    return txt
def boardCal(X, Y):
    for i in range(48):
        for j in range(70):
            if i + Y == playerY and j + X == playerX:
                board[i][j] = " "
            else:
                board[i][j] = world[i + Y][j + X]
#/////////////////////////
# Main Loop
running = True
boardCal(xPos, yPos)
while running:
    update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                yPos-=1
            if event.key == pygame.K_s:
                yPos+=1
            if event.key == pygame.K_a:
                xPos-=1
            if event.key == pygame.K_d:
                xPos+=1
    boardCal(xPos, yPos)
    text(stringArray(board), 0, 0)
    playerX = xPos + len(board[0])/2
    playerY = yPos + len(board)/2
pygame.quit()
sys.exit()