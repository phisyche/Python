import pygame

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('x_racer')
clock = pygame.time.Clock()

soldierImg = pygame.image.load('Call-Of-Duty-HD-Wallpapers.jpg')

def soldier(x, y):
    gameDisplay.blit(soldierImg, (x,y))

x = (display_width * 0.55)
y = (display_height * 0.8)

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill(red)
    soldier(x,y)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
