import pygame
import random
class Cell:
    def __init__(self,surface,grid_x,grid_y):
        self.alive = False   
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.image = pygame.Surface((20,20))
        self.rect = self.image.get_rect()
        self.surface = surface
        self.neighbours = []
    def update(self):
        self.rect.topleft = (self.grid_x*20,self.grid_y*20)
    
    def draw(self):
        if self.alive:
            self.image.fill((0,0,0))
        else:
            self.image.fill((0,0,0))
            pygame.draw.rect(self.image,(255,255,255),(1,1,18,18))
        self.surface.blit(self.image,(self.grid_x*20,self.grid_y*20))
    def get_nehghbours(self,grid):
        neighbour_list = [[1,1],[-1,-1],[-1,1],[1,-1],[0,-1],[0,1],[1,0],[-1,0]]
        for neighbour in neighbour_list:
            neighbour[0] += self.grid_x
            neighbour[1] += self.grid_y
        for neighbour in neighbour_list:
            if neighbour[0]< 0:
                neighbour[0] +=30
            if neighbour[1]< 0:
                neighbour[1] +=30
            if neighbour[1]>29:
                neighbour[1] -=30
            if neighbour[0]>29:
                neighbour[0] -=30
        # for nighbour in neighbour_list:
        #     self.neighbours.append(grid[]) 
        

            
                
                 
                
                
        
        
        