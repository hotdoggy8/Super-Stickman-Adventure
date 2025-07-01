import pygame
import time
Running = True
Process = 1

class CreatePlayer:
    def __init__(self, action, touchingpart, health, frame, color):
        self.action = action
        self.touchingpart = touchingpart
        self.health = health
        self.frame = frame
        self.color = color
    def setaction(self, action):
        self.action = action
        if action == "idle":
            self.frame = 1
        elif action == "walking":
            starttime = None
            isonact2 = False
            while action == "walking":
                if canrun == True:
                    starttime = pygame.time.get_ticks()
                canrun = False
                if (pygame.time.get_ticks() - starttime) == 250:
                    canrun = True
                if canrun:
                    if isonact2:
                        self.frame = 3
                        isonact2 = not isonact2
                    else:
                        self.frame = 2
                        isonact2 = not isonact2

# Basically loads the image of the player. That's it
def RenderPlayer(plrclass):
    ImagePath = None
    if plrclass.color == "yellow":
        if plrclass.frame == 1:
            #Idle-yellow
            ImagePath = "Images/Stickman_idle_yellow.png"
        elif plrclass.frame == 2:
            #Walking1-yellow
            ImagePath = "Images/Stickman_walking1_yellow.png"
        elif plrclass.frame == 3:
            #Walking2-yellow
            ImagePath = "Images/Stickman_walking2_yellow.png"
    elif plrclass.color == "red":
        if plrclass.frame == 1:
            #Idle-red
            ImagePath = "Images/Stickman_idle_red.png"
        elif plrclass.frame == 2:
            #Walking1-red
            ImagePath = "Images/Stickman_walking1_red.png"
        elif plrclass.frame == 3:
            #Walking2-red
            ImagePath = "Images/Stickman_walking2_red.png"
    elif plrclass.color == "green":
        if plrclass.frame == 1:
            #Idle-green
            ImagePath = "Images/Stickman_idle_green.png"
        elif plrclass.frame == 2:
            #Walking1-green
            ImagePath = "Images/Stickman_walking1_green.png"
        elif plrclass.frame == 3:
            #Walking2-green
            ImagePath = "Images/Stickman_walking2_green.png"
    elif plrclass.color == "blue":
        if plrclass.frame == 1:
            #Idle-blue
            ImagePath = "Images/Stickman_idle_blue.png"
        elif plrclass.frame == 2:
            #Walking1-blue
            ImagePath = "Images/Stickman_walking1_blue.png"
        elif plrclass.frame == 3:
            #Walking2-blue
            ImagePath = "Images/Stickman_walking2_blue.png"
    return pygame.image.load(ImagePath).convert()

window = pygame.display.set_mode((1200, 600))

while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    background = None
    if Process == 1:
        #Main menu
        raw_background = pygame.image.load("Images/MountainPlains.png")
        background = pygame.transform.scale(raw_background, (1200, 600)) #Made an mistake so have to resize
        StaticPlr = CreatePlayer("idle", None, 100, 1, "red")
        PlrImage = RenderPlayer(StaticPlr)
        pygame.Surface.set_colorkey(PlrImage, (255, 255, 255))
        window.blit(background, (0, 0))
        window.blit(PlrImage, (0, 0))
    pygame.display.update()