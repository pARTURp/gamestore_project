from random import randint
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h):
        super().__init__()
        self.image = transform.scale(image.load(img), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move(self):
        mouse_x, mouse_y = mouse.get_pos() 
        player.rect.centerx = mouse_x 

    def fire(self):
        bullet = Bullet(img='bullet.png', x=self.rect.x, y=self.rect.y, w=500, h=200)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y += randint(1, 5)
        if self.rect.y > 500:
            self.rect.x = randint(0, 600)
            self.rect.y = 0
            lost += 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= 10

player = Player(img='player.png', x=300, y=400, w=100, h=100)

bullets = sprite.Group()
enemys = sprite.Group()
for i in range(5):
    rand_x = randint(0, 600)
    enemy = Enemy(img='enemy.jpg', x=rand_x, y=0, w=100, h=50)
    enemys.add(enemy)

window = display.set_mode( (700,500) )
display.set_caption('Шутер')

clock = time.Clock()

background =  transform.scale(image.load('background.jpg'), (700,500))

lost = 0
score = 0
font.init()
my_font = font.Font(None, 40)

finish = False

while True:
    for some_event in event.get():
        if some_event.type == QUIT:
            exit()
        elif some_event.type == MOUSEBUTTONDOWN:
            player.fire()

    if not finish:
        window.blit( background, (0, 0) )

        score_text = my_font.render(f'Очки: {score}', 0, (255,255,255))
        window.blit(score_text, (20, 20))

        lost_text = my_font.render(f'Пропущено: {lost}', 0, (255,255,255))
        window.blit(lost_text, (20, 60))

        player.show()
        player.move()

        enemys.draw(window)
        enemys.update()

        bullets.draw(window)
        bullets.update()

        if sprite.groupcollide(bullets, enemys, True, True):
           for i in range(2):
                rand_x = randint(0, 600)
                enemy = Enemy(img='enemy.jpg', x=rand_x, y=0, w=100, h=50)
                enemys.add(enemy)
                score += 1

        if sprite.spritecollide(player, enemys, True) and lost > 10:
            finish = True

        if score > 20:
            finish = True

    display.update()
    clock.tick(100)