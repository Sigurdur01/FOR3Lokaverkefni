#Sigurður Ingi Brynjarsson
import pygame
import random
import pygame.freetype

pygame.init()

###Billy movement sprites###
billyLeft = pygame.image.load('playerPixelModel-left.png')

###Gun sprites###
GunImg1LoadedL = pygame.image.load('playerPixelModel-GunLeft.png')
GunImg2LoadedL = pygame.image.load('playerPixelModel-GunLeft2.png')
GunImg3LoadedL = pygame.image.load('playerPixelModel-GunLeft3.png')
GunImg4LoadedL = pygame.image.load('playerPixelModel-GunLeft4.png')
GunImg5LoadedL = pygame.image.load('playerPixelModel-GunLeft5.png')
###Enemy sprites###
zombieLoadedR = pygame.image.load('enemyPixelModel-right.png')
zombieLoadedL = pygame.image.load('enemyPixelModel-left.png')

height = 1000
width = 1800

mostUsedFont = pygame.freetype.Font('28 Days Later.ttf',30)

pressedKey = pygame.key.get_pressed()
display = pygame.display.set_mode((width,height))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = billyLeft
        self.rect = self.image.get_rect()
        self.rect.centerx = width/2
        self.rect.bottom = height/2
        self.speedx = 0
        self.speedy = 0

    def update(self):
        pressedKey = pygame.key.get_pressed()
        self.speedx = 0
        self.speedy = 0
        ###Controls aka looks for pressed buttons if they are pressed they will move the sprite that many pixles forwards or backwards###
        if pressedKey[pygame.K_a]:
            self.speedx = -1
        if pressedKey[pygame.K_d]:
            self.speedx = 1
        if pressedKey[pygame.K_w]:
            self.speedy = -1
        if pressedKey[pygame.K_s]:
            self.speedy = 1
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        #Width border to stop leaving the map
        if self.rect.x > width:
            self.rect.x = width - 25
        if self.rect.x == 0:
            self.rect.x = self.rect.x + 25
        #Height border to stop leaving the map
        if self.rect.y > height:
            self.rect.y = height -50
        if self.rect.y == 0:
            self.rect.y = self.rect.y + 50

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = zombieLoadedL
        self.rect = self.image.get_rect()
        self.speedx = 1
        self.rect.y = random.randrange(25,875)

    def update(self):
        self.rect.x += self.speedx
        print("Labba")
        if self.rect.left > width +1:
            print("Labba")
            self.speedx = 1
            self.rect.x = random.randrange(25,width)

class Gun():

all_sprites = pygame.sprite.Group()
player = Player()
zombie = Mob()
all_sprites.add(player)

mobs = pygame.sprite.Group()
for i in range(4):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

Go = True
while Go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Go = False

    all_sprites.update()
    mobs.update()
    display.fill((255,255,255))
    all_sprites.draw(display)
    #if pressedKey[pygame.K_ESCAPE]:
       # mainMenu()
    pygame.display.flip()

pygame.quit()


#def mainMenu():
    #resume = mostUsedFont.render('Resume',False,(255,255,255))
    #highscoreDisplay = mostUsedFont.render('Highscore',False,(255,255,255))

    #runMainMenu = True
    #escapeButtonOrResume = True
    #while runMainMenu:
    #    display.fill((0,0,0))
    #    display.blit(resume,(width/2,700))
    #    display.blit(highscoreDisplay,(width/2,400))
    #    if pressedKey[pygame.K_ESCAPE]:
    #        escapeButtonOrResume = False
    #    if escapeButtonOrResume == False:
    #        runMainMenu = False
