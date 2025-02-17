from states import State
from button import Button
from enemy import Enemy, EnemySpawner
from animation import Animation
import numpy as np
import pygame
import global_constants as gc





class Canva:
    def __init__(self):
        self.canvas_x = (gc.SCREEN_WIDTH - gc.CANVAS_WIDTH) // 2
        self.canvas_y = (gc.SCREEN_HEIGHT - gc.CANVAS_HEIGHT) // 2 + 200

        # Canvas grid (initialized to black)
        self.canvas = [[gc.BLACK for _ in range(gc.GRID_SIZE)] for _ in range(gc.GRID_SIZE)]

        self.pixel_drawn = 0
    
    def render(self, screen):
        pygame.draw.rect(screen, gc.FRAME_COLOR, (self.canvas_x - 5, self.canvas_y - 5, gc.CANVAS_WIDTH + 10, gc.CANVAS_HEIGHT + 10))  # Frame
        for y in range(gc.GRID_SIZE):
            for x in range(gc.GRID_SIZE):
                pygame.draw.rect(screen, self.canvas[y][x], (self.canvas_x + x * gc.PIXEL_SIZE, self.canvas_y + y * gc.PIXEL_SIZE, gc.PIXEL_SIZE, gc.PIXEL_SIZE))
    def paint(self, x, y):
        grid_x = (x - self.canvas_x) // gc.PIXEL_SIZE
        grid_y = (y - self.canvas_y) // gc.PIXEL_SIZE
        if 0 <= grid_x < gc.GRID_SIZE and 0 <= grid_y < gc.GRID_SIZE:
            self.canvas[grid_y][grid_x] = gc.WHITE
            self.pixel_drawn+=1
    def reset(self):
        for y in range(gc.GRID_SIZE):
            for x in range(gc.GRID_SIZE):
                self.canvas[y][x] = gc.BLACK
        self.pixel_drawn = 0
    def get_drawing(self):
        arr = []
        for y in range(gc.GRID_SIZE):
            for x in range(gc.GRID_SIZE):
                if self.canvas[y][x] == gc.WHITE:
                    arr.append(255.0)
                else: arr.append(0) 
        return arr
    def within_canva(self, x, y):
        return (self.canvas_x <= x and x <= self.canvas_x + gc.CANVAS_WIDTH) and (self.canvas_y <= y and y <= self.canvas_y + gc.CANVAS_HEIGHT)

class GameState(State):
    def __init__(self, game):
        State.__init__(self, game)

        self.init_buttons()

        #canvas
        self.canva = Canva()

        #background
        self.background = Animation("main/images/background.png", 1280,720,1,60)

        #enemies
        self.enemy_spawner = EnemySpawner(1000, 70) #coordinate of spawner

        #tower
        self.tower = Animation("main/images/tower.png",225,500,1,60)

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
                    self.enemy_spawner.check_kill(Y_pred)
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
        display.fill((255,255,255))

        #draw background first
        self.background.render(display, 0, 0)
        #render buttons
        self.back_btn.render(display)
        #render canva
        self.canva.render(display)
        #render tower
        self.tower.render(display, 10, 100)
        #render enemies
        self.enemy_spawner.render(display)
        
        