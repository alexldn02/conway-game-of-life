import pygame

pygame.init()

display = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Conway's Game of Life")

clock = pygame.time.Clock()

colours = [(255,0,0),(255,128,0),(255,255,0),(0,255,0),(0,255,255),(0,128,255),(0,0,255,),(128,0,255),(255,0,128)]

alive = []
alive_neighbours = []
for y in range(100):
    alive.append([])
    alive_neighbours.append([])
    for x in range(100):
        alive[y].append(False)
        alive_neighbours[y].append(0)

clicking = False

paused = False

running = True
while running:     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            clicking = True
        if event.type == pygame.MOUSEBUTTONUP:
            clicking = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                paused = False
            if event.key == pygame.K_r:
                alive = []
                alive_neighbours = []
                for y in range(200):
                    alive.append([])
                    alive_neighbours.append([])
                    for x in range(200):
                        alive[y].append(False)
                        alive_neighbours[y].append(0)

    if not paused:
        for y in range(100):
            for x in range(100):
                alive_neighbours[y][x] = 0
                for x2, y2 in ((x-1,y+1), (x,y+1), (x+1,y+1), (x-1,y), (x+1,y), (x-1,y-1), (x,y-1), (x+1,y-1)):
                    if alive[y2%100][x2%100]:
                        alive_neighbours[y][x] += 1

        for y in range(100):
            for x in range(100):
                if alive[y][x]:
                    if alive_neighbours[y][x] < 2 or alive_neighbours[y][x] > 3:
                        alive[y][x] = False
                    
                    pygame.draw.rect(display, colours[alive_neighbours[y][x]], (x*10, y*10, 10, 10))
                else:
                    if alive_neighbours[y][x] == 3:
                        alive[y][x] = True
                    pygame.draw.rect(display, (0, 0, 0), (x*10, y*10, 10, 10))

    if clicking:
        mx, my = pygame.mouse.get_pos()
        y = my // 10
        x = mx // 10
        alive[y][x] = True
        alive_neighbours[y][x] = 0
        for x2, y2 in ((x-1,y+1), (x,y+1), (x+1,y+1), (x-1,y), (x+1,y), (x-1,y-1), (x,y-1), (x+1,y-1)):
            if alive[y2%100][x2%100]:
                alive_neighbours[y][x] += 1
        pygame.draw.rect(display, colours[alive_neighbours[y][x]], (x*10, y*10, 10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()