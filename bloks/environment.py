import pygame
import sys
from tkinter import messagebox

class env():
    def __init__(self, level):
        self.placements = {
            "2" : [[200, 600, 100, 100], [0, 700, 1000, 100], [300, 500, 100, 200]
        , [400, 400, 100, 300], [600, 400, 200, 100], [900, 300, 100, 100]]
        , "3" : [[0, 700, 1000, 100], [400, 400, 100, 300], [600, 400, 200, 100], [900, 300, 100, 100], [600, 200, 200, 100]]
        , "1" : [[0, 700, 1000, 100]]
        , "4" : [[0, 700, 200, 50], [300, 600, 200, 50], [550, 150, 50, 400]]
        }
        self.goal_img = pygame.image.load('assets/endflag.png')
        self.floor_img = pygame.image.load('assets/floors.png')
        self.goal = pygame.transform.scale(self.goal_img, (50, 50))
        self.goals = {"2" : [900, 250]
                      ,"3" : [700, 150]
                      ,"1" : [900, 650]
                      , "4" : [900, 650]}
        self.level = level
        if self.placements.get(str(self.level)) == None:
            pygame.quit()
            messagebox.showinfo(message="You have reached the end of the game; Thank you for playing!")
            sys.exit()


    def draw(self, window=pygame.display):
        levellod = self.placements.get(str(self.level))
        for box in range(0, len(levellod)):
            lis = list()
            lis.append(self.placements.get(str(self.level))[box])
            ulis = lis[0]
            floor = pygame.transform.scale(self.floor_img, (ulis[2], ulis[3]))
            window.blit(floor, [ulis[0], ulis[1]])
        window.blit(self.goal, self.goals.get(str(self.level)))
    
    def envcollide(self, plrx, plrbasey):
        print(self.level)
        levellod = self.placements.get(str(self.level))
        for box in range(0, len(levellod)):
            rect = pygame.Rect(levellod[box])
            if rect.collidepoint(plrx, plrbasey):
                return True
        return False
    
    def finishlevel(self, plrx, plry):
        self.goal_rect = self.goal.get_rect()
        self.goal_rect.x = self.goals.get(str(self.level))[0]
        self.goal_rect.y = self.goals.get(str(self.level))[1]
        if self.goal_rect.collidepoint(plrx, plry):
            self.level =+ 1
            print(self.level)
            return True

        return False
