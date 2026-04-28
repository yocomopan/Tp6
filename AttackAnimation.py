from enum import Enum
import arcade
import itertools


class AttackType(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

    def animations(self):
        self.sprites_rock = [
            arcade.Sprite("assets/srock.png"),
            arcade.Sprite("assets/srock-attack.png")
        ]
        self.sprites_paper = [
            arcade.Sprite("assets/spaper.png"),
            arcade.Sprite("assets/spaper-attack.png")
        ]
        self.sprites_scissors = [
            arcade.Sprite("assets/scissors.png"),
            arcade.Sprite("assets/scissors-close.png")
        ]
        cycle_rock = itertools.cycle(self.sprites_rock)
        cycle_paper = itertools.cycle(self.sprites_paper)
        cycle_scissors = itertools.cycle(self.sprites_scissors)
