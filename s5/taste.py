import sys, pygame
pygame.init()

size = width, height = 1080, 720
speed = [2, 2]
DX, DY = 0.1, 0.1
black = 0, 0, 0
screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()
x, y = width/2, height/2
w, h = ballrect.w/2, ballrect.h/2

pygame.time.set_timer(pygame.USEREVENT, 100)
pull = None

while 1:
    event = pygame.event.wait()
    if event.type == pygame.QUIT: sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN or pull and event.type == pygame.MOUSEMOVE:
        pull = event.pos

    if x-w/2<0 or x+w/2 > width:    
        speed[0] = -speed[0]
    if y-h < 0 or y+h > height:
        speed[1] = -speed[1]

    screen.fill(black)
    x += speed[0]
    y += speed[1]
    print (x, y)
    ballrect.move_ip(int(x*DX), int(y*DY))
    screen.blit(ball, ballrect)
    pygame.display.flip()

