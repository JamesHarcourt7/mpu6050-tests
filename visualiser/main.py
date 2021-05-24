import pygame
import serial


class Demo:

    def __init__(self):
        pygame.init()

        # Agent data
        self.width = 40
        self.height = 60
        self.angle = 0
        self.position = pygame.Vector2((300 - (self.width // 2), 250 - (self.height // 2)))
        self.image = pygame.image.load("../resources/blank.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        # Initialise screen and main loop
        self.screen = pygame.display.set_mode((600, 500))
        self.running = True
        self.run()

        pygame.quit()

    def run(self):
        # Main loop
        while self.running:
            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((0, 0, 0))

            self.image = pygame.transform.rotate(self.image, self.angle)
            self.screen.blit(self.image, (int(self.position.x), int(self.position.y)))

            pygame.display.update()


if __name__ == "__main__":
    Demo()
