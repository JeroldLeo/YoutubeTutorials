from states.gameworld import GameWorld
from states.state import State


class Title(State):
    def __init__(self, game):
        State.__init__(self, game)

    def update(self, delta_time, actions):
        if actions["start"]:
            new_state = GameWorld(self.game)
            new_state.enter_state()
        self.game.reset_keys()

    def render(self, display):
        display.fill((255, 255, 255))
        self.game.draw_text(display, "Game States Demo", (0, 0, 0), self.game.GAME_W / 2, self.game.GAME_H / 2)
