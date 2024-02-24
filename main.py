import pygame
import math
from bloks.environment import env

pygame.init()

class main():
    def __init__(self):
        self.inputs = [False, False, False]
        self.window = pygame.display.set_mode((1000, 800))
        self.clock = pygame.time.Clock()
        self.jump = False
        self.fallcount = 0
        self.jumppw = 0
        plr_img = pygame.image.load('assets/player.png')
        wtrmark_img = pygame.image.load('assets/wtrmark.png')
        self.plr_poz = [100, 200]
        self.plr = pygame.transform.scale(plr_img, (50, 50))
        self.wtrmark = pygame.transform.smoothscale(wtrmark_img, (300, 75))
        self.plr_hb = self.plr.get_rect()
        self.jumpmovs = 0
        self.level = 1

    def run(self):

        while True:
            if self.inputs[1] - self.inputs[0] == -1:
                if not env(self.level).envcollide(self.plr_poz[0], self.plr_poz[1]) and not env(self.level).envcollide(self.plr_poz[0], self.plr_poz[1] + 48):
                    self.plr_poz[0] -= 5
            if self.inputs[1] - self.inputs[0] == 1:
                if not env(self.level).envcollide(self.plr_poz[0] + 50, self.plr_poz[1]) and not env(self.level).envcollide(self.plr_poz[0] + 50, self.plr_poz[1] + 48):
                    self.plr_poz[0] += 5
            if env(self.level).envcollide(self.plr_poz[0], self.plr_poz[1]):
                self.plr_poz[0] += 5
            if env(self.level).envcollide(self.plr_poz[0] + 45, self.plr_poz[1]):
                self.plr_poz[0] -= 5
            self.clock.tick(60)
            self.window.fill((200, 200, 200))
            self.window.blit(self.wtrmark, (350, 50))
            env(self.level).draw(self.window)
            self.window.blit(self.plr, self.plr_poz)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.inputs[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.inputs[1] = True
                    if event.key == pygame.K_UP:
                        self.inputs[2] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.inputs[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.inputs[1] = False
                    if event.key == pygame.K_UP:
                        self.inputs[2] = False

            if not env(self.level).envcollide(self.plr_poz[0] + (self.plr.get_width()), self.plr_poz[1] + self.plr.get_height()) and not env(self.level).envcollide(self.plr_poz[0], self.plr_poz[1] + self.plr.get_height()):
                if not self.jump:
                    self.plr_poz[1] += 5
                    self.fallcount += 1
                    if self.fallcount == 240:
                        self.plr_poz = [50, 50]
            else:
                self.fallcount = 0
                if self.inputs[2] == True:
                    self.jump = True
                    self.jumppw = 100
                    self.jumpmovs = 0
            
            if self.jump:
                
                if not env(self.level).envcollide(self.plr_poz[0] + 25, self.plr_poz[1]):
                    self.plr_poz[1] -=  int(self.jumppw / 5)
                self.jumppw -= int(self.jumppw / 5)
                self.jumpmovs += 1
                
                if self.jumpmovs == 20:
                    self.jump = False
                    self.plr_poz[1] = math.trunc(self.plr_poz[1] / 5) * 5

            if env(self.level).finishlevel(self.plr_poz[0] + 25, self.plr_poz[1] + 25):
                self.plr_poz = [50, 50]
                self.level = self.level + 1
                print("level finished")

            pygame.display.update()
game = main()
game.run()