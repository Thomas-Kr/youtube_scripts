import pygame
import random

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Particle System")

BLACK = (0, 0, 0)

class Particle:
    def __init__(self):
        self.radius = random.randint(10, 20)
        self.x = random.randint(self.radius, width-self.radius)
        self.y = random.randint(self.radius, height-self.radius)
        self.color = (random.randint(0, 255), 
                      random.randint(0, 255), 
                      random.randint(0, 255))
        self.speed = [random.uniform(-5, 5), 
                      random.uniform(-5, 5)]

    def move(self):
        self.x += self.speed[0]
        self.y += self.speed[1]
        if self.x - self.radius < 0 or self.x + self.radius > width:
            self.speed[0] *= -1
            return True
        if self.y - self.radius < 0 or self.y + self.radius > height:
            self.speed[1] *= -1
            return True

    def draw(self):
        pygame.draw.circle(screen, self.color, 
                           (int(self.x), int(self.y)), 
                           self.radius)

particles = [Particle()]
pygame.mixer.music.load("sfx/ring_sfx.mp3")
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for particle in particles:
        if particle.move():
            pygame.mixer.music.play()
            particles.append(Particle())
            
        particle.draw()

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()