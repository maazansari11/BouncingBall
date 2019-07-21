import pygame
import random

# Defining colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# defining with and height and size
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BALL_SIZE = 15


class Ball:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0


def make_ball():

    ball = Ball()
    ball.x = random.randrange(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
    ball.y = random.randrange(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)

    # Speed and direction of ball
    ball.change_x = random.randrange(-2, 6)
    ball.change_y = random.randrange(-2, 6)

    return ball


def main():
    # initialisation
    pygame.init()

    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    # caption for screen
    pygame.display.set_caption("Bouncing Balls")

    done = False

    # for screen updates
    clock = pygame.time.Clock()

    ball_list = []

    ball = make_ball()
    ball_list.append(ball)



    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:# exit's from game
                done = True

        for ball in ball_list:
            # Move the ball
            ball.x += ball.change_x
            ball.y += ball.change_y

            # Bounce the ball
            if ball.y > SCREEN_HEIGHT - BALL_SIZE or ball.y < BALL_SIZE:
                ball.change_y *= -1
            if ball.x > SCREEN_WIDTH - BALL_SIZE or ball.x < BALL_SIZE:
                ball.change_x *= -1

        # Set the screen background
        screen.fill(BLACK)

        # Draw the balls
        for ball in ball_list:
            pygame.draw.circle(screen, WHITE, [ball.x, ball.y], BALL_SIZE)

        # Limit to 60fps
        clock.tick(60)

        # update the screen
        pygame.display.flip()

    # to close the program
    pygame.quit()


if __name__ == "__main__":
    main()