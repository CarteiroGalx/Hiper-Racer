import pygame.sprite
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

# CONFIGURAÇÕES DO JOGO
pygame.mixer_music.set_volume(0.7)
pygame.mixer.music.load("songs/soundtrack.mp3")
pygame.mixer.music.play(-1)
som_batida = pygame.mixer.Sound("songs/hit.mp3")
som_morte = pygame.mixer.Sound("songs/gameover.mp3")
som_moedaG = pygame.mixer.Sound("songs/coinsongG.mp3")
som_moedaR = pygame.mixer.Sound("songs/coinsongR.mp3")
tocando_morte = False

tela_largura = 300
tela_altura = 650
tela = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption('Hiper Racer')
FPS = pygame.time.Clock()

py_background = tela_altura/2
py_background2 = -325
background = pygame.image.load("imgs/Background.png")
background2 = pygame.image.load("imgs/Background2.png")
tela_gameover = pygame.image.load("imgs/gameover.png")
background_rect = pygame.Rect(150, py_background, tela_largura, tela_altura)
py_background_y = background_rect.top - (tela_altura//2.0)
background_rect2 = pygame.Rect(150, py_background2, tela_largura, tela_altura)
py_background2_y = background_rect2.top - (tela_altura//2.0)
velocidade = 3


leftposition = 40
middleposition = 150
rightposition = 260

# PLAYER
player_img = pygame.image.load("imgs/CarPlayer.png")
player_img = pygame.transform.scale(player_img, (40, 60))
px = 150
py = tela_altura - 75
player = pygame.Rect(px, py, 40, 60)
lifes = 5
pontos = 0

# CIRCULO VERDE
gcircle_img = pygame.image.load("imgs/GreenCircle.png")
pygame.display.set_icon(gcircle_img)
gcircle_img = pygame.transform.scale(gcircle_img, (30, 30))
px_gcircle = leftposition
py_gcircle = randint(-1500, -50)
gcricle = pygame.Rect(px_gcircle, py_gcircle, 30, 30)
ganhos_vel = 1

# CIRCULO VERMELHO
rcircle_img = pygame.image.load("imgs/RedCircle.png")
rcircle_img = pygame.transform.scale(rcircle_img, (30, 30))
px_rcircle = middleposition
py_rcircle = randint(-1500, -50)
rcricle = pygame.Rect(px_gcircle, py_gcircle, 30, 30)

# OBSTÁCULO 1
square_img = pygame.image.load("imgs/Carro1.png")
square_img = pygame.transform.scale(square_img, (40, 60))
px_square = leftposition
py_square = randint(-1500, -50)
square = pygame.Rect(px_square, py_square, 40, 60)

# OBSTÁCULO 2
square_img2 = pygame.image.load("imgs/Carro2.png")
square_img2 = pygame.transform.scale(square_img2, (40, 60))
px_square2 = middleposition
py_square2 = randint(-1500, -50)
square2 = pygame.Rect(px_square2, py_square2, 40, 60)

# OBSTÁCULO 3
square_img3 = pygame.image.load("imgs/Carro3.png")
square_img3 = pygame.transform.scale(square_img3, (40, 60))
px_square3 = rightposition
py_square3 = randint(-1500, -50)
square3 = pygame.Rect(px_square2, py_square2, 40, 60)

fonte = pygame.font.SysFont('Arial', 35, True, False)
fonte_msg_reset = pygame.font.SysFont('Arial', 24, True, False)
fonte_veloc = pygame.font.SysFont('Arial', 20, True, True)
fonte_pontos = pygame.font.SysFont('Arial', 20, True, False)
velocidade_locker = False


def reset_game():
    global pontos, px_square, px_square2, px_square3, px_gcircle, px_rcircle
    global py_square, py_square2, py_square3, py_gcircle, py_rcircle

    py_gcircle = randint(-1500, -50)
    px_gcircle = randint(1, 3)
    if px_gcircle == 1:
        px_gcircle = leftposition
    elif px_gcircle == 2:
        px_gcircle = middleposition
    elif px_gcircle == 3:
        px_gcircle = rightposition

    py_rcircle = randint(-1500, -50)
    px_rcircle = randint(1, 3)
    if px_rcircle == 1:
        px_rcircle = leftposition
    elif px_rcircle == 2:
        px_rcircle = middleposition
    elif px_rcircle == 3:
        px_rcircle = rightposition

    py_square = randint(-1500, -50)
    px_square = randint(1, 3)
    if px_square == 1:
        px_square = leftposition
    elif px_square == 2:
        px_square = middleposition
    elif px_square == 3:
        px_square = rightposition

    py_square2 = randint(-1500, -50)
    px_square2 = randint(1, 3)
    if px_square2 == 1:
        px_square2 = leftposition
    elif px_square2 == 2:
        px_square2 = middleposition
    elif px_square2 == 3:
        px_square2 = rightposition

    py_square3 = randint(-1500, -50)
    px_square3 = randint(1, 3)
    if px_square3 == 1:
        px_square3 = leftposition
    elif px_square3 == 2:
        px_square3 = middleposition
    elif px_square3 == 3:
        px_square3 = rightposition


def gameover():
    global tocando_morte, velocidade_locker, lifes, pontos
    teclas = pygame.key.get_pressed()
    velocidade_locker = True
    tela.blit(tela_gameover, (0, 0))
    tela.blit(texto_gameover1, (65, 50))
    tela.blit(texto_gameover2, (75, tela_altura - 100))
    tela.blit(texto_gameover3, (9, tela_altura - 50))
    pygame.mixer_music.set_volume(0)
    if tocando_morte is False:
        som_morte.play()
        tocando_morte = True
    if teclas[pygame.K_r]:
        pygame.mixer_music.set_volume(0.7)
        tocando_morte = False
        velocidade_locker = False
        lifes = 5
        pontos = 0
        reset_game()


def update_posicions():
    global py_gcircle, py_rcircle, py_square, py_square2, py_square3, velocidade
    py_gcircle += velocidade
    py_rcircle += velocidade
    py_square += velocidade
    py_square2 += velocidade
    py_square3 += velocidade


def position_checker():
    global py_gcircle, py_rcircle, py_square, py_square2, py_square3, px_gcircle, px_rcircle, px_square, px_square2, px_square3
    if py_gcircle >= 700:
        py_gcircle = randint(-1500, -50)
        px_gcircle = randint(1, 3)
        if px_gcircle == 1:
            px_gcircle = leftposition
        elif px_gcircle == 2:
            px_gcircle = middleposition
        elif px_gcircle == 3:
            px_gcircle = rightposition

    if py_rcircle >= 700:
        py_rcircle = randint(-1500, -50)
        px_rcircle = randint(1, 3)
        if px_rcircle == 1:
            px_rcircle = leftposition
        elif px_rcircle == 2:
            px_rcircle = middleposition
        elif px_rcircle == 3:
            px_rcircle = rightposition

    if py_square >= 700:
        py_square = randint(-1500, -50)
        px_square = randint(1, 3)
        if px_square == 1:
            px_square = leftposition
        elif px_square == 2:
            px_square = middleposition
        elif px_square == 3:
            px_square = rightposition

    if py_square2 >= 700:
        py_square2 = randint(-1500, -50)
        px_square2 = randint(1, 3)
        if px_square2 == 1:
            px_square2 = leftposition
        elif px_square2 == 2:
            px_square2 = middleposition
        elif px_square2 == 3:
            px_square2 = rightposition

    if py_square3 >= 700:
        py_square3 = randint(-1500, -50)
        px_square3 = randint(1, 3)
        if px_square3 == 1:
            px_square3 = leftposition
        elif px_square3 == 2:
            px_square3 = middleposition
        elif px_square3 == 3:
            px_square3 = rightposition


while True:
    FPS.tick(60)
    tela.fill((64, 64, 64))
    tela.blit(background, background_rect)
    tela.blit(background2, background_rect2)
    tela.blit(gcircle_img, gcricle)
    tela.blit(rcircle_img, rcricle)
    tela.blit(square_img, square)
    tela.blit(square_img2, square2)
    tela.blit(square_img3, square3)
    texto = fonte.render(f"Pontos: %.0f" % pontos, True, (255, 255, 255))
    texto_veloc = fonte_veloc.render(f"Velocidade: %.2f" % velocidade, True, pygame.Color('#ffffff'))
    texto_vidas = fonte_veloc.render(f"Vidas: {lifes}", True, (255, 255, 255))
    tela.blit(texto_vidas, (110, 620))
    tela.blit(texto_veloc, (10, 40))
    tela.blit(texto, (10, 10))
    tela.blit(player_img, player)

    texto_gameover1 = fonte.render("Você bateu!", True, (255, 255, 255))
    texto_gameover2 = fonte_pontos.render(f"Pontos totais: %.0f" % pontos, True, (255, 255, 255))
    texto_gameover3 = fonte_msg_reset.render("Aperte R para recomeçar", True, (255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_d and px != 255:
                px += 105

            elif event.key == K_a and px != 45:
                px -= 105

    keys_aceleration = pygame.key.get_pressed()

    if keys_aceleration[pygame.K_s] and tocando_morte is not True:
        if velocidade > 2:
            velocidade -= 0.1
    elif velocidade_locker is True:
        velocidade = 0

    if keys_aceleration[pygame.K_w] and tocando_morte is not True:
        if velocidade <= 20:
            velocidade += 0.1
    elif velocidade_locker is True:
        velocidade = 0

    if player.colliderect(square) and lifes >= 1:
        py_square = randint(-1500, -50)
        px_square = randint(1, 3)
        som_batida.play()
        lifes = lifes - 1
        if px_square == 1:
            px_square = leftposition
        elif px_square == 2:
            px_square = middleposition
        elif px_square == 3:
            px_square = rightposition
    elif lifes <= 0:
        gameover()

    if player.colliderect(square2) and lifes >= 1:
        py_square2 = randint(-1500, -50)
        px_square2 = randint(1, 3)
        som_batida.play()
        lifes = lifes - 1
        if px_square2 == 1:
            px_square2 = leftposition
        elif px_square2 == 2:
            px_square2 = middleposition
        elif px_square2 == 3:
            px_square2 = rightposition
    elif lifes <= 0:
        gameover()

    if player.colliderect(square3) and lifes >= 1:
        py_square3 = randint(-1500, -50)
        px_square3 = randint(1, 3)
        som_batida.play()
        lifes = lifes - 1
        if px_square3 == 1:
            px_square3 = leftposition
        elif px_square3 == 2:
            px_square3 = middleposition
        elif px_square3 == 3:
            px_square3 = rightposition
    elif lifes <= 0:
        gameover()

    if player.colliderect(gcricle):
        pontos += ganhos_vel * velocidade
        som_moedaR.play()
        py_gcircle = randint(-1500, -50)
        px_gcircle = randint(1, 3)
        if px_gcircle == 1:
            px_gcircle = leftposition
        elif px_gcircle == 2:
            px_gcircle = middleposition
        elif px_gcircle == 3:
            px_gcircle = rightposition

    if player.colliderect(rcricle):
        if pontos > 0:
            pontos -= ganhos_vel * velocidade
            som_moedaG.play()
        py_rcircle = randint(-1500, -50)
        px_rcircle = randint(1, 3)
        if px_rcircle == 1:
            px_rcircle = leftposition
        elif px_rcircle == 2:
            px_rcircle = middleposition
        elif px_rcircle == 3:
            px_rcircle = rightposition

    player.center = (px, py)
    rcricle.center = (px_rcircle, py_rcircle)
    gcricle.center = (px_gcircle, py_gcircle)
    square.center = (px_square, py_square)
    square2.center = (px_square2, py_square2)
    square3.center = (px_square3, py_square3)
    background_rect.center = (150, py_background)
    background_rect2.center = (150, py_background2)

    update_posicions()
    position_checker()
    py_background += velocidade
    py_background2 += velocidade

    if background_rect.top >= tela_altura:
        py_background = -325

    if background_rect2.top >= tela_altura:
        py_background2 = -325

    pygame.display.flip()
