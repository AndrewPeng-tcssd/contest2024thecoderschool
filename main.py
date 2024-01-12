import pygame
from player import Player

# initialize pygame
pygame.init()

# set window
window = pygame.display.set_mode((1200, 800))


# draw window
def draw():
    window.fill((255, 255, 255))
    p.draw(window)


# game loop
run = True
frame_rate = pygame.time.Clock()
p = Player()

while run:
    # how many frames every second
    frame_rate.tick(45)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    draw()
    pygame.display.update()
