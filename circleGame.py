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
player_radius = 40

# Ground setup
ground_rect = pygame.Rect(0, 650, 1300, 100)

# Multiple floating platforms (like steps)
platforms = [
    pygame.Rect(400, 550, 180, 20),
    pygame.Rect(600, 480, 180, 20),
    pygame.Rect(800, 410, 180, 20),
    pygame.Rect(1000, 340, 180, 20),
]

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
    if keys[pygame.K_w] and not is_jumping:
        velocity_y = jump_strength
        is_jumping = True

    # Apply gravity
    velocity_y += gravity * dt
    player_pos.y += velocity_y * dt

    # --- COLLISIONS ---
    on_platform = False

    # Check collision with each floating platform
    if velocity_y > 0:  # Only check when falling
        for platform in platforms:
            # If player's bottom touches platform top and within horizontal bounds
            if (platform.left < player_pos.x < platform.right and
                player_pos.y + player_radius >= platform.top and
                player_pos.y + player_radius - velocity_y * dt < platform.top):
                player_pos.y = platform.top - player_radius
                velocity_y = 0
                is_jumping = False
                on_platform = True
                break

    # Ground collision
    if not on_platform and player_pos.y + player_radius >= ground_rect.top:
        player_pos.y = ground_rect.top - player_radius
        velocity_y = 0
        is_jumping = False

    # Clamp player inside screen
    player_pos.x = max(player_radius, min(screen.get_width() - player_radius, player_pos.x))

    # --- DRAW ---
    screen.fill("grey")
    pygame.draw.rect(screen, "gold", ground_rect)
    for p in platforms:
        pygame.draw.rect(screen, "brown", p)
    pygame.draw.circle(screen, "cyan", player_pos, player_radius)

    pygame.display.flip()
    dt = clock.tick(60) / 1000  # Delta time in seconds

pygame.quit()
