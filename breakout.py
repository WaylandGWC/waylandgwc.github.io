]import sys
import pygame.draw

WIDTH = 500
HEIGHT = 300

RED = 200, 0, 0
BOX = Rect((20, 20), (100, 100))
WHITE = (255, 255, 255)

BLUE= (0, 0, 200)
RADIUS = 20
circle_x = 150
circle_y = 150
x_velocity = 5
y_velocity = 5
circle_box = None
bricks = []
paddle = Rect((WIDTH/2-10, HEIGHT-10), (40, 20))

def draw():
    screen.fill((128, 100, 0))
    screen.draw.filled_rect(paddle, WHITE)
    for brick in bricks:
        screen.draw.filled_rect(brick, RED)
    pygame.draw.circle(screen.surface, BLUE, (circle_x, circle_y), RADIUS, 0)

    
def update():
    global paddle
    global circle_x, circle_y, x_velocity, y_velocity
    
    if keyboard.right:
        paddle.move_ip(5, 0)
    if keyboard.left:
        paddle.move_ip(-5, 0)
    if paddle.right > WIDTH:
        paddle.right = WIDTH
    elif paddle.left < 0:
        paddle.left = 0
        
    circle_x = circle_x + x_velocity
    circle_y = circle_y + y_velocity
    
    circle_box = Rect((circle_x - RADIUS, circle_y - RADIUS), (RADIUS*2, RADIUS*2))
    
    if circle_x < 0 or circle_x > WIDTH:
        x_velocity = -1 * x_velocity
    if circle_y < 0 or circle_y > HEIGHT:
        y_velocity = -1 * y_velocity
    
    if circle_box.colliderect(paddle):
        y_velocity = -1 * y_velocity
        
    for brick in bricks:
        if circle_box.colliderect(brick):
            bricks.remove(brick)

def setup_game():
    global bricks
    y = 40
    brick_width = 20
    brick_height = 10

    for i in range(0, 5):
        x = 0
        while x < WIDTH:
            brick = Rect((x, y), (x+brick_width, y+brick_height))
            bricks.append(brick)
            x += brick_width
        y += brick_height
        
setup_game()


    
    
