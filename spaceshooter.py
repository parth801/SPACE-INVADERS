import pygame
import os
pygame.init()
pygame.font.init()
WIDTH =  900
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders game")
pygame.display.update()
vel = 5
fps = 60
white  = "white"
bullet_vel = 7
max_bullets  = 3
black  = (0, 0, 0)
red = "red"
yellow =  "yellow"
border = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)
spaceship_width = 55
spaceship_height = 40
space = pygame.transform.scale(pygame.image.load("background.png"), (WIDTH, HEIGHT ))

yellow_spaceship_image = pygame.image.load("spaceship2.png")
yellow_spaceship   = pygame.transform.rotate(pygame.transform.scale(yellow_spaceship_image, (spaceship_width, spaceship_height)), 90)

red_spaceship_image = pygame.image.load("spaceship 1.png")
red_spaceship   = pygame.transform.rotate(pygame.transform.scale(red_spaceship_image, (spaceship_width, spaceship_height)), 270)



def Drawwindow(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    screen.blit(space, (0, 0))
    screen.blit(yellow_spaceship, (100, 200))
    screen.blit(red_spaceship, (200, 100))

    for i in red_bullets:
        pygame.draw.rect(screen, "red",  bullet)

    for i in yellow_bullets:
        pygame.draw.rect(screen, "yellow", bullet)
    
    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x  - vel>0:
        yellow.x-=vel
    if keys_pressed[pygame.K_d] and yellow.x  + yellow.width<border.x:
        yellow.x+=vel
    if keys_pressed[pygame.K_w] and yellow.y  - vel>0:
        yellow.y-=vel
    if keys_pressed[pygame.K_s] and yellow.y  + yellow.height<HEIGHT.y:
        yellow.y+=vel

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x  - vel>0:
            red.x-=vel
    if keys_pressed[pygame.K_RIGHT] and red.x  + red.width<WIDTH:
            red.x+=vel
    if keys_pressed[pygame.K_UP] and red.y  - vel>0:
            red.y-=vel
    if keys_pressed[pygame.K_DOWN] and red.y  + red.height<HEIGHT-15:
            red.y+=vel

def handle_bullets(yellow_bullets,):

    run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    Drawwindow(red, yellow, None,  None, None, None)
    pygame.display.update()
