import pygame
pygame.init()

SCREEN = (1900, 1000)

screen = pygame.display.set_mode(SCREEN)
screen.fill((200, 200, 200))

timer = pygame.time.Clock()

kartinochka = pygame.image.load('Screenshot(201).png') # load дапамагае захаваць фатаграфіі з кампутар

kitty = pygame.transform.scale(kartinochka, (kartinochka.get_width() * 1, kartinochka.get_height() * 1)) # scale змяненне памераў

screen.blit(kitty, (0, 0))

while True:
    pygame.display.update()
    timer.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # QUIT - выхад // Калі была націснута клавішу крыжык, то зрабіць наступнае
            pygame.quit() # Выйсці з-за pygame
            quit() # Выйсці цалкам з-за праграммы