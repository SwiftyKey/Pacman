import pygame

size = (800, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pacman")

fps = 60
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    clock.tick(fps)
