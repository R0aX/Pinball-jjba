import pygame
import random

# Initialize Pygame
pygame.init()

# 1. Screen Dimensions (Portrait Format)
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JoJo Pinball Adventure")

# --- IMAGE LOADING ---
try:
    # Load the background image from your folder
    bg_img = pygame.image.load("jojo.background.png")
    # Scale it to fit the screen size exactly
    bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))
except Exception as e:
    print(f"Could not load image: {e}")
    # Fallback if the image isn't in the same folder as the script
    bg_img = pygame.Surface((WIDTH, HEIGHT))
    bg_img.fill((20, 20, 40))

# Colors
PURPLE, ORANGE = (140, 0, 255), (255, 140, 0)
YELLOW, WHITE = (255, 255, 0), (255, 255, 255)

clock = pygame.time.Clock()
font = pygame.font.SysFont("Verdana", 32, bold=True)

# 2. Physics Variables
ball_pos = pygame.Vector2(WIDTH // 2, 100)
ball_vel = pygame.Vector2(random.choice([-4, 4]), 2)
ball_radius = 12
gravity = 0.2
friction = 0.995

# Flipper Dimensions
f_width, f_height = 130, 25
left_flipper_base = pygame.Vector2(WIDTH // 2 - 165, HEIGHT - 100)
right_flipper_base = pygame.Vector2(WIDTH // 2 + 35, HEIGHT - 100)

# 3. Obstacles (Bumpers)
bumpers = [
    {"pos": pygame.Vector2(WIDTH // 2, 200), "radius": 45, "color": (255, 50, 50)},
    {"pos": pygame.Vector2(WIDTH // 4, 380), "radius": 35, "color": (50, 255, 50)},
    {"pos": pygame.Vector2(3 * WIDTH // 4, 380), "radius": 35, "color": (50, 255, 50)},
]

score = 0
running = True

while running:
    clock.tick(60)
    
    # --- DRAW BACKGROUND FIRST ---
    screen.blit(bg_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    l_active = keys[pygame.K_a]
    r_active = keys[pygame.K_d]

    # Ball Physics
    ball_vel.y += gravity
    ball_vel *= friction
    ball_pos += ball_vel

    # Wall Bounces
    if ball_pos.x <= ball_radius or ball_pos.x >= WIDTH - ball_radius:
        ball_vel.x *= -0.8
        ball_pos.x = max(ball_radius, min(ball_pos.x, WIDTH - ball_radius))
    if ball_pos.y <= ball_radius:
        ball_vel.y *= -0.8
        ball_pos.y = ball_radius

    # Bumper Collisions
    for b in bumpers:
        dist = ball_pos.distance_to(b["pos"])
        if dist < ball_radius + b["radius"]:
            normal = (ball_pos - b["pos"]).normalize()
            ball_vel = ball_vel.reflect(normal) * 1.4
            ball_pos = b["pos"] + normal * (ball_radius + b["radius"] + 1)
            score += 100

    # Flipper Logic
    l_y = left_flipper_base.y - (35 if l_active else 0)
    left_rect = pygame.Rect(left_flipper_base.x, l_y, f_width, f_height)
    
    r_y = right_flipper_base.y - (35 if r_active else 0)
    right_rect = pygame.Rect(right_flipper_base.x, r_y, f_width, f_height)

    # Collision check
    if left_rect.collidepoint(ball_pos.x, ball_pos.y + ball_radius):
        ball_vel.y = -abs(ball_vel.y) * (1.6 if l_active else 1.1)
        ball_vel.x += (ball_pos.x - left_rect.centerx) * 0.15
    
    if right_rect.collidepoint(ball_pos.x, ball_pos.y + ball_radius):
        ball_vel.y = -abs(ball_vel.y) * (1.6 if r_active else 1.1)
        ball_vel.x += (ball_pos.x - right_rect.centerx) * 0.15

    # Reset
    if ball_pos.y > HEIGHT:
        ball_pos = pygame.Vector2(WIDTH // 2, 100)
        ball_vel = pygame.Vector2(random.uniform(-4, 4), 3)
        score = 0

    # Drawing Game Elements
    for b in bumpers:
        # Draw bumpers with a slight glow
        pygame.draw.circle(screen, b["color"], b["pos"], b["radius"])
        pygame.draw.circle(screen, WHITE, b["pos"], b["radius"], 4)

    pygame.draw.rect(screen, PURPLE, left_rect, border_radius=15)
    pygame.draw.rect(screen, ORANGE, right_rect, border_radius=15)
    
    # Draw the ball (Golden Spirit!)
    pygame.draw.circle(screen, YELLOW, ball_pos, ball_radius)
    pygame.draw.circle(screen, WHITE, ball_pos, ball_radius, 3)

    # Score Counter (Added a small shadow for readability)
    score_shadow = font.render(f"SCORE: {score}", True, (0, 0, 0))
    score_txt = font.render(f"SCORE: {score}", True, WHITE)
    screen.blit(score_shadow, (22, 22))
    screen.blit(score_txt, (20, 20))

    pygame.display.flip()

pygame.quit()