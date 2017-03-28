#coding:utf-8
import pygame

pygame.init()

size = (255,255)
screen = pygame.display.set_mode(size)

#棋盘棋子方格大小
block_width = 20
block_height = 20
margin = 5

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

#初始化一个棋盘 10*10
grid = [[0 for x in range(10)] for y in range(10)]

done = False

clock = pygame.time.Clock()
while not done :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #在鼠标点击的地方绘制绿色
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (block_width+margin)
            row = pos[1] // (block_height+margin)
            grid[row][column] = 1
            print("click",pos,"grid coordinate:",row,column)

    screen.fill(BLACK)
    #绘制棋盘
    for row in range(10):
        for column in range(10):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,color,[(margin+block_width)*column+margin,
            (margin+block_height)*row+margin,block_width,block_height])


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
