#Sigurður Ingi Brynjarsson
import pygame
import random
import pygame.freetype

pygame.init()
pygame.font.init()

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
###Bullet sprite###
bulletLoaded = pygame.image.load('bulletPixelModel.png')

height = 1000
width = 1600

pressedKey = pygame.key.get_pressed()
display = pygame.display.set_mode((width,height))

fontName = pygame.font.match_font('arial')
def text(sur,text,size,x,y):
    font = pygame.font.Font(fontName, size)
    surface = font.render(text, False,(0,0,0))
    textRect = surface.get_rect()
    textRect.midtop = (x,y)
    sur.blit(surface, textRect)

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

    def fire(self):
        bullet = Gun(self.rect.centerx,self.rect.top)
        sprites.add(bullet)
        bullets.add(bullet)
        randomlySelected = random.randint(1,5)
        if randomlySelected == 1:
            self.image = GunImg1LoadedL
        elif randomlySelected == 2:
            self.image = GunImg2LoadedL
        elif randomlySelected == 3:
            self.image = GunImg3LoadedL
        elif randomlySelected == 4:
            self.image = GunImg4LoadedL
        elif randomlySelected == 5:
            self.image = GunImg5LoadedL
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = zombieLoadedL
        self.rect = self.image.get_rect()
        self.speedx = 1
        self.rect.y = random.randrange(0,height)

    def update(self):
        self.rect.x += self.speedx
        if self.rect.left > width:
            self.rect.x = random.randrange(0,width)
            self.speedx = 1

class Gun(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bulletLoaded
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedx = -3
    def update(self):
        self.rect.x += self.speedx
        if self.rect.bottom < 0:
            self.kill()

class Menu:
    def __init__(self):
        self.image = pygame.Surface((height,width))
sprites = pygame.sprite.Group()
player = Player()
sprites.add(player)

bullets = pygame.sprite.Group()

zombie = Mob()
mobs = pygame.sprite.Group()
for i in range(10):
    m = Mob()
    sprites.add(m)
    mobs.add(m)

score = 0
Go = True
while Go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Go = False
        if event.type == pygame.MOUSEBUTTONUP:
            player.fire()
        if pressedKey[pygame.K_ESCAPE]:
            Menu()
    collisions = pygame.sprite.spritecollide(player,mobs,False)
    if collisions:
        Go = False
    collisions = pygame.sprite.groupcollide(mobs,bullets,True,True)
    for collision in collisions:
        score = +1
        m = Mob()
        sprites.add(m)
        mobs.add(m)


    sprites.update()
    mobs.update()
    display.fill((255,255,255))
    sprites.draw(display)
    text(display,str(score),18,width/2,10)
    pygame.display.flip()

pygame.quit()
