
#создай игру "Лабиринт"!
from random import randint
from pygame import*
from time import time as timer
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Space")
background = transform.scale(image.load("galaxy.jpg"), (win_width, win_height))

mixer.init()
mixer.music.load('dbaff.mp3')
mixer.music.play()
mixer.music.set_volume(0.1)
fire_sound = mixer. Sound("fire.ogg")
fire_sound.set_volume(0.01)

font.init()
font2 = font.SysFont("Arial", 35)
font1 = font.SysFont("Arial", 80)

win = font1.render("YOU WIN", True, (0,255,0))
lose = font1.render("YOU LOSE", True, (255,0,0))



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
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x-= self.speed 
        if keys[K_RIGHT] and self.rect.x < 640:
            self.rect.x += self.speed 
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y-= self.speed
        if keys[K_DOWN] and self.rect.y < 440:
            self.rect.y += self.speed  
    def fire(self):
        bullet = Bullet('good.png', self.rect.centerx, self.rect.top, 15, 20, 15)
        bullets.add(bullet)



class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_height -80)
            self.rect.y = 0
            lost = lost + 1

class Bullet(GameSprite):
    def update(self):
       self.rect.y -= self.speed 
       if self.rect.y <0:
           self.kill()



ship = Player("rocket.png", 5, win_height -100, 10, 80, 100)
monsters = sprite.Group()
asteroids = sprite.Group()
bullets = sprite.Group()
for i in range(5):
    monster = Enemy("ufo.png", randint(80, win_height -80), -40, randint(1,5), 80,50)
    monsters.add(monster)

for i in range(3):
    asteroid = Enemy("ast.png", randint(80, win_height -80), -40, randint(1,5), 80,50)
    asteroids.add(asteroid)

lost = 0
score = 0






game = True
finish = False

num_fire = 0
rel_time = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                if num_fire < 5 and rel_time == False:
                    fire_sound.play()
                    ship.fire()
                    num_fire += 1
                if num_fire >=5 and rel_time == False:
                    rel_time = True
                    last_time = timer()


    if not finish:
        window.blit(background, (0,0))
        text = font2.render(f"Kills:{score}", True, (255, 255, 255))
        window.blit(text,(10,20))
        text_lose = font2.render(f"Missed: {lost}", True, (255,255,255))
        window.blit(text_lose, (10,50))


    
        ship.reset()  
        ship.update()
        monsters.draw(window)
        monsters.update()
        asteroids.draw(window)
        asteroids.update()
        bullets.draw(window)
        bullets.update()

        if rel_time:
            new_time = timer()
            if new_time - last_time < 3:
                reload = font2.render("wait, reload", True, (100,100,100))
                window.blit(reload, (250,450))
            else:
                num_fire = 0
                rel_time = False


        colides = sprite.groupcollide(monsters, bullets, True, True)
        for i in colides:
            score += 1 
            monster = Enemy("ufo.png", randint(80, win_height -80), -40, randint(1,5), 80,50)
            monsters.add(monster)
        if score == 10:
            finish = True
            window.blit(win, (200, 200))

        if sprite.spritecollide(ship, asteroids, True):
            finish = True
            window.blit(lose, (200, 200))  

        if sprite.spritecollide(ship, monsters, True):
            finish = True
            window.blit(lose, (200, 200)) 
    else:
        finish = False
        score = 0
        lost = 0

        num_fire = 0
        rel_time = False
        for m in monsters:
            m.kill()
        for b in bullets:
            b.kill()

        time.delay(3000)
        for i in range(5):
            monster = Enemy("good.png", randint(80, win_height -80), -40, randint(1,5), 80,50)
            monsters.add(monster)



    display.update()
    time.delay(20)
