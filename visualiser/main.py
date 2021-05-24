import pygame
import serial
import _thread


class Demo:

    def __init__(self):
        pygame.init()

        # Agent data
        self.width = 40
        self.height = 60
        self.angle = 0
        self.a = pygame.Vector2()
        self.v = pygame.Vector2()
        self.position = pygame.Vector2((380, 270))

        # Initialise screen and main loop
        self.screen = pygame.display.set_mode((800, 600))
        self.running = True

        self.image = pygame.image.load("../resources/blank.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(center=self.position)

        _thread.start_new_thread(self.read_serial, ())
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
            self.draw()
            pygame.display.update()

    def update(self, angle, acceleration):
        self.a = acceleration
        self.angle = angle

        self.v += self.a * 0.1
        self.position += self.v * 0.1

    def draw(self):
        rotated = pygame.transform.rotate(self.image, self.angle)
        rect = rotated.get_rect(center=self.position)
        self.screen.blit(rotated, rect)

    def read_serial(self):
        conn = serial.Serial(port="COM3", baudrate=115200, timeout=.1)
        while self.running:
            data = conn.readline().decode("utf-8")
            data = data.rstrip().split(" ")
            if len(data) == 3:
                angle = float(data[0])
                acceleration = pygame.Vector2(0, 0)
                print(angle)
                print(acceleration)
                self.update(angle, acceleration)


if __name__ == "__main__":
    Demo()
