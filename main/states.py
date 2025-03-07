import pygame

#abstract base class
class State():
    def __init__(self, game):
        self.game = game
        self.prev_state = None
    
    def handle_input(self, mouse_pos): #instant inputs
        pass

    def handle_event(self, mouse_pos):
        pass

    def update(self):
        pass

    def render(self, surface):
        pass

    def enter_state(self):
        if len(self.game.state_stack) > 1:
            self.prev_state = self.game.state_stack[-1]
        self.game.state_stack.append(self)
    
    def exit_state(self):
        self.game.state_stack.pop()
