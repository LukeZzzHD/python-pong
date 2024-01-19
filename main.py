import pygame
import sys
from settings import *
from events import *

# Initialize Pygame
pygame.init()

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(GAME_TITLE)

# Font setup
font = pygame.font.Font(None, 36)

# Function to display text on the screen
def draw_text(text, x, y):
    text_surface = font.render(text, True, TEXT_COLOR)
    screen.blit(text_surface, (x, y))

# Function to start the game
def start_game():
    ball_rect.center = (WIDTH // 2, HEIGHT // 2)
    paddle1_rect.centery = HEIGHT // 2
    paddle2_rect.centery = HEIGHT // 2
    global BALL_SPEED_Y  # Use global keyword to modify the global variable
    BALL_SPEED_Y = INITIAL_BALL_SPEED_Y  # Reset vertical ball speed
    return 0, 0

# Create paddles and ball
paddle1_rect = pygame.Rect(50, 150, 10, 100)
paddle2_rect = pygame.Rect(WIDTH - 60, 150, 10, 100)
ball_rect = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)

# Initialize game variables
score1, score2 = start_game()

# Initialize movement variables
paddle1_move_up = paddle1_move_down = False
paddle2_move_up = paddle2_move_down = False

# Game loop
clock = pygame.time.Clock()
game_active = False

while True:
    for event in pygame.event.get():
        if user_closed_window(event):
            pygame.quit()
            sys.exit()
        elif key_is_pressed(event):
            if key_is_W(event):
                paddle1_move_up = True
            elif key_is_S(event):
                paddle1_move_down = True
            elif key_is_ArrowUP(event):
                paddle2_move_up = True
            elif key_is_ArrowDown(event):
                paddle2_move_down = True
            elif key_is_Space(event) and not game_active:
                game_active = True
        elif key_is_released(event):
            if key_is_W(event):
                paddle1_move_up = False
            elif key_is_S(event):
                paddle1_move_down = False
            elif key_is_ArrowUP(event):
                paddle2_move_up = False
            elif key_is_ArrowDown(event):
                paddle2_move_down = False

    # Move paddles if movement keys are held
    if paddle1_move_up:
        paddle1_rect.y -= PADDLE_SPEED
    if paddle1_move_down:
        paddle1_rect.y += PADDLE_SPEED
    if paddle2_move_up:
        paddle2_rect.y -= PADDLE_SPEED
    if paddle2_move_down:
        paddle2_rect.y += PADDLE_SPEED

    # Ensure paddles stay within bounds
    paddle1_rect.y = max(0, min(HEIGHT - paddle1_rect.height, paddle1_rect.y))
    paddle2_rect.y = max(0, min(HEIGHT - paddle2_rect.height, paddle2_rect.y))

    # Move ball
    if game_active:
        ball_rect.x += BALL_SPEED_X
        ball_rect.y += BALL_SPEED_Y

        # Collision with paddles
        if ball_rect.colliderect(paddle2_rect) or ball_rect.colliderect(paddle1_rect):
            BALL_SPEED_X = -BALL_SPEED_X
            # Adjust vertical speed based on collision point
            if ball_rect.colliderect(paddle1_rect):
                ball_rect.y += (ball_rect.centery - paddle1_rect.centery) // 10
            if ball_rect.colliderect(paddle2_rect):
                ball_rect.y += (ball_rect.centery - paddle2_rect.centery) // 10

        # Collision with top and bottom
        if ball_rect.top <= 0 or ball_rect.bottom >= HEIGHT:
            BALL_SPEED_Y = -BALL_SPEED_Y

        # Scoring and resetting vertical trajectory
        if ball_rect.right >= WIDTH or ball_rect.left <= 0:
            if ball_rect.right >= WIDTH:
                score1 += 1
            else:
                score2 += 1

            if score1 >= 5 or score2 >= 5:
                score1, score2 = start_game()
                game_active = False
            else:
                start_game()  # Reset vertical trajectory
                game_active = False

    # Draw everything
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, PADDLE_1_COLOR, paddle1_rect)
    pygame.draw.rect(screen, PADDLE_2_COLOR, paddle2_rect)
    pygame.draw.ellipse(screen, BALL_COLOR, ball_rect)

    if not game_active:
        draw_text("Press SPACE to start", WIDTH // 4, HEIGHT // 2)

    draw_text(f"{score1} : {score2}", WIDTH // 2 - 30, 20)

    # Update the display
    pygame.display.flip()

    # Set the frames per second
    clock.tick(60)