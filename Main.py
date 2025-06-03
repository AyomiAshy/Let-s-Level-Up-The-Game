import pygame
import random
import sys
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Collision Game")
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
player = pygame.Rect(300, 200, 40, 40)
circle_radius = 20
circle_x = random.randint(circle_radius, WIDTH - circle_radius)
circle_y = random.randint(circle_radius, HEIGHT - circle_radius)
MOVE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_EVENT, 1000)
font = pygame.font.SysFont(None, 55)
clock = pygame.time.Clock()
game_over = False
running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == MOVE_EVENT and not game_over:
            circle_x = random.randint(circle_radius, WIDTH - circle_radius)
            circle_y = random.randint(circle_radius, HEIGHT - circle_radius)
    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.left > 0:
            player.x -= 5
        if keys[pygame.K_RIGHT] and player.right < WIDTH:
            player.x += 5
        if keys[pygame.K_UP] and player.top > 0:
            player.y -= 5
        if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
            player.y += 5
        circle_rect = pygame.Rect(circle_x - circle_radius, circle_y - circle_radius, circle_radius * 2, circle_radius * 2)
        if player.colliderect(circle_rect):
            game_over = True
    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.circle(screen, RED, (circle_x, circle_y), circle_radius)
    if game_over:
        text = font.render("Game Over!", True, (0, 0, 0))
        screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()
