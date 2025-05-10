import pygame
import os

pygame.init()

window = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()

running = True
task = "devenginebgmove"
mainx = 0
clonex = 1200

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if task == "devenginebgmove":
        plainmountsbg = pygame.image.load(os.path.join("assets\images", "plainmounts.png")).convert()
        plainmountsclone = pygame.image.load(os.path.join("assets\images", "plainmounts.png")).convert()
        window.blit(plainmountsbg, (mainx, 0))
        window.blit(plainmountsclone, (clonex, 0))
    pygame.display.update()
    clock.tick(60)
    mainx -= 1
    clonex -= 1
    if mainx == -1200:
        mainx = 0
        clonex = 1200