from settings import *

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(join("assets", "images", "asteroid.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.speed_y = randint(2, 5)

    def update(self):
        self.rect.y += self.speed_y
