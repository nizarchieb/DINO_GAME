import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 200
GROUND_HEIGHT = 50
FPS = 60
MIN_SPACE_BETWEEN_CACTI = 100  # Adjust as needed

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Dino class
class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (100, HEIGHT - GROUND_HEIGHT - 25)
        self.velocity = 0
        self.jump = False

    def update(self):
        self.velocity += 1
        self.rect.y += self.velocity

        if self.rect.bottom > HEIGHT - GROUND_HEIGHT:
            self.rect.bottom = HEIGHT - GROUND_HEIGHT
            self.velocity = 0
            self.jump = False

    def jump_action(self):
        if not self.jump:
            self.velocity -= 18  # Higher jump
            self.jump = True

# Cactus class
class Cactus(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = pygame.Surface((30, 30))  # Smaller cactus
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = HEIGHT - GROUND_HEIGHT - 30  # Lower cactus

    def update(self):
        self.rect.x -= 5
        if self.rect.right < 0:
            space = MIN_SPACE_BETWEEN_CACTI
            if len(cacti) > 0:
                space += cacti.sprites()[-1].rect.right  # Adjust the space based on the position of the last cactus

            self.rect.left = WIDTH + space  # Space between obstacles
            self.rect.y = HEIGHT - GROUND_HEIGHT - 30  # Reset cactus height

# Timer class
class Timer:
    def __init__(self):
        self.start_time = time.time()

    def get_elapsed_time(self):
        return time.time() - self.start_time

# Initialize game variables
all_sprites = pygame.sprite.Group()
dinosaurs = pygame.sprite.Group()
cacti = pygame.sprite.Group()
timer = Timer()

dino = Dino()
all_sprites.add(dino)
dinosaurs.add(dino)

# Set up Pygame window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Game")
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dino.jump_action()

    # Spawn a new cactus at random intervals
    if random.randint(0, 100) < 1:  # Fewer obstacles
        cactus = Cactus(WIDTH + MIN_SPACE_BETWEEN_CACTI)
        all_sprites.add(cactus)
        cacti.add(cactus)

    # Update sprites
    all_sprites.update()

    # Check for collisions
    if pygame.sprite.spritecollide(dino, cacti, False):
        print("Game Over! Time:", round(timer.get_elapsed_time(), 2), "seconds")
        running = False
 
    # Draw background
    window.fill(BLACK)

    # Draw ground
    pygame.draw.rect(window, WHITE, (0, HEIGHT - GROUND_HEIGHT, WIDTH, GROUND_HEIGHT))
    # Draw sprites
    all_sprites.draw(window)

    # Display time
    font = pygame.font.Font(None, 36)
    time_text = font.render(f"Time: {round(timer.get_elapsed_time(), 2)} seconds", True, WHITE)
    window.blit(time_text, (10, 10))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()