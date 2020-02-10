import  pygame
x=pygame.init()
gamewindow = pygame.display.set_mode((1000,600))
pygame.display.set_caption("My First Game")
ExitGame = False
GameOver = False
#GameLoop
while not ExitGame:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            ExitGame = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You have Pressed Right Key")
            if event.key == pygame.K_LEFT:
                print("You have pressed Left Arrow key ")

pygame.quit()
quit()