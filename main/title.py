from states import State
from button import Button
from gamestate import GameState

class Title(State):
    def __init__(self, game):
        State.__init__(self, game)

        self.init_buttons()

    def init_buttons(self): 
        self.play_btn = Button(self.game.SCREEN_WIDTH/2 - 100, self.game.SCREEN_HEIGHT/2 - 50,
                               100, 50, "PLAY", self.game.font_dir, 30)
    
    def handle_input(self, mouse_pos): #instant inputs
        pass

    def handle_event(self, mouse_pos):
        #handle button
        self.play_btn.handle(mouse_pos)

    def update(self):
        #update buttons

        if self.play_btn.is_clicked():
            print("ENTER GAMESTATE!")
            
            new_state = GameState(self.game)
            new_state.enter_state()
        
       # self.game.reset_keys() #????

    def render(self, display):
        display.fill((0,0,0))
        self.game.draw_text(display, "DIGIT SCRIBBLE", (255,255,255), self.game.SCREEN_WIDTH/2,
                            self.game.SCREEN_HEIGHT/4)
        
        #render buttons

        self.play_btn.render(display)