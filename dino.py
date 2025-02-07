import pygame
from random import randint, choice
import pickle

pygame.init()

WIDTH, HEIGHT = 1000, 400
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


def scoresSave():  # сохраняем очки
    global scoresBest

    if scores > scoresBest:
        f = open('scores.dat', 'wb')
        pickle.dump(scores, f)
        f.close()
        scoresBest = scores


def scoresLoad():
    global scoresBest
    try:
        f = open('scores.dat', 'wb')
        scoresBest = pickle.load(f)
        f.close()
    except:
        pass


imgSprites = pygame.image.load('sprites.png').convert_alpha()
imgBG = imgSprites.subsurface(2, 104, 2400, 26)
imgDinoStand = [imgSprites.subsurface(1514, 2, 88, 94),
                imgSprites.subsurface(1602, 2, 88, 94)]
imgDinoSit = [imgSprites.subsurface(1866, 36, 118, 60),
              imgSprites.subsurface(1984, 36, 118, 60)]
imgDinoLose = [imgSprites.subsurface(1690, 2, 88, 94)]
imgCactus = [imgSprites.subsurface(446, 2, 34, 70),
             imgSprites.subsurface(480, 2, 68, 70),
             imgSprites.subsurface(512, 2, 102, 70),
             imgSprites.subsurface(512, 2, 68, 70),
             imgSprites.subsurface(652, 2, 50, 100),
             imgSprites.subsurface(752, 2, 98, 100),
             imgSprites.subsurface(850, 2, 102, 100), ]
imgPter = [imgSprites.subsurface(260, 0, 92, 82),
           imgSprites.subsurface(352, 0, 92, 82)]
imgRestart = imgSprites.subsurface(2, 2, 72, 64)

sndJump = pygame.mixer.Sound('jump.wav')
sndLevelup = pygame.mixer.Sound('levelup.wav')
sndGameOver = pygame.mixer.Sound('gameover.wav')

fontScores = pygame.font.Font(None, 30)

py, sy, = 380, 0
isStand = False
speed = 10
frame = 0
scores = 0
scoresBest = 0
uruven = 0
night = 0

bgs = [pygame.Rect(0, HEIGHT - 50, 2400, 26)]
objects = []
timer = 0


class Obj:
    def __init__(self):
        objects.append(self)

        if randint(0, 4) == 0 and scores > 500:
            self.image = imgPter
            self.speed = 3
            py = HEIGHT - 30 - randint(0, 2) * 50
        else:
            self.image = [choice(imgCactus)]
            self.speed = 0
            py = HEIGHT - 20

        self.rect = self.image[0].get_rect(bottomleft=(WIDTH, py))
        self.frame = 0

    def update(self):
        global speed, timer, sy
        self.rect.x -= speed + self.speed
        self.frame = (self.frame + 0.1) % len(self.image)

        if self.rect.colliderect(dinoRect) and speed != 0:
            speed = 0
            timer = 60
            sy = -10
            sndGameOver.play()

        if self.rect.right < 0: objects.remove(self)

    def draw(self):
        window.blit(self.image[int(self.frame)], self.rect)


scoresLoad()

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    keys = pygame.key.get_pressed()
    b1, b2, b3 = pygame.mouse.get_pressed()
    pressJump = keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP] or b1
    pressSit = keys[pygame.K_LCTRL] or keys[pygame.K_s] or keys[pygame.K_DOWN] or b3

    if (pressJump or pressSit) and speed == 0 and timer == 0:  # кнопка
        scoresSave()
        py, sy, = 380, 0
        isStand = False
        speed = 10  # значения на ноль
        frame = 0
        scores = 0
        objects = []

    if pressJump and isStand and speed > 0:
        sy = -22
        sndJump.play()
    if isStand: frame = (frame + speed / 35) % 2

    py += sy
    sy = (sy + 1) * 0.97

    isStand = False
    if py > HEIGHT - 20:
        py, sy, isStand = HEIGHT - 20, 0, True

    if speed == 0:
        dinoImage = imgDinoLose[0]
    elif pressSit:
        dinoImage = imgDinoSit[int(frame)]
    else:
        dinoImage = imgDinoStand[int(frame)]

    dw, dh = dinoImage.get_width(), dinoImage.get_height()
    dinoRect = pygame.Rect(150, py - dh, dw, dh)

    for i in range(len(bgs) - 1, -1, -1):
        bg = bgs[i]
        bg.x -= speed

        bg.right < 0 and bgs.pop(i)

    if bgs[-1].right < WIDTH:
        bgs.append(pygame.Rect(bgs[-1].right, HEIGHT - 50, 2400, 26))

    for obj in objects: obj.update()

    if timer > 0:
        timer -= 1
    elif speed > 0:
        timer = randint(100, 150)
        Obj()

    scores += speed / 50

    if scores // 100 > uruven:  # вычисление
        uruven = scores // 100
        sndLevelup.play()

    if speed > 0:
        speed = 10 + scores // 100

    night = (night + 0.02) % 512

    d = abs(night - 256)
    window.fill((d, d, d))
    for bg in bgs: window.blit(imgBG, bg)
    for obj in objects: obj.draw()
    window.blit(dinoImage, dinoRect)

    text = fontScores.render('Scores:' + str(int(scores)), 1, 'gray40')
    window.blit(text, (WIDTH - 150, 10))

    text = fontScores.render('Record:' + str(int(scoresBest)), 1, 'orange')
    window.blit(text, (50, 10))

    if speed == 0 and timer == 0:
        rect = imgRestart.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        window.blit(imgRestart, rect)

    pygame.display.update()
    clock.tick(FPS)
scoresSave()
pygame.quit()
