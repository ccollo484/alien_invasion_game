# in the game alien invasion the player controls a ship by moving it left or right with the arrow keys and fire bullets with the spacebar, a fleet of aliens move down the screen and when one group is beaten a new fleet spawns which moves faster, if the aliens reach
# the bottom of the screen the player loses.

import sys

import pygame


class AlienINvasion:
    """overall class to manager game assets and behaviour"""

    def __init__(self):
        """initialise the game, and create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.caption("Alien Invasion")

        def run_game(self):
            """start the main loop for the game."""
            while True:
                # Watch for keyboard and mouse events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

                        # Make the most recently drawn screen visible.


if __name__ == "__main__":
    # make a game instance, and run the game.
    ai = AlienINvasion()
    ai.run_game()
