import pygame, time, random

# Set window size
window_x = 1200
window_y = 900

# Define vars
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
snake_spd = 10
score = 0
fruit_spawn = True

# Initialize game
pygame.init()
game_running = True
font = pygame.font.Font(None, 40) # Setting Font


# Display game window & display fps
game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("hoc and cardin")
fps = pygame.time.Clock()

# Create snake & position
snake_pos = [100, 50]
snake_body = [  [100, 50],
                [90, 50],
                [80, 50],
                [70, 50]
            ]

# Generate fruit position
fruit_pos = [random.randrange(0, (window_x//10)) * 10,
             random.randrange(0, (window_y//10)) * 10]

# function to spawn fruit
def apple_spawn():
    global fruit_spawn, fruit_pos
    # Checks if fruit is spawned, if not, spawn fruit
    if not fruit_spawn:
        fruit_pos = [random.randrange(0, (window_x//10)) * 10,
                     random.randrange(0, (window_y//10)) * 10]
        # Checks if fruit is in snake
        if fruit_pos in snake_body:
            fruit_spawn = False
    
    fruit_spawn = True
    game_window.fill(black)
    
    pygame.draw.rect(game_window, red, pygame.Rect(fruit_pos[0], fruit_pos[1], 10, 10))

# function to draw snake
def draw_snake():
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))


# function to show score
def show_score():
    surface = font.render("Score: " + str(score), True, white)

    game_window.blit(surface, (0, 0))

# main function
while game_running:

    # Quit button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F2:
                game_running = False

    # Spawn apples
    apple_spawn()

    # Draw snake
    draw_snake()

    # Display score
    show_score()

    pygame.display.update()
    fps.tick(snake_spd)




