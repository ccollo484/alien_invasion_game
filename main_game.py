# in the game alien invasion the player controls a ship by moving it left or right with the arrow keys and fire bullets with the spacebar, a fleet of aliens move down the screen and when one group is beaten a new fleet spawns which moves faster, if the aliens reach
# the bottom of the screen the player loses.

import sys

import pygame

from settings import Settings


class AlienInvasion:
    """overall class to manager game assets and behaviour"""

    def __init__(self):
        """initialise the game, and create game resources"""
        pygame.init()
        # sets frame rate to the same on every system
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        # set the background colour
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    # make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
