from pygame import *


WIN_WIDTH = 700
WIN_HEIGHT = 500
FPS = 40
bg = (250, 200, 147)
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >= 5:
            self.rect.y -= self.speed
        elif keys[K_s] and self.rect.y <= WIN_HEIGHT - 155:
            self.rect.y += self.speed
    
class Player2(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >= 5:
            self.rect.y -= self.speed
        elif keys[K_DOWN] and self.rect.y <= WIN_HEIGHT - 155:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, speed_x, speed_y):
        super().__init__(player_image, player_x, player_y, size_x, size_y,speed_x)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.y >= WIN_HEIGHT-50:
            self.speed_y *= -1

        if self.rect.y <= 0:
            self.speed_y *= -1

    def collide_rect(self, player):
        if self.rect.colliderect(player):
            self.speed_x *= -1

window = display.set_mode((WIN_WIDTH, WIN_HEIGHT))
display.set_caption('PingPong')

clock = time.Clock()


player1 = Player1('racket.png', 50, WIN_HEIGHT - 280, 50, 150, 4)

player2 = Player2('racket.png', WIN_WIDTH - 100, WIN_HEIGHT - 280, 50, 150, 4)

ball = Ball('tenis_ball.png', 325, WIN_HEIGHT - 280, 50, 50, 7, 7)

game = True
finish = False

font.init()
font_win = font.SysFont('Arial', 70)
win_r = font_win.render('Выйграл 2 игрок!', True, (0, 0, 255))
win_l = font_win.render('Выйграл 1 игрок!', True, (255, 0, 0))
winner = None

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.fill(bg)

        player1.reset()
        player1.update_l()
        player2.reset()
        player2.update_r()
        ball.reset()
        ball.update()
        ball.collide_rect(player1)
        ball.collide_rect(player2)

        if ball.rect.x < 0:
            winner = win_r
            finish = True
        
        if ball.rect.x > WIN_WIDTH - 50:
            winner = win_l
            finish = True

        

    elif finish:
        window.blit(winner, (75, 200))

    display.update()
    clock.tick(FPS)
