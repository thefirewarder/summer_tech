import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")
clock = pygame.time.Clock()

player = pygame.Rect(100, HEIGHT - 100, 50, 50)
player_vel_y = 0
on_ground = False

scroll_distance = 0
SCROLL_TRIGGER_X = 500

GRAVITY = 0.5
JUMP_STRENGTH = -10
MOVE_SPEED = 5
bush_color = (220,255,220)
offset_enemy = 0
enemy_world_x = 1400
enemy_y = HEIGHT - 60
enemy_radius = 20
enemy_alive = True

ground_rects = [pygame.Rect(x * 200, HEIGHT - 50, 200, 50) for x in range(20)]
while True:
    offset_enemy += 1.5
    screen.fill((135, 206, 235))
    for i in range(1,10,2):
        pygame.draw.rect(screen, bush_color, pygame.Rect(1400*i - scroll_distance, 550, 300, 200))
    for i in range(2,11,2):
        pygame.draw.rect(screen, bush_color, pygame.Rect(1400*i - scroll_distance, 650, 100, 100))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player.x > 0:
        player.x -= MOVE_SPEED
    if keys[pygame.K_d] and player.x < 950:
        player.x += MOVE_SPEED
    if keys[pygame.K_SPACE] and on_ground:
        player_vel_y = JUMP_STRENGTH
        on_ground = False

    player_vel_y += GRAVITY
    player.y += player_vel_y

    on_ground = False
    for ground in ground_rects:
        ground_x = ground.x - scroll_distance
        ground_rect = pygame.Rect(ground_x, ground.y, ground.width, ground.height)
        if player.colliderect(ground_rect) and player_vel_y >= 0:
            player.bottom = ground_rect.top
            player_vel_y = 0
            on_ground = True
   
    if player.x > SCROLL_TRIGGER_X:
        player.x = SCROLL_TRIGGER_X
        scroll_distance += MOVE_SPEED

    for ground in ground_rects:
        ground_x = ground.x - scroll_distance
        pygame.draw.rect(screen, (100, 200, 100), (ground_x, ground.y, ground.width, ground.height))

    pygame.draw.rect(screen, (255, 0, 0), player)

    enemy_x = enemy_world_x - scroll_distance - offset_enemy
    enemy_rect = pygame.image.load("/Users/benmcintosh/Documents/eye.png").convert()
    screen.blit(enemy_rect,(enemy_x,enemy_y))
    if enemy_alive:
        pygame.draw.circle(screen, (0, 0, 255), (int(enemy_x), enemy_y), enemy_radius)

        if player.colliderect(enemy_rect):
            if player.bottom <= enemy_rect.top + 10 and player_vel_y > 0:
                enemy_alive = False
                player_vel_y = JUMP_STRENGTH
            else:
                pygame.quit()
                sys.exit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)
