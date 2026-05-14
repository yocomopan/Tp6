"""
2026-04-16
Ivan Zheryakov
Roche, Papier et Ciseaux
"""
import random

from game_state import GameState
from AttackAnimation import AttackType


"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Starting Template"
option_height = 191


class GameView(arcade.View):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self):
        super().__init__()

        self.background_color = arcade.color.SMOKY_BLACK
        self.title = arcade.Text("Rochambeau",
                                 WINDOW_WIDTH / 2 - 135, WINDOW_HEIGHT - 70,
                                 arcade.color.APPLE_GREEN,
                                 40, font_name="Comic Sans MS")
        self.sub_title = arcade.Text("Appuyez sur l'un des choix proposé ci-dessous pour jouer!",
                                     WINDOW_WIDTH / 2 - 448, WINDOW_HEIGHT - 102,
                                     arcade.color.BLUEBERRY,
                                     25, font_name="Comic Sans MS")

        self.game_state = GameState.NOT_STARTED
        self.reset_score = 0

        self.sprites_rock = [
            arcade.Sprite("assets/srock.png"),
            arcade.Sprite("assets/srock-attack.png")
        ]

        self.score_humain = 0
        self.score_humain_text = arcade.Text(f"Score: {self.score_humain}",
                                             WINDOW_WIDTH / 2 - 385, WINDOW_HEIGHT / 2 + 100,
                                             arcade.color.CANDY_APPLE_RED,
                                             25, font_name="Comic Sans MS")
        self.score_pc = arcade.Text(f"Score: {self.reset_score}",
                                    WINDOW_WIDTH / 2 + 255, WINDOW_HEIGHT / 2 + 100,
                                    arcade.color.CANDY_APPLE_RED,
                                    25, font_name="Comic Sans MS")

        self.beard = arcade.Sprite("assets/faceBeard.png", .60,
                                   WINDOW_WIDTH / 2 - 320, WINDOW_HEIGHT / 2)  # +.20
        self.pc = arcade.Sprite("assets/compy.png", 3,
                                WINDOW_WIDTH / 2 + 320, WINDOW_HEIGHT / 2)  # +1
        self.ore = arcade.Sprite("assets/srock.png", .60,
                                 320 + 320 / 3, option_height)
        self.sheet = arcade.Sprite("assets/spaper.png", .60,
                                   320, option_height)
        self.shears = arcade.Sprite("assets/scissors.png", .60,
                                    320 - 320 / 3, option_height)

        self.beard_list = arcade.SpriteList()
        self.pc_list = arcade.SpriteList()
        self.material_list = arcade.SpriteList()

        self.material_list.append(self.ore)
        self.material_list.append(self.sheet)
        self.material_list.append(self.shears)

        self.beard_list.append(self.beard)
        self.pc_list.append(self.pc)

        self.player_attack_type = {
            AttackType.ROCK: False,
            AttackType.PAPER: False,
            AttackType.SCISSORS: False
        }
        self.pat = self.player_attack_type
        self.computer_attack_type = None
        self.cat = self.computer_attack_type

    def reset(self):
        """Reset the game to the initial state."""
        # Do changes needed to restart the game here if you want to support that
        pass

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()
        self.beard_list.draw()
        self.pc_list.draw()
        self.material_list.draw()

        self.title.draw()
        self.sub_title.draw()
        self.score_humain_text.draw()
        self.score_pc.draw()

        # Call draw() on all your sprite lists below

    def on_update(self, delta_time):

        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.cat = random.choice(list(AttackType.__iter__()))
        if self.cat == self.pat:
            print("partie nulle")

        elif ((self.cat == 1 and self.pat == 2) or
              (self.cat == 0 and self.pat == 1) or
              (self.cat == 2 and self.pat == 0)):
            self.score_humain += 1

        elif ((self.cat == 2 and self.pat == 1) or
              (self.cat == 1 and self.pat == 0) or
              (self.cat == 0 and self.pat == 2)):
            self.score_pc += 1



    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        if key == arcade.key.SPACE:
            if self.game_state == GameState.NOT_STARTED:
                self.game_state = GameState.ROUND_ACTIVE


    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        if self.game_state != GameState.ROUND_ACTIVE:
            return

        if self.ore.collides_with_point((x, y)):
            self.player_attack_type[AttackType.ROCK] = True
            print("ore")

        if self.sheet.collides_with_point((x, y)):
            self.player_attack_type[AttackType.PAPER] = True
            print("sheet")

        if self.shears.collides_with_point((x, y)):
            self.player_attack_type[AttackType.SCISSORS] = True
            print("shears")





def main():
    """ Main function """
    # Create a window class. This is what actually shows up on screen
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    # Create and setup the GameView
    game = GameView()

    # Show GameView on screen
    window.show_view(game)

    # Start the arcade game loop
    arcade.run()


if __name__ == "__main__":
    main()
