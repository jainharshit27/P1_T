import pygame

pygame.init()
clock=pygame.time.Clock()

screen = pygame.display.set_mode((600,300))

b1 = pygame.Rect(100,100,50,50)
w1 = pygame.Rect(100,150,50,50)

b2 = pygame.Rect(150,150,50,50)
w2 = pygame.Rect(150,100,50,50)


while True:    
    screen.fill((150,75,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.draw.rect(screen,(0,0,0),b1)
    pygame.draw.rect(screen,(255,255,255),w1)
    
    pygame.draw.rect(screen,(0,0,0),b2)
    pygame.draw.rect(screen,(255,255,255),w2)
    
    pygame.display.update()