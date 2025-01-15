from states import State

class Title(State):
    def __init__(self, game):
        State.__init__(self, game)
    
    def update(self, delt, actions):
        self.game.reset_keys() #implement later

    def render(self, display):
        display.fill((255,255,255))
        self.game.draw_text(display, "Title State", (0,0,0), self.game.GAME_WIDTH/2,
                            self.game.GAME_HEIGHT/2)