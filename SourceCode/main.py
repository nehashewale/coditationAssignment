import pygame
import sys
from game_window_class import*

w = 800
h = 800
backround = (199,199,199)
FPS = 60

def get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
                 
                

def update():
    game_window.update()

def draw():
    window.fill(backround)
    game_window.draw()
                
def mouse_on_grid(pos):
    if pos[0] > 100 and pos[0] < w-100:
        if pos[1] > 90 and pos[1] < h-20:
            return True 
    return False
def click_cell(pos):
    # print("click")
    grid_pos = [pos[0]-100,pos[1]-90] 
    grid_pos[0] = grid_pos[0]//20
    grid_pos[1] = grid_pos[1]//20
    if game_window.grid[grid_pos[1]][grid_pos[0]].alive:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = False
    else:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = True
        
    

pygame.init()
window = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()
game_window = Game_window(window,100,90 )
running = True

while running:
    get_events()
    update()
    draw()
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
sys.exit()

