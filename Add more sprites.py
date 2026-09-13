import random
import pygame

# Initialize Pygame and the audio mixer
pygame.init()
pygame.mixer.init()

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
RED = (255, 50, 50)

# Set up the display screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Collision Game")
clock = pygame.time.Clock()

# Load and scale the galaxy background image
try:
    background_image = pygame.image.load("galaxy.jpg")
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
except pygame.error:
    print("Warning: 'galaxy.jpg' not found. Falling back to a solid black background.")
    background_image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_image.fill((0, 0, 0))

# Load the explosion sound effect safely
try:
    explosion_sound = pygame.mixer.Sound("soundreality-explosion-fx-343683.mp3")
except pygame.error:
    print("Warning: 'soundreality-explosion-fx-343683.mp3' not found. Sound will not play.")
    explosion_sound = None

class Player(pygame.sprite.Sprite):
    """The character controlled by the user's arrow keys."""
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        # Start player in the center of the screen
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed = 5 # Pixels moved per frame

    def update(self):
        # Get a list of all currently pressed keys
        keys = pygame.key.get_pressed()
        
        # Move based on arrow keys
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Keep player completely inside the screen boundaries
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):
    """An enemy sprite positioned randomly on the screen."""
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.reset_position()

    def reset_position(self):
        """Moves the enemy to a random location after a collision."""
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)

# Create sprite groups to manage rendering and collisions
all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()

# Instantiate the player
player = Player()
all_sprites.add(player)

# Instantiate 7 enemies at random positions
for _ in range(7):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemy_sprites.add(enemy)

# Game variables
score = 0
font = pygame.font.SysFont(None, 36)

# Main Game Loop
running = True
while running:
    # 1. Handle events (like closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Update sprite positions
    all_sprites.update()

    # 3. Check for collisions
    hit_enemies = pygame.sprite.spritecollide(player, enemy_sprites, False)
    for enemy in hit_enemies:
        score += 1
        
        # Play the explosion sound effect if it was successfully loaded
        if explosion_sound:
            explosion_sound.play()
            
        enemy.reset_position() # Teleport the hit enemy to a new random spot

    # 4. Drawing / Rendering
    # Blit the galaxy background onto the screen
    screen.blit(background_image, (0, 0))

    # Draw all sprites to the screen over the background
    all_sprites.draw(screen)

    # Render and display the score text
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Flip the display buffer to show the new frame
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

pygame.quit()
