import pygame

from settings import *

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

        # font
        self.font = pygame.font.Font(None, 74)
        self.text = "00"
        self.text_surface = self.font.render(self.text, True, WHITE)

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

    def draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.text_surface, (50, 250))
        if DISPLAY:
            pygame.display.flip()
        else:
            self.window.flip()

if __name__ == "__main__":
    game = Game()
    game.new()
    pygame.quit()
    raise SystemExit
