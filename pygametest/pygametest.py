import pygame
import random

pygame.init()

SCREEN_WIDTH = 1920

SCREEN_HEIGHT = 1080

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player_width = 20
player_height = 150

#player2 modes: Human, NPC, HardNPC
player2_mode = "NPC"
player1points = 0
player2points = 0
paddlespeed = 2

ballstartspeed = 2
ballspeed = ballstartspeed
ball_dim = 20
ball_dir = [-ballspeed, ballspeed]
ballx = ball_dir[random.randint(0,1)]
bally = ball_dir[random.randint(0,1)]
ball_color = (255,255,255)




player = pygame.Rect(50, 465, player_width, player_height)
player2 = pygame.Rect(1845, 465, player_width, player_height)
ball = pygame.Rect(950, 530, ball_dim, ball_dim)

text_font = pygame.font.Font("bit5x3.ttf", 60)

def draw_text(text, font, text_col, x, y):
    img = font.render(text,True, text_col)
    screen.blit(img, (x,y))
def follow_ball():
    if ball.y > player2.y + (player_height/2):
            if player2.y < SCREEN_HEIGHT - player_height:
                player2.move_ip(0,paddlespeed)
    if ball.y < player2.y + (player_height/2):
            if 0 < player2.y:
                player2.move_ip(0,-paddlespeed)

 

run = True

while run:
    
    screen.fill((0,0,0))

    #DRAW TEXT
    draw_text(f"{player2points}", text_font,(255,255,255), 960, 150)
    draw_text(f"{player1points}", text_font,(255,255,255), 860, 150)

    #DRAW PADDLES
    pygame.draw.rect(screen,(255,255,255), player)
    pygame.draw.rect(screen,(255,255,255), player2)

    #DRAW BALL
    pygame.draw.rect(screen,ball_color, ball)

    #MOVEMENT
    key = pygame.key.get_pressed()

    #BALL MOVEMENT
    ball_dir = [-ballspeed, ballspeed]
    ball.move_ip(ballx, bally)



    #WALL BOUNCE
    if 0 > ball.y or ball.y > SCREEN_HEIGHT - ball_dim:
        ball_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        pygame.mixer.music.load('bump.mp3')
        pygame.mixer.music.play(0)
        bally = -bally
    #POINTS
    if 0 > ball.x or ball.x > SCREEN_WIDTH - ball_dim:
        if 0>ball.x:
            player2points +=1
        elif ball.x > SCREEN_WIDTH - ball_dim:
            player1points +=1
        pygame.mixer.music.load('413629__djlprojects__video-game-sfx-positive-action-long-tail.mp3')
        pygame.mixer.music.play(0)
        ballspeed = ballstartspeed
        ball.x = 950
        ball.y = 530
        ballx = ball_dir[random.randint(0,1)]
        bally = ball_dir[random.randint(0,1)]
        ball.move_ip(ballx, bally)
    
    #BALL/PADDLE COLLISIONS

    if ball.colliderect(player):
        ball_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        pygame.mixer.music.load('bump.mp3')
        pygame.mixer.music.play(0)
        ballx = -ballx

        if ball.x < player.x + (player_width - ballspeed-1):
            bally = -bally


    if ball.colliderect(player2):
        ball_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        pygame.mixer.music.load('bump.mp3')
        pygame.mixer.music.play(0)
        ballx = -ballx

        if ball.x > player2.x + ballspeed:
            bally = -bally


    #PLAYER1 MOVEMENT
    if key[pygame.K_w] == True:
        if 0 < player.y:
            player.move_ip(0,-paddlespeed)
    if key[pygame.K_s] == True:
        if player.y < SCREEN_HEIGHT - player_height:
            player.move_ip(0,paddlespeed)
    #PLAYER2 MOVEMENT
    if player2_mode == "Human":
        if key[pygame.K_UP] == True:
            if 0 < player2.y:
                player2.move_ip(0,-paddlespeed)
        if key[pygame.K_DOWN] == True:
            if player2.y < SCREEN_HEIGHT - player_height:
                player2.move_ip(0,paddlespeed)
    #AI MOVEMENT
    elif player2_mode == "NPC":
        if ball.x > ((2*SCREEN_WIDTH)/3) and ballx > 0:
         follow_ball()
    elif player2_mode == "HardNPC":
        player2.y = ball.y - (player_height/2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()
pygame.quit()