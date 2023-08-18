import pygame
import random
import numpy as np

class Snake:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction


SCREEN_WIDTH  = 400
SCREEN_HEIGHT = 400
GRID_SIZE = 10
WORLD = np.zeros((SCREEN_WIDTH//GRID_SIZE, SCREEN_HEIGHT//GRID_SIZE))
FPS = 10

snake = Snake(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, "right")

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Font(None, 24)
clock = pygame.time.Clock()

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False    
    
    screen.fill("gray")
    
    # fps = int(clock.get_fps())
    # fps_text = font.render(f"{fps} FPS", False, (0, 0, 0))
    # screen.blit(fps_text, (10, 10))

    pygame.draw.rect(screen, "black", (snake.x, snake.y, GRID_SIZE, GRID_SIZE))

    WORLD[snake.x//GRID_SIZE, snake.y//GRID_SIZE] += 4
    WORLD -= 1
    WORLD[WORLD < 0] = 0

    trace = np.argwhere(WORLD > 0)*GRID_SIZE
    for trace_point in trace:
        pygame.draw.rect(screen, "black", (trace_point[0], trace_point[1], GRID_SIZE, GRID_SIZE))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and snake.direction != "down":
        snake.direction = "up"
    elif keys[pygame.K_d] and snake.direction != "left":
        snake.direction = "right"
    elif keys[pygame.K_s] and snake.direction != "up":
        snake.direction = "down"
    elif keys[pygame.K_a] and snake.direction != "right":
        snake.direction = "left"

    match snake.direction:
        case "up":
            snake.y -= GRID_SIZE
            if snake.y == 0 - GRID_SIZE:
                snake.y = SCREEN_HEIGHT-GRID_SIZE
        case "right": 
            snake.x += GRID_SIZE
            if snake.x == SCREEN_WIDTH:
                snake.x = 0
        case "down":
            snake.y += GRID_SIZE
            if snake.y == SCREEN_HEIGHT:
                snake.y = 0
        case "left":
            snake.x -= GRID_SIZE
            if snake.x == 0 - GRID_SIZE:
                snake.x = SCREEN_WIDTH-GRID_SIZE
        case _:
            raise NotImplementedError

    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()