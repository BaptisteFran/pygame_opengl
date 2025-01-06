from settings import *
from asteroid import Asteroid

class Game:
    def __init__(self):
        pygame.init()
        if DISPLAY:
            self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        else:
            self.window = pygame.Window(size=(WINDOW_WIDTH, WINDOW_HEIGHT), title="Test OpenGL with Window Module")
            self.screen = self.window.get_surface()
        self.clock = pygame.time.Clock()
        self.running = True

        # groups
        self.all_sprites = pygame.sprite.Group()

        # font
        self.font = pygame.font.Font(None, 74)
        self.text = "00"
        self.text2 = 0
        self.text_surface = self.font.render(self.text, True, WHITE)
        self.text_surface2 = self.font.render(str(self.text2), True, WHITE)


    def spawn_asteroid(self):
        asteroid = Asteroid(randint(150, 1200), randint(-100, -40))
        self.all_sprites.add(asteroid)
        self.text2 += 1


    def new(self):
        self.run()

    def run(self):
        while self.running:
            self.clock.tick()
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.text = "{:.2f}".format(self.clock.get_fps())
        self.text_surface = self.font.render(self.text, True, WHITE)  # Met à jour la surface du texte
        self.spawn_asteroid()
        self.text_surface2 = self.font.render(str(self.text2), True, WHITE)  # Met à jour la surface du texte
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.text_surface, (50, 250))
        self.screen.blit(self.text_surface2, (50, 350))
        self.all_sprites.draw(self.screen)
        if DISPLAY:
            pygame.display.flip()
        else:
            self.window.flip()

if __name__ == "__main__":
    game = Game()
    game.new()
    pygame.quit()
    raise SystemExit
