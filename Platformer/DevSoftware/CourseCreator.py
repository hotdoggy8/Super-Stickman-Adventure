import pygame
import threading

window = pygame.display.set_mode((1200, 600))
Running = True
World = 1
Block = "None"
Block_List = {
    1:["Spawn", "Grass_block", "Dirt_block"]
}
Block_ingame = []
globalxshift = 0

pygame.display.set_caption("coursecreator.py")

#stole from chatgpt :laughing_face:
def round_to_nearest(x, base):
    return round(x / base) * base

def cmdprogram():
    global Block
    global Block_List
    global World
    while Running:
        command = input("cmd:>>")
        if command == "changeblock":
            world = int(input("World? [INT] >> "))
            if world == 1:
                block = input("Block? [STR] >> ")
                if block.lower() == "none":
                    Block = "None"
                elif block.lower() == "grass_block":
                    Block = Block_List[world][1]
                elif block.lower() == "dirt_block":
                    Block = Block_List[world][2]
                elif block.lower() == "spawn":
                    Block = Block_List[world][0]
                else:
                    print("Error: No valid blocks found")
            else:
                print("Error: No valid world found")
        elif command == "save":
            name = input("File Name? (If doesn't exist, creates new file) [STR] >> ")
            with open("Worlds/" + name + ".txt", "w") as file:
                for blockdata in Block_ingame:
                    file.write(str(blockdata[1])+";"+str(blockdata[2])+";"+str(blockdata[3])+"\n")
            print("File export success")
        else:
            print("Error: No such command found")

threading.Thread(target=cmdprogram, daemon=True).start()

while Running:
    window.fill((102, 204, 255))
    pygame.font.init()
    mouseX, mouseY = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        globalxshift -= 38
    elif keys[pygame.K_RIGHT]:
        globalxshift += 38
    boxposX, boxposY = float(round_to_nearest(mouseX, 38) - 38/2), float(round_to_nearest(mouseY, 38) - 38/2)
    box = pygame.rect.Rect(boxposX, boxposY, 38.0, 38.0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if Block == "Spawn":
                    Block_ingame.append([pygame.image.load("Images/Spawn.png"), (boxposX - globalxshift), boxposY, "Spawn"])
                elif Block == "Grass_block":
                    Block_ingame.append([pygame.image.load("Images/Grass_block.png"), (boxposX - globalxshift), boxposY, "Grass_block"])
                elif Block == "Dirt_block":
                    Block_ingame.append([pygame.image.load("Images/Dirt_block.png"), (boxposX - globalxshift), boxposY, "Dirt_block"])
    pygame.draw.rect(window, (0, 0, 0), box, 1)
    for blockdata in Block_ingame:
        window.blit(blockdata[0], (blockdata[1] + globalxshift, blockdata[2]))
    pygame.display.update()