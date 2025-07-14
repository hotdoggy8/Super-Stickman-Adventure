#SUPER STICKMAN ADVENTURE
#Pre-alpha 1.0

#DESCRIPTION OF THIS VERION:
#This version is about testing the new 2D system i made. I'll try my best to add new stuff.

import pygame
import random

pygame.init()
Running = True
Process = 1
globalxshift = 38 #Notice: This shift the level back
forbiddenblocks = ["Spawn"]
approvedforvisibility = False
isonact2 = True
walkdelay = 0
PlayingMusic = False

#This helps waiting without universally stopping everything
#Also please clock this thing or else it won't work
class WaitModule:
    def __init__(self):
        self.tasks = []
    def WaitMS(self, sleep_time, callback):
        currenttick = pygame.time.get_ticks()
        self.tasks.append([currenttick + sleep_time, callback])
    def Update(self):
        currenttick = pygame.time.get_ticks()
        for index, timecapsule in enumerate(self.tasks):
            if timecapsule[0] <= currenttick:
                timecapsule[1]() #cursed eh? it calls the function when delay's done.
                self.tasks.pop(index)

WaitScheduler = WaitModule()

class CreatePlayer:
    def __init__(self, action, health, frame, color, PosX, PosY, touchingpart):
        self.action = action
        self.health = health
        self.frame = frame
        self.color = color
        self.PosX = PosX
        self.PosY = PosY
        self.touchingpart = touchingpart
    def updateanim(self):
        global isonact2
        global walkdelay
        if self.action == "walking":
            if walkdelay == 2:
                walkdelay = 0
                isonact2 = not isonact2
                if isonact2:
                    self.frame = 3
                else:
                    self.frame = 2
            else:
                walkdelay += 1
        elif self.action == "idle":
            self.frame = 1

# Basically loads the image of the sprites
def RenderSprite(sprclass, type):
    ImagePath = None
    if type == "player":
        if sprclass.color == "yellow":
            if sprclass.frame == 1:
                #Idle-yellow
                ImagePath = "Images/Stickman_idle_yellow.png"
            elif sprclass.frame == 2:
                #Walking1-yellow
                ImagePath = "Images/Stickman_walking1_yellow.png"
            elif sprclass.frame == 3:
                #Walking2-yellow
                ImagePath = "Images/Stickman_walking2_yellow.png"
        elif sprclass.color == "red":
            if sprclass.frame == 1:
                #Idle-red
                ImagePath = "Images/Stickman_idle_red.png"
            elif sprclass.frame == 2:
                #Walking1-red
                ImagePath = "Images/Stickman_walking1_red.png"
            elif sprclass.frame == 3:
                #Walking2-red
                ImagePath = "Images/Stickman_walking2_red.png"
        elif sprclass.color == "green":
            if sprclass.frame == 1:
                #Idle-green
                ImagePath = "Images/Stickman_idle_green.png"
            elif sprclass.frame == 2:
                #Walking1-green
                ImagePath = "Images/Stickman_walking1_green.png"
            elif sprclass.frame == 3:
                #Walking2-green
                ImagePath = "Images/Stickman_walking2_green.png"
        elif sprclass.color == "blue":
            if sprclass.frame == 1:
                #Idle-blue
                ImagePath = "Images/Stickman_idle_blue.png"
            elif sprclass.frame == 2:
                #Walking1-blue
                ImagePath = "Images/Stickman_walking1_blue.png"
            elif sprclass.frame == 3:
                #Walking2-blue
                ImagePath = "Images/Stickman_walking2_blue.png"
    return pygame.image.load(ImagePath).convert()

#Load a level into an array
def LoadLevel(filename, worldarray, forbiddenarray):
    with open(f"Worlds/{filename}.txt", "r") as level:
        for unstrippeddataline in level:
            if not unstrippeddataline == "":
                dataline = unstrippeddataline.strip()
                dataparts = dataline.split(";") #[0] = posX; [1] = posY; [2] = blockType
                global approvedforvisibility
                for fblock in forbiddenblocks:
                    if dataparts[2] != fblock:
                        approvedforvisibility = True
                    else:
                        approvedforvisibility = False
                if approvedforvisibility:
                    worldarray.append([pygame.image.load("Images/" + dataparts[2] + ".png"), int(float(dataparts[0])), int(float(dataparts[1]))])
                else:
                    forbiddenarray.append([dataparts[2], dataparts[0], dataparts[1], pygame.image.load("Images/" + dataparts[2] + ".png")])
window = pygame.display.set_mode((1200, 600))
titlecolor = random.choice(["red", "yellow", "green", "blue"])
globalfont = "TinyAndChunkyRegular.ttf"
clicking = False
mainplayer = None
blackrecty = -600.0
scheduledwaitevents = {}
Lives = 4
spawned = False
canleft = True
canright = True
titlelevelarray = []
titlelevelfbblocks = []
LoadLevel("title", titlelevelarray, titlelevelfbblocks)

pygame.display.set_caption("Super Stickman Adventure | Pre-alpha 1.0")

#NOTICE:
# *Each stickman has 20px left gap. And a 33px right gap. There was also an 23px top gap

while Running:
    pygame.time.Clock().tick(60.0) #The standard 60fps
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clicking = True
        elif event.type == pygame.MOUSEBUTTONUP:
            clicking = False
    background = None
    if Process == 0:
        #Undefined
        window.fill((0, 0, 0))
        text = pygame.font.Font(globalfont, 12).render("This process is not defined and will not work. The game has crashed.", False, (255, 255, 255))
        window.blit(text, (0, 0))
    elif Process == 1:
        #Main menu
        mouseX, mouseY = pygame.mouse.get_pos()
        raw_background = pygame.image.load("Images/MountainPlains.png")
        background = pygame.transform.scale(raw_background, (1200, 600))
        LogoImg = pygame.image.load("Images/Logo.png")
        titletext = pygame.font.Font(globalfont, 12).render("Pre-alpha 1.0", False, (255, 255, 255))
        startbtn = pygame.font.Font(globalfont, 20).render("Start", False, (255, 255, 255))
        startbtnhovered = pygame.font.Font(globalfont, 20).render("> Start", False, (255, 255, 255))
        window.blit(background, (0, 0))
        for renderdata in titlelevelarray:
            if (not (renderdata[1] - globalxshift < -38)) and (not (renderdata[1] - globalxshift > 1200)):
                window.blit(renderdata[0], (renderdata[1] - globalxshift, renderdata[2]))
        window.blit(LogoImg, (400, 40))
        window.blit(titletext, (400, 241))
        if mouseX < (600 + startbtn.get_width()/2) and mouseX > (600 - startbtn.get_width()/2) and mouseY > 350 and mouseY < (350 + startbtn.get_height()):
            window.blit(startbtnhovered, (600 - (startbtnhovered.get_width()/2) - 15, 350))
            if clicking == True:
                pygame.mixer.music.load("Audio/Coin.ogg")
                pygame.mixer.music.set_volume(0.25)
                pygame.mixer.music.play()
                Process = 2
        else:
            window.blit(startbtn, (600 - (startbtn.get_width()/2), 350))
    elif Process == 2:
        #Character select
        transistionspd = 11 #Pixels per frame
        transistiondone = False
        if globalxshift < 836:
            globalxshift += transistionspd
        else:
            transistiondone = True
        mouseX, mouseY = pygame.mouse.get_pos()
        raw_background = pygame.image.load("Images/MountainPlains.png")
        background = pygame.transform.scale(raw_background, (1200, 600))
        Reddata = CreatePlayer("idle", 100, 1, "red", 1245 - globalxshift - 20, 375, None)
        Yellowdata = CreatePlayer("idle", 100, 1, "yellow", 1345 - globalxshift - 20, 375, None) 
        Greendata = CreatePlayer("idle", 100, 1, "green", 1445 - globalxshift - 20, 375, None)
        Bluedata = CreatePlayer("idle", 100, 1, "blue", 1545 - globalxshift - 20, 375, None)
        Redsprite = RenderSprite(Reddata, "player")
        Yellowsprite = RenderSprite(Yellowdata, "player")
        Greensprite = RenderSprite(Greendata, "player")
        Bluesprite = RenderSprite(Bluedata, "player")
        pygame.Surface.set_colorkey(Redsprite, (255, 255, 255))
        pygame.Surface.set_colorkey(Yellowsprite, (255, 255, 255))
        pygame.Surface.set_colorkey(Greensprite, (255, 255, 255))
        pygame.Surface.set_colorkey(Bluesprite, (255, 255, 255))
        window.blit(background, (0, 0))
        for renderdata in titlelevelarray:
            if (not (renderdata[1] - globalxshift < -38)) and (not (renderdata[1] - globalxshift > 1200)):
                window.blit(renderdata[0], (renderdata[1] - globalxshift, renderdata[2]))
        window.blit(Redsprite, (Reddata.PosX, Reddata.PosY))
        window.blit(Yellowsprite, (Yellowdata.PosX, Yellowdata.PosY))
        window.blit(Greensprite, (Greendata.PosX, Greendata.PosY))
        window.blit(Bluesprite, (Bluedata.PosX, Bluedata.PosY))
        if transistiondone:
            charselecttxt = pygame.font.Font(globalfont, 20).render("Select a character!", False, (255, 255, 255))
            window.blit(charselecttxt, (600 - (charselecttxt.get_width()/2), 150))
            if mouseX > (1245 - globalxshift - 20 + 20) and mouseX < (1245  - globalxshift - 20 + Redsprite.get_width()) - 33 and mouseY > 375 + 23 and mouseY < 375 + Redsprite.get_height():
                SectRect = pygame.Rect(float(1245 - globalxshift), 375.0 + 23.0, 47.0, 77.0)
                pygame.draw.rect(window, (0, 0, 0), SectRect, 2)
                if clicking:
                    mainplayer = CreatePlayer("idle", 100, 1, "red", 0, 0, None)
                    pygame.mixer.music.load("Audio/Coin.ogg")
                    pygame.mixer.music.set_volume(0.25)
                    pygame.mixer.music.play()
                    Process = 3
            if mouseX > (1345 - globalxshift - 20 + 20) and mouseX < (1345  - globalxshift - 20 + Yellowsprite.get_width()) - 33 and mouseY > 375 + 23 and mouseY < 375 + Yellowsprite.get_height():
                SectRect = pygame.Rect(float(1345 - globalxshift), 375.0 + 23.0, 47.0, 77.0)
                pygame.draw.rect(window, (0, 0, 0), SectRect, 2)
                if clicking:
                    mainplayer = CreatePlayer("idle", 100, 1, "yellow", 0, 0, None)
                    pygame.mixer.music.load("Audio/Coin.ogg")
                    pygame.mixer.music.set_volume(0.25)
                    pygame.mixer.music.play()
                    Process = 3
            if mouseX > (1445 - globalxshift - 20 + 20) and mouseX < (1445  - globalxshift - 20 + Greensprite.get_width()) - 33 and mouseY > 375 + 23 and mouseY < 375 + Greensprite.get_height():
                SectRect = pygame.Rect(float(1445 - globalxshift), 375.0 + 23.0, 47.0, 77.0)
                pygame.draw.rect(window, (0, 0, 0), SectRect, 2)
                if clicking:
                    mainplayer = CreatePlayer("idle", 100, 1, "green", 0, 0, None)
                    pygame.mixer.music.load("Audio/Coin.ogg")
                    pygame.mixer.music.set_volume(0.25)
                    pygame.mixer.music.play()
                    Process = 3
            if mouseX > (1545 - globalxshift - 20 + 20) and mouseX < (1545  - globalxshift - 20 + Bluesprite.get_width()) - 33 and mouseY > 375 + 23 and mouseY < 375 + Bluesprite.get_height():
                SectRect = pygame.Rect(float(1545 - globalxshift), 375.0 + 23.0, 47.0, 77.0)
                pygame.draw.rect(window, (0, 0, 0), SectRect, 2)
                if clicking:
                    mainplayer = CreatePlayer("idle", 100, 1, "blue", 0, 0, None)
                    pygame.mixer.music.load("Audio/Coin.ogg")
                    pygame.mixer.music.set_volume(0.25)
                    pygame.mixer.music.play()
                    Process = 3
            if PlayingMusic == False:
                pygame.mixer.music.load("Audio/CharacterSelect.ogg")
                pygame.mixer.music.set_volume(0.25)
                pygame.mixer.music.play(-1)
                PlayingMusic = True
    elif Process == 3:
        #Transistion into game
        PlayingMusic = False
        blackrecty += 5.0
        BlackRect = pygame.Rect(0.0, blackrecty, 1200.0, 600.0)
        pygame.draw.rect(window, (0, 0, 0), BlackRect)
        if blackrecty == 0.0:
            Process = 4
    elif Process == 4:
        #Live count
        window.fill((0, 0, 0))
        Dummy = RenderSprite(mainplayer, "player")
        pygame.Surface.set_colorkey(Dummy, (255, 255, 255))
        livescount = pygame.font.Font(globalfont, 20).render("x " + str(Lives), False, (255, 255, 255))
        window.blit(Dummy, (480, 200))
        window.blit(livescount, (580, 240))
        def joingame():
            global Process
            scheduledwaitevents.pop("livecountwait")
            Process = 5
        if scheduledwaitevents.get("livecountwait") == None:
            WaitScheduler.WaitMS(3000, joingame)
            scheduledwaitevents["livecountwait"] = True
    elif Process == 5:
        #Test course
        raw_background = pygame.image.load("Images/MountainPlains.png")
        background = pygame.transform.scale(raw_background, (1200, 600))
        playersprite = RenderSprite(mainplayer, "player")
        pygame.Surface.set_colorkey(playersprite, (255, 255, 255))
        if not spawned:
            spawned = True
            for fblock in titlelevelfbblocks:
                if fblock[0] == "Spawn":
                    print(int(float(fblock[2])))
                    print(fblock[3].get_height())
                    mainplayer.PosX = int(float(fblock[1]))
                    mainplayer.PosY = int(float(fblock[2])) + fblock[3].get_height() - playersprite.get_height()
        for blockdata in titlelevelarray:
            if mainplayer.PosX - 20 + globalxshift + 38 >= blockdata[1] and mainplayer.PosX - 20 + globalxshift + 38 <= blockdata[1] + blockdata[0].get_width() and mainplayer.PosY + playersprite.get_height() >= blockdata[2]:
                touchingblk = pygame.Rect(blockdata[1], blockdata[2], 38.0, 38.0)
                pygame.draw.rect(window, (0, 0, 0), touchingblk, 2)
                mainplayer.touchingpart = blockdata
                break
            else:
                mainplayer.touchingpart = None
        if mainplayer.touchingpart == None:
            print(mainplayer.touchingpart)
            mainplayer.PosY += 1
        Keys = pygame.key.get_pressed()
        walkspd = 6
        if Keys[pygame.K_a]:
            mainplayer.action = "walking"
            playersprite = pygame.transform.flip(playersprite, True, False) #Flips left
            if mainplayer.PosX > -20:
                mainplayer.PosX -= walkspd
        if Keys[pygame.K_d]:
            mainplayer.action = "walking"
            playersprite = pygame.transform.flip(playersprite, False, False) #Flips right
            if mainplayer.PosX < 600:
                mainplayer.PosX += walkspd
            else:
                globalxshift += walkspd
        if Keys[pygame.K_SPACE]:
            print("jump")
        if not Keys[pygame.K_a] and not Keys[pygame.K_d] and not Keys[pygame.K_SPACE]:
            mainplayer.action = "idle"
        window.blit(background, (0, 0))
        for renderdata in titlelevelarray:
            if (not (renderdata[1] - globalxshift < -38)) and (not (renderdata[1] - globalxshift > 1200)):
                window.blit(renderdata[0], (renderdata[1] - globalxshift, renderdata[2]))
        window.blit(playersprite, (mainplayer.PosX, mainplayer.PosY))
        mainplayer.updateanim()
    WaitScheduler.Update()
    pygame.display.update()

pygame.quit()
