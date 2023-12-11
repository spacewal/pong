import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)  # Change the color to black
FPS = 60

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Create the paddles and the ball
player_paddle = pygame.Rect(10, HEIGHT // 2 - 50, 10, 100)  # Left paddle
opponent_paddle = pygame.Rect(WIDTH - 20, HEIGHT // 2 - 50, 10, 100)  # Right paddle
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)

# Initial ball speed
ball_speed_x = 7
ball_speed_y = 7

# Initial scores
player_score = 0
opponent_score = 0

# Font for the scoreboard
font = pygame.font.Font(None, 36)

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    
    # Manual control for left paddle
    if keys[pygame.K_w] and player_paddle.top > 0:
        player_paddle.y -= 7
    if keys[pygame.K_s] and player_paddle.bottom < HEIGHT:
        player_paddle.y += 7

    # Opponent's paddle movement (automatic)
    if opponent_paddle.centery < ball.centery:
        opponent_paddle.y += 7
    elif opponent_paddle.centery > ball.centery:
        opponent_paddle.y -= 7

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with paddles
    if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
        ball_speed_x = -ball_speed_x

    # Ball collision with top and bottom walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y = -ball_speed_y

    # Scoring
    if ball.left <= 0:
        opponent_score += 1
        ball_speed_x = -ball_speed_x
        ball.x = WIDTH // 2 - 15
        ball.y = HEIGHT // 2 - 15

    if ball.right >= WIDTH:
        player_score += 1
        ball_speed_x = -ball_speed_x
        ball.x = WIDTH // 2 - 15
        ball.y = HEIGHT // 2 - 15

    # Drawing everything on the screen
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, player_paddle)
    pygame.draw.rect(screen, BLACK, opponent_paddle)
    pygame.draw.ellipse(screen, BLACK, ball)

    # Draw the scoreboard
    player_text = font.render(f"Player: {player_score}", True, BLACK)
    opponent_text = font.render(f"Opponent: {opponent_score}", True, BLACK)
    screen.blit(player_text, (WIDTH // 4, 10))
    screen.blit(opponent_text, (WIDTH // 2, 10))

    # Update the display
    pygame.display.flip()

    # Set the frames per second
    clock.tick(FPS)
