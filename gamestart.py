import pygame
import sys
import os




'''
Objects
'''

class Player(pygame.sprite.Sprite):
    #spawns a player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        #just using one pic for now, could make it have moves with other pics
        img = pygame.image.load("rick.jpg")
        # lmao this is not work but it's supposed to make rick's background transparent
        img.convert_alpha()  # optimise alpha
        img.set_colorkey(ALPHA)  # set alpha
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        #sprite movement
        self.movex = 0
        self.movey = 0
        self.frame = 0

    def control(self, x, y):
        '''
        control player movement
        '''
        self.movex += x
        self.movey += y

    def update(self):
        '''Update sprite position'''
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

        # moving up
        if self.movey != 0:
            self.frame += 1
            if self.frame > 3 * animationCycles:
                self.frame = 0

        # # falling down
        # if self.movey > 0:
        #     self.frame += 1
        #     if self.frame > 3 * animationCycles:
        #         self.frame = 0

    def apply_gravity(self):
        if self.rect.y < startHeight:
            self.movey += 10



'''
Setup
'''

#window size
worldx = 960
worldy = 720

#set frame rate, start its internal clock, and start
frameRate = 40
animationCycles = 4
clock = pygame.time.Clock()
pygame.init()

#setting up the background, this version for using stage.png
world = pygame.display.set_mode([worldx, worldy])
backdrop = pygame.image.load(os.path.join('images', 'stage.png')).convert()
backdropbox = world.get_rect()

#lmao this is not work but it's supposed to make rick's background transparent
ALPHA = (152, 179, 239)

#spawn player
player = Player()
player.rect.x = 960 - player.rect.width
player.rect.y = startHeight = 720 - player.rect.height
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 30



'''
alternatively, using just a color
world = pygame.display.set_mode([worldx,worldy])
BLUE  = (25,25,200)
BLACK = (23,23,23 )
WHITE = (254,254,254)
'''

'''
Main
'''

main = True
jump = False

while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                sys.exit()
                main = False
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0, -steps)

        if event.type == pygame.KEYUP:
            print("key up")
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                jump = True


                #TODO: figure out why falling is inconsistent :(
                # start = 720 - player.rect.height
                # distance = 0
                # while player.rect.y < startHeight:
                #     player.control(0, steps)
                #     distance += 10
                #     world.blit(backdrop, backdropbox)
                #     player.update()
                #     player_list.draw(world)
                #     pygame.display.flip()
                #     clock.tick(frameRate)
                # distance = -distance+10
                # player.control(0, distance)


    world.blit(backdrop, backdropbox)
    player.apply_gravity()
    player.update()
    player_list.draw(world)
    pygame.display.flip()
    clock.tick(frameRate)