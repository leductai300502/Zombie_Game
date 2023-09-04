import pygame
import random
from Classes.GameDefine import Constants
from Classes.SoundEffect import SoundEffect


class  Game(object):
    def __init__(self) -> None:
        self.win = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))

        pygame.display.set_caption(Constants.GAME_TITLE)

        #Load Image Start Game
        self.start = pygame.image.load(Constants.IMAGE_START)

        #Load Image Background
        self.bg = pygame.image.load(Constants.IMAGE_BG)

        #Load Image GameOver
        self.stop_game = pygame.image.load(Constants.IMAGE_GAMEOVER)

        #Load Image Try Again
        self.tryAgain = pygame.image.load(Constants.IMAGE_BUTTON_1)
        self.tryAgainHover = pygame.image.load(Constants.IMAGE_BUTTON_2)
 
        #Load Image Hole
        self.Hole = pygame.image.load(Constants.IMAGE_HOLE)

        #Defind Hole Size
        self.Hole = pygame.transform.scale(self.Hole, (100,100 ))
        self.image_rect = self.Hole.get_rect()

        #Defind Font
        self.fontObj = pygame.font.Font(Constants.FONT_NAME, Constants.FONT_SIZE)

        #Load Image Pointer
        self.cursor_img = pygame.image.load(Constants.IMAGE_HAMMER)

        #Defind Pointer Size
        self.cursor_img = pygame.transform.scale(self.cursor_img, (60, 60))

        #Hide Default Pointer
        pygame.mouse.set_visible(False)

        #List Frame Animation Of Zombie
        zombieSpriteSheet = pygame.image.load(Constants.IMAGE_ZOMBIE)
        self.zombieImage = []
        self.zombieImage.append(zombieSpriteSheet.subsurface(Constants.ZOM_SPRITE_1))
        self.zombieImage.append(zombieSpriteSheet.subsurface(Constants.ZOM_SPRITE_2))
        self.zombieImage.append(zombieSpriteSheet.subsurface(Constants.ZOM_SPRITE_3))
        self.zombieImage.append(zombieSpriteSheet.subsurface(Constants.ZOM_SPRITE_4))
        self.zombieImage.append(zombieSpriteSheet.subsurface(Constants.ZOM_SPRITE_5))
        self.zombieImage.append(zombieSpriteSheet.subsurface(Constants.ZOM_SPRITE_6))

        self.sound = SoundEffect()

    ##################################################################################
        #Mouse Setting
        self.rotate_cursor = False
        self.isHit = False
        self.hits = 0
        self.miss = 0
        self.count = 0

        #Timer Settting
        self.Timer_Flag = True
        self.count_Timer = 0
        self.max = 60

        #Update Animation
        self.walkCount = 0
        self.update_animation = False
        self.random_hole = 0
        self.zombie_alive = True

        #Running Game Setting
        self.run = True
        self.fail_count = -1
        self.stop = False

        #FPS
        self.clock = pygame.time.Clock()
    ##################################################################################

        

    def redrawGameWindow(self):
        self.win.blit(self.bg,(0,0))
        for element in Constants.LIST_HOLE:
            self.win.blit(self.Hole,element)

        #update hit of player
        currentHitString = "HIT - " + str(self.hits)
        hitText = self.fontObj.render(currentHitString, True, (255,0,0))
        self.win.blit(hitText, (100,50)) 

        #update miss of player
        currentMissString = "MISS - " + str(self.miss)
        MissText = self.fontObj.render(currentMissString, True, (255,0,0))
        self.win.blit(MissText, (300,50))

        #update live of player
        currentLiveString = "LIVE - " + str(3 - self.fail_count)
        LiveText = self.fontObj.render(currentLiveString, True, (255,0,0))
        self.win.blit(LiveText, (600,50))
    ##################################################################################
    def updateZombie(self):

        if self.walkCount + 1 <= 18:
            self.win.blit(self.zombieImage[self.walkCount//6],Constants.LIST_HOLE[self.random_hole])
            self.walkCount +=1 
        else:
            if self.isHit == False:
                self.win.blit(self.zombieImage[2],Constants.LIST_HOLE[self.random_hole])
    ##################################################################################
    def levelUp(self):
        print("hehe")                
    ##################################################################################
    def Timer(self):
        self.count_Timer += 1
        if self.count_Timer > self.max:
            self.Timer_Flag = True
            self.count_Timer = 0
    ##################################################################################
    def generateZombie(self):       
        if self.zombie_alive == True:
            self.fail_count += 1
            if self.fail_count >= 3:
                self.stop = True
                self.update_animation = False
                self.fail_count = 0
        
        self.random_hole = random.randint(0,7)
        self.image_rect.center = Constants.LIST_HOLE[self.random_hole]
        self.walkCount = 0
        self.update_animation = True
        self.Timer_Flag = False
        self.zombie_alive = True
    ##################################################################################
    def hitZombie(self):
        if self.walkCount + 1 <= 36:
            self.win.blit(self.zombieImage[self.walkCount//6],Constants.LIST_HOLE[self.random_hole])
            self.walkCount +=1 
            self.count_Timer -= 1
        else:
            self.isHit = False
            self.count_Timer = 60
    ##################################################################################
    def endScreen(self):
        self.win.blit(self.stop_game,(0,0))
        self.win.blit(self.tryAgain, (278, 509))
        #update hit of player
        currentHitString =  str(self.hits)
        hitText = self.fontObj.render(currentHitString, True, (255,0,0))
        self.win.blit(hitText, (311, 364)) 
        #update miss of player
        currentMissString = str(self.miss)
        MissText = self.fontObj.render(currentMissString, True, (255,0,0))
        self.win.blit(MissText, (580, 364))
        #update score of player
        currentScoreString =  str(self.hits)
        scoreText = self.fontObj.render(currentScoreString, True, (255,0,0))
        self.win.blit(scoreText, (507, 444))

        mouseX, mouseY = pygame.mouse.get_pos()
        if mouseX >= 278 and mouseX <= 557 and mouseY >= 480 and mouseY <= 539:
            self.win.blit(self.tryAgainHover, (278, 509))
    ##################################################################################
    def mouseControl(self):
        if self.rotate_cursor:
                self.rotated_cursor = pygame.transform.rotate(self.cursor_img, Constants.HAMMER_ANGLE)
                self.win.blit(self.rotated_cursor, pygame.mouse.get_pos())
        else:
            self.win.blit(self.cursor_img, pygame.mouse.get_pos())


        if self.rotate_cursor and Constants.HAMMER_ANGLE != 0:
            self.count += 1
            if(self.count == 10):
                self.rotate_cursor = False
                self.count = 0

    ####################################################################################
    def Start(self):
        #####################################################################
        # Game Start Menu
        begin = True
        button0 = pygame.image.load(Constants.IMAGE_BUTTON_0)
        button0_hover = pygame.image.load(Constants.IMAGE_BUTTON_0_HOVER)
        
        button0_hover_rect = button0.get_rect()
        button0_hover_rect.center = (527,352)

        while begin:
            self.win.blit(self.start,(0,0))
            self.win.blit(button0,(527,352))

            mouseX, mouseY = pygame.mouse.get_pos()
            if mouseX >= 527 and mouseX <= 794 and mouseY >= 352 and mouseY <= 406:
                self.win.blit(button0_hover, (527, 352))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    begin = False
                    self.run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.rotate_cursor = True
                    self.sound.playMissSound()
                    if button0_hover_rect.collidepoint(mouse_pos):
                        begin = False                    

            self.mouseControl()

            pygame.display.update()
        #End Game Start Menu 
        #####################################################################
        ##                                                                 ##
        ##                                                                 ##
        #####################################################################
        #Before Game Play
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.rotate_cursor = True
                    self.sound.playMissSound() 
                    mouseX, mouseY = pygame.mouse.get_pos()
                    if mouseX >= 278 and mouseX <= 557 and mouseY >= 480 and mouseY <= 539:
                        self.stop = False
                        self.count_Timer = 0
                        self.max = 60
                        self.hits = 0
                        self.miss = 0
                        
                    if self.image_rect.collidepoint(mouse_pos) and self.isHit == False:
                        if self.max > 15:
                            self.max -= 1
                        if self.count_Timer != 0:
                            self.isHit = True
                            self.hits += 1
                            self.zombie_alive = False
                            self.sound.playHitSound()
                    else:
                        self.miss += 1
            if self.stop == False: 
                #Handle Game Windown
                self.redrawGameWindow()

                #Handle Generate Zombie
                if self.Timer_Flag == True:
                    self.generateZombie()

                #Handle Hit Zombie
                if self.isHit == True:
                    self.hitZombie()

                #Handle Update New Animation Zombie
                if self.update_animation:
                    self.updateZombie()
                
                #Timer Of Game
                self.Timer()
            else:
                self.endScreen()

            self.mouseControl() 

            pygame.display.update()
            self.clock.tick(30)
        #End Game Start Menu 
        #####################################################################
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
pygame.init()
man = Game()
man.Start()
pygame.quit()