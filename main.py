import random,pygame,math

pygame.init()
resolution = (500,500)
screen = pygame.display.set_mode(resolution)

i = 0
n = 0
screen.fill([25,25,25])
while True:
    i += 1
    x = random.random()
    y = random.random()
    if x**2+y**2 < 1:
        n += 1
        screen.set_at((int(x*resolution[0]),int(y*resolution[0])), [0,255,0])
    else:
        screen.set_at((int(x*resolution[0]),int(y*resolution[0])), [255,0,0])
    if i/1000 == int(i/1000):
        print("Pi = "+str(4*n/i))
        pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
