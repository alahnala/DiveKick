import sys, pygame
pygame.init()

size = width, height = 1000, 1000
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

rick = pygame.image.load("rick.jpg")
rickrect = rick.get_rect()

morty = pygame.image.load("morty.bmp")
mortyrect = morty.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    rickrect = rickrect.move(speed)
    if rickrect.left < 0 or rickrect.right > width:
        speed[0] = -speed[0]
    if rickrect.top < 0 or rickrect.bottom > height:
        speed[1] = -speed[1]
    screen.fill(black)
    screen.blit(rick, rickrect)
    pygame.display.flip()