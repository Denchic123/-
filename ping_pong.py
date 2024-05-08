from pygame import *
"Размер окна"
Win_HEIGHT = 500
Win_WIDTH = 700
window = display.set_mode((Win_WIDTH, Win_HEIGHT))
display.set_caption('ping_pong')
window.fill((250, 243, 177))
FPS = 60
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed_x = player_speed
        self.speed_y = player_speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def updateL(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >= 5:
            self.rect.y -= self.speed
        elif keys[K_DOWN] and self.rect.y <= Win_HEIGHT- 150:
            self.rect.y += self.speed

    def updateR(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >= 5:
            self.rect.y -= self.speed
        elif keys[K_s] and self.rect.y <= Win_HEIGHT - 150:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x


player1 = Player('racket.png', 5,Win_HEIGHT - 200, 10, 50, 150)
player2 = Player('racket.png', 645,Win_HEIGHT - 200, 10, 50, 150)
ball = Ball('tenis_ball.png',200, 200, 10, 50, 50)

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill((250, 243, 177))
    if not finish:
        player1.updateL()
        player1.reset()
        player2.updateR()
        player2.reset()
        ball.update()
        ball.reset()
    display.update()
    clock.tick(FPS)