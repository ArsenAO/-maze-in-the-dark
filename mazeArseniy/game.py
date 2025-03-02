import pygame
import time
import math
pygame.init()
w = pygame.display.set_mode((1000,665), pygame.FULLSCREEN)
w_win, h_win = w.get_size()
fon = pygame.image.load('image/fon.jpg') 
fon = pygame.transform.scale(fon,(w_win,h_win))
cl = pygame.time.Clock()
osnova= True
game = False
menu =True
gameOver =False
win = False
sound = pygame.mixer.Sound("sound/sond.mp3")
myfont = pygame.font.Font("font/Pshek_KY2.ttf", 100)
lose_txt = myfont.render("YOU LOSE!", True, (139, 0, 0))
win_txt = myfont.render("YOU WIN!!!", True, (0,255,0))
timetxt = myfont.render("0", True, (0,0,0) )
pygame.display.update()
sound.play(-1)
class HitBox():
    def __init__(self, images, x,y,width,height):
        self.rect = pygame.Rect(x,y,width,height)
        try:
            self.image= pygame.image.load(images)
            self.image = pygame.transform.scale(self.image,(self.rect.width,self.rect.height))
        except:
            self.image = images
    def paint(self):
        w.blit(self.image,(self.rect.x,self.rect.y))
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image, speed, x, y, w, h):
        #super.__init__()
        self.image = pygame.transform.scale(pygame.image.load(image), (w,h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def paint(self):
        w.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
class Monster(GameSprite):
    def __init__(self, image, speed, x, y, w, h, direction):
        super().__init__(image, speed, x, y, w, h)
        self.direction = direction
    def update(self):
        if self.direction == "left":
            self.rect.x -= self.speed
        if self.direction == "right":
            self.rect.x += self.speed
        if self.direction == "up":
            self.rect.y -= self.speed
        if self.direction == "down":
            self.rect.y += self.speed
        if self.rect.x >= 1000:
            self.direction = "left"
        if self.rect.x <= 0:
            self.direction = "right"
        if self.rect.y >= 665:
            self.direction = "up"
        if self.rect.y <= 0:
            self.direction = "down"
class Wall(pygame.sprite.Sprite):
    def __init__(self, color_1,color_2,color_3, x, y, w,h):
        super().__init__()
        self.width = w
        self.height = h
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((color_1,color_2,color_3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw_wall(self):
        w.blit(self.image, (self.rect.x, self.rect.y))
class WallKey(Wall):
    def __init__(self, color_1,color_2,color_3, x, y, w,h, xkey,ykey):
        super().__init__(color_1,color_2,color_3,x,y,w,h)
        self.keysW = 45
        self.keysH = 45
        self.imagesKey = pygame.transform.scale(pygame.image.load("image/keys.png"), (self.keysW, self.keysH))
        self.rectKey = self.imagesKey.get_rect()
        self.rectKey.x = xkey
        self.rectKey.y = ykey
        self.podnit = False
        self.otkrit = False
    def draw_wall(self):
        if self.otkrit == False:
            w.blit(self.image, (self.rect.x, self.rect.y))
        if self.podnit == False:
            w.blit(self.imagesKey, (self.rectKey.x, self.rectKey.y))
gg = Player("image/Player.webp", 10, 10, 320, 20,50)
hp = 1
skarb = GameSprite("image/scarb.png", 10, 900, 600, 50,50)
enemy1 = Monster("image/enemy.jpg", 10, 600, 332, 50, 20, "left")
enemy2 = Monster("image/enemy.jpg", 10, 200, 332, 50, 20, "up")
enemysM = []
enemysM.append(enemy1) 
enemysM.append(enemy2) 
a = 0
b = 0
tma = []
while 1:
    
    temniyKvadrat = Wall(0,0,0, a*52, b*52, 52,52)
    tma.append(temniyKvadrat)
    a +=1
    if a > 19:
        b += 1
        a = 0
    if b == 15:
        break
stena1 = Wall(255, 0,0, 150, 0, 25, 200 )
stena2 = Wall(255, 0,0, 150, 275, 25, 400 )
stena3 = Wall(255, 0,0, 175, 175, 300, 25)
stena4 = Wall(255, 0,0, 175, 275, 100, 25)
stena5 = Wall(255, 0,0, 330, 275, 300, 25)
stena6 = Wall(255, 0,0, 450, 75, 25, 100)
stena7 = Wall(255, 0,0, 350, 0, 25, 100)
stena8 = Wall(255, 0,0, 250, 75, 25, 100)
stena9 = Wall(255, 0,0, 575, 175, 300, 25)
stena10 = Wall(255, 0,0, 575, 0, 25, 200 )
stena11 = Wall(255, 0,0, 450, 300, 25, 125)
stena12 = Wall(255, 0,0, 450, 525, 25, 150)
stena13 = Wall(255, 0,0, 750, 200, 25, 225)
stena14 = Wall(255, 0,0, 475, 400, 275, 25)
stena15 = Wall(255, 0,0, 450, 525, 25, 150)
steniM = []
steniM.append(stena1)
steniM.append(stena2)
steniM.append(stena3)
steniM.append(stena4)
steniM.append(stena5)
steniM.append(stena6)
steniM.append(stena7)
steniM.append(stena8)
steniM.append(stena9)
steniM.append(stena10)
steniM.append(stena11)
steniM.append(stena12)
steniM.append(stena13)
steniM.append(stena14)
steniM.append(stena15)
stenaKeyM = []
stenKey1 = WallKey(0, 255,0, 450, 525, 25, 150, 10, 200)
stenKey2 = WallKey(0, 255,0, 450, 525, 25, 150, 10, 200)
stenaKeyM.append(stenKey1)
stenaKeyM.append(stenKey2)
reset = GameSprite("image/reset.jpg", 0, 380, 180, 220, 220)
xmos = -1
ymos = -1
startB = HitBox('image/startB.png', 325,182,350, 240)
timer = 0
hitTim = 0
tmaRast = 0
admin = False
while osnova:
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu =False
            if event.type == pygame.MOUSEBUTTONDOWN:
                xmos,ymos = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if startB.rect.collidepoint(xmos,ymos):
                    game = True
                    menu = False
                    xmos = 0
                    ymos = 0
                    timer1 = time.time()
            
        w.blit(fon,(0,0))
        startB.paint()
        pygame.display.update()
        cl.tick(40)
    while game:
        if not win and not gameOver:
            timer2 = time.time()
        hitTim -=1
        timer = timer2-timer1
        w.blit(fon,(0,0))
        gg.paint()
        if not gameOver and not win:
            gg.update()
        for enemy in enemysM:
            if not gameOver and not win:
                enemy.update()
            enemy.paint()
        if gg.rect.y >= 665:
            gg.rect.y -= 10
        if gg.rect.y <= 0:
            gg.rect.y += 10
        if gg.rect.x <=0:
            gg.rect.x +=10
        if gg.rect.x >= 1000:
            gg.rect.x -=10
        for stenka in steniM:
            if gg.rect.colliderect(stenka):
                if (gg.rect.bottom > stenka.rect.top and gg.rect.top < stenka.rect.top):
                    gg.rect.y -= 10
                elif (gg.rect.top < stenka.rect.bottom and gg.rect.bottom > stenka.rect.bottom):
                    gg.rect.y += 10
                elif (gg.rect.right > stenka.rect.left and gg.rect.left < stenka.rect.left):
                    gg.rect.x -=10
                elif (gg.rect.left < stenka.rect.right and gg.rect.right > stenka.rect.right):
                    gg.rect.x +=10
            for enemy in enemysM:
                if enemy.rect.colliderect(stenka):
                    if enemy.rect.bottom > stenka.rect.top and enemy.rect.top < stenka.rect.top:
                        enemy.direction = "up"
                    elif enemy.rect.top < stenka.rect.bottom and enemy.rect.bottom > stenka.rect.bottom:
                        enemy.direction = "down"
                    elif enemy.rect.right > stenka.rect.left and enemy.rect.left < stenka.rect.left:
                        enemy.direction = "left"
                    elif enemy.rect.left < stenka.rect.right and enemy.rect.right > stenka.rect.right:
                        enemy.direction = "right"
                if gg.rect.colliderect(enemy) and hitTim <= 0 and hp:
                    hp -=1
                    hitTim = 60
                elif gg.rect.colliderect(skarb):
                    win = True
            stenka.draw_wall()
        for keySten in stenaKeyM:
            if gg.rect.colliderect(keySten.rectKey):
                keySten.podnit = True
            if gg.rect.colliderect(keySten.rect):
                if keySten.podnit:
                    keySten.otkrit = True
                else:
                    if enemy.rect.bottom > stenka.rect.top and enemy.rect.top < stenka.rect.top:
                        enemy.direction = "up"
                    elif enemy.rect.top < stenka.rect.bottom and enemy.rect.bottom > stenka.rect.bottom:
                        enemy.direction = "down"
                    elif enemy.rect.right > stenka.rect.left and enemy.rect.left < stenka.rect.left:
                        enemy.direction = "left"
                    elif enemy.rect.left < stenka.rect.right and enemy.rect.right > stenka.rect.right:
                        enemy.direction = "right"
            keySten.draw_wall()

        for teni in tma:
            if admin == True:
                tmaRast =0
            else:
                tmaRast = math.sqrt((((teni.rect.x + 52) - (gg.rect.x + 10))) ** 2 +  ((teni.rect.y + 52) - (gg.rect.y + 25)) ** 2)
            if (tmaRast<= 54) and (tmaRast >= -54):
                teni.image.set_alpha(0)
            elif (tmaRast > 54 and tmaRast <= 102) or (tmaRast < -54 and tmaRast >= -102):
                teni.image.set_alpha(50)
            elif (tmaRast > 102 and tmaRast <= 156) or (tmaRast < -102 and tmaRast >= -156):
                teni.image.set_alpha(150)
            elif (tmaRast > 156) or (tmaRast < -156):
                teni.image.set_alpha(255)
            teni.draw_wall()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                xmos,ymos = event.pos
        if reset.rect.collidepoint(xmos,ymos) and (gameOver or win):
            gg.rect.x = 10
            gg.rect.y = 320
            xmos = 0
            ymos = 0
            gameOver = False
            win = False
            timer1= time.time()
            print(str(win) + str(gameOver))
        if hp == 0:
            gameOver = True
        if not win:
            skarb.paint()
        if gameOver:
            w.blit(lose_txt,(320,400))
            reset.paint()
        if win:
            w.blit(win_txt,(320,400))
            reset.paint()
        timetxt = myfont.render(str(int(timer)), True, (0,0,0) )
        w.blit(timetxt,(10,10))
        pygame.display.flip()
        pygame.display.update()
        cl.tick(40)
    if game == False and menu == False:
        osnova = False