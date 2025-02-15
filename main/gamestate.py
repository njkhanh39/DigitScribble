from states import State
from button import Button
from enemy import Enemy, EnemySpawner
import numpy as np
import pygame

# Constants
PIXEL_SIZE = 10  # Each pixel in the grid is 10x10, so the canvas is 280x280
GRID_SIZE = 28
CANVAS_WIDTH, CANVAS_HEIGHT = PIXEL_SIZE * GRID_SIZE, PIXEL_SIZE * GRID_SIZE
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FRAME_COLOR = (100, 100, 100)



class Canva:
    def __init__(self):
        self.canvas_x = (SCREEN_WIDTH - CANVAS_WIDTH) // 2
        self.canvas_y = (SCREEN_HEIGHT - CANVAS_HEIGHT) // 2

        # Canvas grid (initialized to black)
        self.canvas = [[BLACK for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

        self.pixel_drawn = 0
    
    def render(self, screen):
        pygame.draw.rect(screen, FRAME_COLOR, (self.canvas_x - 5, self.canvas_y - 5, CANVAS_WIDTH + 10, CANVAS_HEIGHT + 10))  # Frame
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                pygame.draw.rect(screen, self.canvas[y][x], (self.canvas_x + x * PIXEL_SIZE, self.canvas_y + y * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))
    def paint(self, x, y):
        grid_x = (x - self.canvas_x) // PIXEL_SIZE
        grid_y = (y - self.canvas_y) // PIXEL_SIZE
        if 0 <= grid_x < GRID_SIZE and 0 <= grid_y < GRID_SIZE:
            self.canvas[grid_y][grid_x] = WHITE
            self.pixel_drawn+=1
    def reset(self):
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                self.canvas[y][x] = BLACK
        self.pixel_drawn = 0
    def get_drawing(self):
        arr = []
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                if self.canvas[y][x] == WHITE:
                    arr.append(255.0)
                else: arr.append(0) 
        return arr
    def within_canva(self, x, y):
        return (self.canvas_x <= x and x <= self.canvas_x + CANVAS_WIDTH) and (self.canvas_y <= y and y <= self.canvas_y + CANVAS_HEIGHT)

class GameState(State):
    def __init__(self, game):
        State.__init__(self, game)

        self.init_buttons()

        #canvas
        self.canva = Canva()

        #enemies
        self.enemy_spawner = EnemySpawner(1000, 70) #coordinate of spawner

    def init_buttons(self): 
        self.back_btn = Button(10, 10,
                                100, 50, "BACK", self.game.font_dir, 30)
    
    def handle_input(self, mouse_pos): #instant inputs
        pass

    def handle_event(self, mouse_pos):
        #handle button
        self.back_btn.handle(mouse_pos)

        #game events
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                self.game.playing = False
                self.game.running = False
            elif pygame.mouse.get_pressed()[0]:
                self.canva.paint(x, y)
            elif (event.type == pygame.MOUSEBUTTONUP):
                if(self.canva.pixel_drawn >= 5):
                    X_pred = np.array(self.canva.get_drawing()).reshape(-1, 784)
                    Y_pred = self.game.svc.predict(X_pred)
                    print("PREDICT: ", Y_pred)

                    #test
                    if(Y_pred == 4):
                        self.enemy_spawner.kill_first()
                self.canva.reset()

    def update(self):
        #update buttons

        if self.back_btn.is_clicked():
            print("BACK BUTTON CLICKED!")
            self.exit_state()
        
        
        # self.game.reset_keys() #????
        
        #update entities
        self.enemy_spawner.update(self.game.dt)


    def render(self, display):
        display.fill((0,0,0))

        
        #render buttons

        self.back_btn.render(display)
        self.canva.render(display)
        self.enemy_spawner.render(display)
        