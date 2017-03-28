import pygame
import random
pygame.init()


WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BlACK = (0,0,0)
BLUE = (0,0,255)


size=(700,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("animaiton")

snow_list = []
for i in range(50):
    x = random.randrange(0,400)
    y = random.randrange(0,400)
    snow_list.append([x,y])

done = False
clock = pygame.time.Clock()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)

    for i in snow_list:
        pygame.draw.circle(screen,BlACK,i,2)
        i[1]+=1
        if(i[1]>400):
            i[1]=random.randrange(-50,-10)
            i[0]=random.randrange(0,400)


    pygame.display.flip()
    clock.tick(100)


pygame.quit()
