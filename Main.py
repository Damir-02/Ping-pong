
#создай игру "Лабиринт"!
from random import randint
from pygame import*
from time import time as timer
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))





class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, player_speed,w,h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))  
    

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y-= self.speed
        if keys[K_DOWN] and self.rect.y < 440:
            self.rect.y += self.speed  
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y-= self.speed
        if keys[K_s] and self.rect.y < 440:
            self.rect.y += self.speed  



back = (200,255,255) 
win_width = 600
win_hight = 500
window = display.set_mode((win_width, win_hight))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

racket1 = Player("ld.png", 30,300,5,60,140)
racket2 = Player("ld.png", 499,300,5,60,140)
ball = GameSprite("1.png", 200, 200, 4, 150, 60)


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        racket1.reset()
        racket2.reset()
        ball.update()
        ball.reset()










    display.update()
    time.delay(20)