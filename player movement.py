import pygame
import random
from pygame.locals import *
from sys import exit
billy = 'playerPixelModel-Down.png'
pygame.init()

####Billy coords,directions and speed####
speed = 1
posx = 600
posy = 440
direction = "right"
head = "down"
gunCommand = ""

####Enemy coords and speed####
enemyX = 0
enemyXOtherSide = 1200
enemySpeed = 100

display = pygame.display.set_mode((1200,880), 0, 32)
###Billy movement sprites###
billyUp = pygame.image.load('playerPixelModel-Up.png')
billyRight = pygame.image.load('playerPixelModel-right.png')
billyLeft = pygame.image.load('playerPixelModel-left.png')
billyDown = pygame.image.load('playerPixelModel-Down.png')
###Gun sprites###
GunImg1LoadedL = pygame.image.load('playerPixelModel-GunLeft.png')
GunImg2LoadedL = pygame.image.load('playerPixelModel-GunLeft2.png')
GunImg3LoadedL = pygame.image.load('playerPixelModel-GunLeft3.png')
GunImg4LoadedL = pygame.image.load('playerPixelModel-GunLeft4.png')
GunImg5LoadedL = pygame.image.load('playerPixelModel-GunLeft5.png')

GunImg1LoadedR = pygame.image.load('playerPixelModel-GunRight.png')
GunImg2LoadedR = pygame.image.load('playerPixelModel-GunRight2.png')
GunImg3LoadedR = pygame.image.load('playerPixelModel-GunRight3.png')
GunImg4LoadedR = pygame.image.load('playerPixelModel-GunRight4.png')
GunImg5LoadedR = pygame.image.load('playerPixelModel-GunRight5.png')
###Enemy sprites###
zombieLoadedR = pygame.image.load('enemyPixelModel-right.png')
zombieLoadedL = pygame.image.load('enemyPixelModel-left.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pressedKeys = pygame.key.get_pressed()
##########Base skeleton og movement################
    if pressedKeys[K_a]:
        posx = posx - speed
        direction = "left"
    elif pressedKeys[K_d]:
        posx = posx + speed
        direction = "right"
    elif pressedKeys[K_w]:
        posy = posy - speed
        direction = "up"
    elif pressedKeys[K_s]:
        posy = posy + speed
        direction = "down"
    elif pressedKeys[K_q]:
        gunCommand = "shoot"
    elif pressedKeys[K_e]:
        speed = 1
        gunCommand = ""

    if posx > 1200:
        posx = 0
    elif posx < 0:
        posx = 1200
    if posy > 880:
        posy = 0
    elif posy < 0:
        posy = 880
#Player
##################Directions and sprite diretions###########################
    if direction == "up":
        head = pygame.transform.rotate(billyUp,0)
    if direction == "right":
        head = pygame.transform.rotate(billyRight,0)
    if direction == "left":
        head = pygame.transform.rotate(billyLeft,0)
    if direction == "down":
        head = pygame.transform.rotate(billyDown,0)
    #Shot the gun left
    if gunCommand == "shoot" and direction == "left":
        speed = 0.5
        randomlySelected = random.randint(1,5)
        if randomlySelected == 1:
            head = pygame.transform.rotate(GunImg1LoadedL,0)
        elif randomlySelected == 2:
            head = pygame.transform.rotate(GunImg2LoadedL,0)
        elif randomlySelected == 3:
            head = pygame.transform.rotate(GunImg3LoadedL,0)
        elif randomlySelected == 4:
            head = pygame.transform.rotate(GunImg4LoadedL,0)
        elif randomlySelected == 5:
            head = pygame.transform.rotate(GunImg5LoadedL,0)
    #Shot the gun right
    if gunCommand == "shoot" and direction == "right":
        speed = 0.5
        randomlySelected = random.randint(1,5)
        if randomlySelected == 1:
            head = pygame.transform.rotate(GunImg1LoadedR,0)
        elif randomlySelected == 2:
            head = pygame.transform.rotate(GunImg2LoadedR,0)
        elif randomlySelected == 3:
            head = pygame.transform.rotate(GunImg3LoadedR,0)
        elif randomlySelected == 4:
            head = pygame.transform.rotate(GunImg4LoadedR,0)
        elif randomlySelected == 5:
            head = pygame.transform.rotate(GunImg5LoadedR,0)
#################################
#Enemys
    enemyY = random.randint(1,880)

    enemyExistR = False
    enemyExistL = False

    randomSpawnEnemy = random.randint(1,2)
    if randomSpawnEnemy == 1:
        display.blit(zombieLoadedR,(enemyY,enemyXOtherSide))
        enemyExistR = True
    elif randomSpawnEnemy == 2:
        display.blit(zombieLoadedL,(enemyY,enemyX))
        enemyExistL = True


    if enemyExistR == True:
        enemyXOtherSide = enemyXOtherSide - enemySpeed
    if enemyExistL == True:
        enemyX = enemyX + enemySpeed

    if enemyX > 1200:
        enemyX = 0
    elif enemyXOtherSide < 0:
        enemyXOtherSide = 1200
    display.fill((255,255,255))
    display.blit(head, (posx,posy))
    pygame.display.update()
