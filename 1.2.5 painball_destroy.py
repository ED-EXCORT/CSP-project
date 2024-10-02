import pygame  # Import the Pygame library for game development
import random  # Import the random module for generating random values
import time  # Import the time module for handling time-related functions
from leaderboard import *  # Import functions for leaderboard management

# Initialize Pygame
pygame.init()

# Set up constants for the game
SCREEN_WIDTH = 800  # Width of the game window
SCREEN_HEIGHT = 600  # Height of the game window
WHITE = (255, 255, 255)  # Color for white
BLACK = (0, 0, 0)  # Color for black
PADDLE_WIDTH = 100  # Width of the paddle
PADDLE_HEIGHT = 20  # Height of the paddle
BALL_RADIUS = 10  # Radius of the ball
PADDLE_SPEED = 10  # Speed at which the paddle moves
BALL_SPEED_X = 4  # Initial horizontal speed of the ball
BALL_SPEED_Y = -4  # Initial vertical speed of the ball
TARGET_WIDTH = 80  # Width of each target
TARGET_HEIGHT = 20  # Height of each target
ROWS = 3  # Number of rows of targets
COLS = 6  # Number of columns of targets
LEADERBOARD_FILE = 'leaderboard.txt'  # File for leaderboard storage

# Initialize font for rendering text
pygame.font.init()
FONT = pygame.font.Font(None, 36)  # Set font size to 36

# Initialize the screen with specified dimensions
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Paintball_destroy")  # Set the window title

# Function to initialize the paddle
def create_paddle():
    # Create a rectangle for the paddle and position it at the bottom center of the screen
        #line of code 37 based on the snippet of code from https://www.geeksforgeeks.org/create-a-pong-game-in-python-pygame/
    paddle = pygame.Rect(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - 40, PADDLE_WIDTH, PADDLE_HEIGHT)
    return paddle  # Return the paddle rectangle
# end of snippet

# Function to initialize the ball

def create_ball():
    # Create a rectangle for the ball and position it in the center of the screen
    #line of code 45 based on the snippet of code from https://www.geeksforgeeks.org/create-a-pong-game-in-python-pygame/
    ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_RADIUS, SCREEN_HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
    #end of snippet

    return ball  # Return the ball rectangle

# Function to create the targets
def create_targets():
    targets = []  # Initialize an empty list to store target rows
    for row in range(ROWS):  # Loop through the number of rows
        target_row = []  # Initialize an empty list for each row of targets
        for col in range(COLS):  # Loop through the number of columns
            # Calculate target position based on its row and column
            target_x = 60 + col * (TARGET_WIDTH + 10)
            target_y = 60 + row * (TARGET_HEIGHT + 10)
            # Create a rectangle for the target and add it to the row
            target_row.append(pygame.Rect(target_x, target_y, TARGET_WIDTH, TARGET_HEIGHT))
        targets.append(target_row)  # Add the row of targets to the targets list
    return targets  # Return the list of target rows

# Function to draw the paddle, ball, and targets on the screen
def draw_game_elements(paddle, ball, targets):
    # Draw paddle
    pygame.draw.rect(screen, WHITE, paddle)  # Draw the paddle in white
    # Draw ball
    pygame.draw.ellipse(screen, WHITE, ball)  # Draw the ball in white
    # Draw targets
    for row in targets:  # Loop through each row of targets
        for target in row:  # Loop through each target in the row
            pygame.draw.rect(screen, WHITE, target)  # Draw each target in white

#snipet code borrowed from https://stackoverflow.com/questions/16044229/how-to-get-keyboard-input-in-pygame

# Function to move the paddle based on user input
def move_paddle(paddle):
    keys = pygame.key.get_pressed()  # Get the state of all keys
    if keys[pygame.K_LEFT] and paddle.left > 0:  # Move left if the left key is pressed
        paddle.move_ip(-PADDLE_SPEED, 0)  # Move paddle left
    if keys[pygame.K_RIGHT] and paddle.right < SCREEN_WIDTH:  # Move right if the right key is pressed
        paddle.move_ip(PADDLE_SPEED, 0)  # Move paddle right
        
# End of snippet code------------------------

# Function to move the ball and handle collisions with walls, paddle, and targets
def move_ball(ball, ball_speed_x, ball_speed_y, paddle, targets):
    ball.x += ball_speed_x  # Update ball's horizontal position
    ball.y += ball_speed_y  # Update ball's vertical position

    # Ball collision with walls
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:  # If ball hits left or right wall
        ball_speed_x *= -1  # Reverse horizontal direction
    if ball.top <= 0:  # If ball hits the top wall
        ball_speed_y *= -1  # Reverse vertical direction

    # Ball collision with paddle
    if ball.colliderect(paddle):  # If ball collides with paddle
        ball_speed_y *= -1  # Reverse vertical direction

    # Ball collision with targets
    for row in targets:  # Loop through each row of targets
        for target in row:  # Loop through each target in the row
            if ball.colliderect(target):  # If ball collides with a target
                row.remove(target)  # Remove the target from the row
                ball_speed_y *= -1  # Reverse vertical direction
                return ball_speed_x, ball_speed_y, True  # Return True if hit a target

    return ball_speed_x, ball_speed_y, False  # Return False if no target hit

# Function to reset the ball position when it goes out of bounds
def reset_ball(ball):
    # Reset ball position to the center of the screen
    ball.x = SCREEN_WIDTH // 2 - BALL_RADIUS
    ball.y = SCREEN_HEIGHT // 2 - BALL_RADIUS
    # Return a random horizontal direction for the ball
    return random.choice([-BALL_SPEED_X, BALL_SPEED_X]), BALL_SPEED_Y

# Function to display score and timer on the screen
def display_score_and_timer(score, start_time):
    elapsed_time = int(time.time() - start_time)  # Calculate elapsed time
    score_text = FONT.render(f'Score: {score}', True, WHITE)  # Render score text
    timer_text = FONT.render(f'Time: {elapsed_time}s', True, WHITE)  # Render timer text
    screen.blit(score_text, (10, 10))  # Draw score text on screen
    screen.blit(timer_text, (SCREEN_WIDTH - 150, 10))  # Draw timer text on screen

# I used reference code from catchAturtle.py and Space_turtles_Samuhel_1.1.9.py
# Function to display the end game leaderboard
def show_leaderboard(player_name, score, elapsed_time):
    # Get current leaderboard data
    leader_names = get_names(LEADERBOARD_FILE)  # Get names from leaderboard file
    leader_scores = get_scores(LEADERBOARD_FILE)  # Get scores from leaderboard file

    # Update leaderboard with the current player's score
    update_leaderboard(LEADERBOARD_FILE, leader_names, leader_scores, player_name, score)

    # Display the updated leaderboard
    screen.fill(BLACK)  # Clear the screen
    end_text = FONT.render('Game Over! Final Scores:', True, WHITE)  # Render game over text
    screen.blit(end_text, (SCREEN_WIDTH // 2 - end_text.get_width() // 2, 100))  # Center the text
    
    y_offset = 200  # Starting vertical position for scores
    for index, name in enumerate(leader_names):  # Loop through leaderboard names
        score_text = FONT.render(f'{index + 1}. {name} - {leader_scores[index]} pts', True, WHITE)  # Render score text
        screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, y_offset))  # Center the score text
        y_offset += 50  # Increment y-offset for the next score

    pygame.display.flip()  # Update the display
    pygame.time.wait(5000)  # Show leaderboard for 5 seconds
# end of reference code from catchAturtle.py and Space_turtles_Samuhel_1.1.9.py
# Main game loop
def game_loop(player_name):
    # Load background image
    background = pygame.image.load('background.png')  # Load the background image (replace with your image file)

    # Initialize the paddle, ball, and targets
    paddle = create_paddle()  # Create the paddle
    ball = create_ball()  # Create the ball
    targets = create_targets()  # Create the targets

    # Ball speed
    ball_speed_x = BALL_SPEED_X  # Set initial horizontal speed of the ball
    ball_speed_y = BALL_SPEED_Y  # Set initial vertical speed of the ball

    # Timer and score
    start_time = time.time()  # Record the start time
    score = 0  # Initialize score

    running = True  # Control the main game loop
    while running:
        screen.blit(background, (0, 0))  # Draw the background

        # Event handling
        for event in pygame.event.get():  # Loop through all events
            if event.type == pygame.QUIT:  # Check if the quit event is triggered
                running = False  # Exit the game loop

        # Move paddle and ball
        move_paddle(paddle)  # Move the paddle based on user input
        ball_speed_x, ball_speed_y, target_hit = move_ball(ball, ball_speed_x, ball_speed_y, paddle, targets)  # Move the ball

        # Update score if a target is hit
        if target_hit:  # Check if a target was hit
            score += 1  # Increment score

        # Reset the ball if it goes out of bounds
        if ball.bottom >= SCREEN_HEIGHT:  # If the ball goes out of bounds
            ball_speed_x, ball_speed_y = reset_ball(ball)  # Reset the ball position

        # Draw the paddle, ball, and targets
        draw_game_elements(paddle, ball, targets)  # Draw all game elements

        # Display the score and timer
        display_score_and_timer(score, start_time)  # Show score and timer on the screen

        # Check win condition
        if score >= 10:  # Check if the player has reached the score goal wich is 10 just for testing purpuses lol
            show_leaderboard(player_name, score, int(time.time() - start_time))  # Show leaderboard
            running = False  # Exit the game loop
            
         #code snippet from https://stackoverflow.com/questions/67285976/pygame-pygame-time-clock-or-time-sleep
        # Update the display and set the frame rate
        pygame.display.flip()  # Update the screen
        pygame.time.Clock().tick(60)  # Set frame rate to 60 FPS
        #end of code snippet
        
    # Quit Pygame
    pygame.quit()  # Exit Pygame

# Start the game after asking for the player's name
def main():
    player_name = input("Enter your name: ")  # Prompt user for their name
    game_loop(player_name)  # Start the game loop with the player's name

# I learned about this here https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
if __name__ == "__main__":
    main()  # Run the main function if the script is executed
