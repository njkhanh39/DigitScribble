from loadmodel import RBF_SVM
from predict_image import ImageProcessor
import os, time, pygame
from title import Title

class Game:
    def __init__(self):
        #innit model
        self.init_model()

        #self.GAME_WIDTH, self.GAME_HEIGHT = 960, 540
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 1280, 720

        #running boolean
        self.playing = False
        self.running = True

        #canvas for gaming -- not sure how to use yet
        #self.game_canvas = pygame.Surface((self.GAME_WIDTH, self.GAME_HEIGHT))
        #screen for display
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        #state stack
        self.state_stack = []

        #delta time
        self.dt, self.prev_time = 0, 0

        #actions
        self.actions = {"left": False, "right": False, "down": False, "up": False}
        self.mouse_pos = [0,0]

        #load assets (implement later)
        self.load_assets() 

        #RUN
        self.load_states()
    
    def init_model(self):
        self.svc = RBF_SVM()
        self.svc.load()
        

    def game_loop(self):
        self.update_dt()
        self.handle_input() #handle instant input top of state + mousepos
        self.event_handling()
        self.update() #update the state
        self.render() #render screen + state
    
    def handle_input(self):
        #mouse pos
        self.mouse_pos = pygame.mouse.get_pos()

        #update top state
        self.state_stack[-1].handle_input(self.mouse_pos)

    def event_handling(self):
        #state events

        self.state_stack[-1].handle_event(self.mouse_pos)

        #screen event (quitting) + inputs? (might fix later)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            
            #pressing keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.actions['left'] = True
                if event.key == pygame.K_d:
                    self.actions['right'] = True
                if event.key == pygame.K_s:
                    self.actions['down'] = True
                if event.key == pygame.K_w:
                    self.actions['up'] = True
            #releasing keys
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.actions['left'] = False
                if event.key == pygame.K_d:
                    self.actions['right'] = False
                if event.key == pygame.K_s:
                    self.actions['down'] = False
                if event.key == pygame.K_w:
                    self.actions['up'] = False

    def clear(self, color = (0,0,0)):
        self.screen.fill(color)
    
    #render screen + state
    def render(self):
        self.state_stack[-1].render(self.screen)
        self.screen.blit(pygame.transform.scale(self.screen, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)), (0,0))
        pygame.display.flip()
    
    def update(self):
        self.state_stack[-1].update()
    
    #helpers, called within class???!
    def update_dt(self):
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now
    
    def draw_text(self, surface, text, color, x, y):
        text_surface = self.font.render(text, True, color)
        #text_surface.set_colorkey((0,0,0))
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        surface.blit(text_surface, text_rect)
    
    def load_assets(self):
        #pointers to dir
        # self.main_dir = os.path.join("main")
        # self.assets_dir = os.path.join(self.main_dir, "assets")
        # self.sprites_dir = os.path.join(self.assets_dir, "sprites")
        # self.fonts_dir = os.path.join(self.assets_dir, "fonts")

        # print("Font path: ", self.fonts_dir)
        #add the font later
        self.font = pygame.font.Font('main\\assets\\fonts\\audiowide.ttf', 50)
        self.font_dir = 'main\\assets\\fonts\\audiowide.ttf'

    def load_states(self):
        self.title_screen = Title(self)
        self.state_stack.append(self.title_screen)
    
    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False
# pygame.init()

# SCREEN_WIDTH = 1280
# SCREEN_HEIGHT = 720

# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# player = pygame.Rect((300, 250, 50, 50))

# run = True
# while run:
#     #clear before render

#     screen.fill((0,0,0))

#     #render
#     pygame.draw.rect(screen, (255, 0, 0), player)

#     key = pygame.key.get_pressed()

#     if key[pygame.K_a] == True: 
#         player.move_ip(-1,0)
#     elif key[pygame.K_d] == True: 
#         player.move_ip(1,0)
#     elif key[pygame.K_w] == True: 
#         player.move_ip(0,-1)
#     elif key[pygame.K_s] == True: 
#         player.move_ip(0, 1)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#     #update
#     pygame.display.update()
    

# pygame.quit()