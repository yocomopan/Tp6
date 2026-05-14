from enum import Enum
import arcade
import itertools


class AttackType(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

class AttackAnimation(arcade.Sprite):
        ATTACK_SCALE = 0.50

        def __init__(self, attack_type):
            super().__init__()

            self.attack_type = attack_type
            if self.attack_type == AttackType.ROCK:
                self.textures = [
                    arcade.load_texture("assets/srock.png"),
                    arcade.load_texture("assets/srock-attack.png"),
                ]
            elif self.attack_type == AttackType.PAPER:
                self.textures = [
                    arcade.load_texture("assets/spaper.png"),
                    arcade.load_texture("assets/spaper-attack.png"),
                ]
            else:
                self.textures = [
                    arcade.load_texture("assets/scissors.png"),
                    arcade.load_texture("assets/scissors-close.png"),
                ]

            self.scale = self.ATTACK_SCALE
            self.current_texture = 0
            self.set_texture(self.current_texture)

        ANIMATION_SPEED = 5.0

class Animations:

    def __init__(self, option_chosen):
        self.choice = option_chosen
        if self.choice == AttackType.ROCK:

            self.texture_rock = [
                arcade.load_texture("assets/srock.png"),
                arcade.load_texture("assets/srock-attack.png")
            ]
        if self.choice == AttackType.PAPER:
            self.texture_paper = [
                arcade.load_texture("assets/spaper.png"),
                arcade.load_texture("assets/spaper-attack.png")
            ]
        if self.choice == AttackType.SCISSORS:
            self.texture_scissors = [
                arcade.load_texture("assets/scissors.png"),
                arcade.load_texture("assets/scissors-close.png")
            ]

        cycle_rock = itertools.cycle([self.texture_rock])
        cycle_paper = itertools.cycle([self.texture_paper])
        cycle_scissors = itertools.cycle([self.texture_scissors])
    ANIMATION_SPEED = 5.0




