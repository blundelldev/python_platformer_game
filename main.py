import pygame
import math
from bloks.environment import env

pygame.init()

class main():
    def __init__(self, player_img):
        self.inputs = [False, False, False]
        self.window = pygame.display.set_mode((1000, 800))
        self.clock = pygame.time.Clock()
        self.jump = False
        self.fallcount = 0
        self.jumppw = 0
        pygame.joystick.init()
        plr_img = pygame.image.load(player_img)
        wtrmark_img = pygame.image.load('assets/wtrmark.png')
        self.plr_poz = [100, 200]
        self.plr = pygame.transform.scale(plr_img, (50, 50))
        self.wtrmark = pygame.transform.smoothscale(wtrmark_img, (300, 75))
        self.plr_hb = self.plr.get_rect()
        self.jumpmovs = 0
        self.level = 1
        pygame.display.set_icon(plr_img)
        pygame.display.set_caption('Platformer')

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
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.inputs[0] = True
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.inputs[1] = True
                    if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_SPACE:
                        self.inputs[2] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.inputs[0] = False
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.inputs[1] = False
                    if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_SPACE:
                        self.inputs[2] = False

            if not env(self.level).envcollide(self.plr_poz[0] - 5, self.plr_poz[1] + self.plr.get_height()) and not env(self.level).envcollide(self.plr_poz[0] + 50, self.plr_poz[1] + self.plr.get_height()):
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

            if env(self.level).finishlevel(self.plr_poz[0], self.plr_poz[1] + 25) or env(self.level).finishlevel(self.plr_poz[0] + 50, self.plr_poz[1] + 25):
                self.plr_poz = [50, 50]
                self.level = self.level + 1

            pygame.display.update()

plr_image = input("choose a enter the number from this key to choose character skin:\n 1 = crazy triangle\n 2 = toon cube\n --")
print('hope you enjoy the game')
if plr_image == "1":
    plr_image = 'assets/player.png'
elif plr_image == "2":
    plr_image = 'assets/toonsquare.png'
else:
    print('you seem to have entered an invalid name, you may have also entered a different directory')
game = main(plr_image)
game.run()