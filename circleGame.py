import pygame

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Player setup
player_pos = pygame.Vector2(screen.get_width() / 2, 600)
velocity_y = 0
gravity = 1000  # pixels per second squared
jump_strength = -500
is_jumping = False

# Ground setup
ground_rect = pygame.Rect(0, 650, 1300, 100)

dt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Horizontal movement
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # Jump input
    if keys[pygame.K_SPACE] and not is_jumping:
        velocity_y = jump_strength
        is_jumping = True

    # Apply gravity
    velocity_y += gravity * dt
    player_pos.y += velocity_y * dt

    # Ground collision
    if player_pos.y + 40 >= ground_rect.top:
        player_pos.y = ground_rect.top - 40
        velocity_y = 0
        is_jumping = False

    # Clamp player inside screen
    player_pos.x = max(40, min(screen.get_width() - 40, player_pos.x))

    # --- DRAW ---
    screen.fill("grey")
    pygame.draw.rect(screen, "gold", ground_rect)
    pygame.draw.circle(screen, "cyan", player_pos, 40)

    pygame.display.flip()
    dt = clock.tick(60) / 1000  # Delta time in seconds

pygame.quit()
