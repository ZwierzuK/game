#python3
#ZZ22 - Top Lobster game - become top lobster
# w tej wszystko juz jest ustawione ale przed uzyciem pygame_functions
import pygame, sys, random
from pygame.locals import *
#from pygame_functions import *


#frames per second
FPS = 30
#window
WINDOWWIDTH = 1000
WINDOWHEIGHT = 700
HALFWINDOWWIDTH = int(WINDOWWIDTH/2)
HALFWINDOWHEIGHT = int(WINDOWHEIGHT/2)
# COLORS    R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)
BLACK    = (  0,   0,   0)
pause = False


def main():
    global FPSCLOCK, DISPLAY, pause
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        DISPLAY.fill(WHITE)
        text_display('freesansbold.ttf', 100, 'dfd', RED, 500, 200)
        button("start The game", 100, 600, 600, 20, NAVYBLUE, BLUE,game_loop)
        pygame.display.update()
        FPSCLOCK.tick(15)

def game_loop():
    global pause
    #barge info
    x = (WINDOWWIDTH * 0.49)
    y = (WINDOWHEIGHT * 0.8)
    x_change = 0
    bargeImage = pygame.image.load('barge.png')
    bargeImageLeft = pygame.transform.rotate(bargeImage, 30)
    bargeImageRight = pygame.transform.rotate(bargeImage, -30)
    bargesizeX = 50
    bargesizeY = 100
    #obstacle
    speed = 5
    pathX = random.randrange(95,905)
    pathY = -200
    sizeX  = 10
    sizeY = 10
    #text
    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    textSurfaceObj = fontObj.render('Top Lobster', True, RED)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (HALFWINDOWWIDTH, HALFWINDOWHEIGHT)

    #sound
    pygame.mixer.music.load('songClasic.mp3')
    pygame.mixer.music.play(-1, 0.0) # for playing in backroud this vairables
    #to play in define time first import time next time.sleep(1) for example play for 1 secon

    pygame.display.set_caption('TOP LOBSTER')#game title in window


    while True: #MAIN GAME LOOP

        x += x_change
        pathY += speed

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -5
                elif event.key == pygame.K_RIGHT:
                        x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0


        DISPLAY.fill(WHITE) #shows main background
        DISPLAY.blit(textSurfaceObj, textRectObj) #shows text
        obstacle(pathX,pathY)
#move of the barge
        if x_change == 0:
            DISPLAY.blit(bargeImage,(x,y))
        if x_change == -5:
            DISPLAY.blit(bargeImageLeft,(x,y))
        if x_change == 5:
            DISPLAY.blit(bargeImageRight,(x,y))

#collision with edge
        if x < 100 or x > 900:
            collision()
        if  x > 905:
            pygame.quit()
        if  x < 95:
            pygame.quit()
#powrot obstacle po zniknieciu u dolu
        if pathY > WINDOWHEIGHT:
            pathY = 0 - 200
            pathX = random.randrange(95,905)
#kolizja z obstacle
        if y < pathY+sizeY:
            print('y crossover')

            if x > pathX and x < pathX + sizeY or x+bargesizeX > pathX and x + bargesizeX < pathX+sizeX:
                print('x crossover')
                collision()

        obstacle(pathX,pathY)
        button("koty", 100, 100, 100, 20, NAVYBLUE, BLUE, im)
        text_display('freesansbold.ttf', 100, 'dfd', RED, 23, 40)
        #pokazuje eventy
        #print(event)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def unpause():
    global pause
    pause = False
    pygame.mixer.music.unpause()

def paused():

    while pause:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        DISPLAY.fill(WHITE)
        pygame.mixer.music.pause()
        text_display('freesansbold.ttf', 300, 'Paused', RED, 100, 40)
        button("Continue", 400, 400, 100, 20, NAVYBLUE, BLUE,unpause)
        button("Quit", 600, 600, 100, 20, NAVYBLUE, BLUE,quit)
        pygame.display.update()
        FPSCLOCK.tick(15)



def collision():
    text_display('freesansbold.ttf', 100, 'crashed', RED, 100, 40)

def obstacle(pathX,pathY):
    obImg = pygame.image.load('lobster.png')
    DISPLAY.blit(obImg, (pathX, pathY))
    '''
def obstacle():
    obImg = pygame.image.load('lobster.png')
    ob1Img = pygame.image.load('grass2.png')
    ob2Img = pygame.image.load('bottom4.png')
    listImg = [obImg, ob1Img, ob2Img]
    x = random.randrange(95,905)
    y = 200
    speed = 5
    y += speed
    obstacleImg = random.choice(listImg)
    DISPLAY.blit(obstacleImg, (x, y))
    '''
def button(text,x,y,width,height,inactivecolor,activecolor,action=None):
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(DISPLAY,activecolor,(x,y,width,height))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(DISPLAY,inactivecolor,(x,y,width,height))
    fontObj = pygame.font.Font("freesansbold.ttf",20)
    textSurfaceObj = fontObj.render(text, True, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = ( (x+(width/2)), (y+(height/2)) )
    DISPLAY.blit(textSurfaceObj,textRectObj)

def text_display(font, size, text, color, x, y):
    fontObj = pygame.font.Font(font, size)
    textSurfaceObj = fontObj.render(text, True, color)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (x, y)
    DISPLAY.blit(textSurfaceObj,textRectObj)

def im(): #how to show image
    shellImg = pygame.image.load('lobster.png') #data for blit in main loop
    shellx = 500
    shelly = 200
    DISPLAY.blit(shellImg, (shellx, shelly)) #shows image of shell




if __name__ == '__main__':
    main()
