# Simple Rock Paper Scissors with GUI
# By GDWR
# https://github.com/GDWR

import pygame
import random
import time

#screen setup
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('RPS by GDWR')


#load sprites
comp_r = (pygame.image.load('sprites/comp_r.png'))
comp_p = (pygame.image.load('sprites/comp_p.png'))
comp_s = (pygame.image.load('sprites/comp_s.png'))
player_r = (pygame.image.load('sprites/player_r.png'))
player_p = (pygame.image.load('sprites/player_p.png'))
player_s = (pygame.image.load('sprites/player_s.png'))
winImg = (pygame.image.load('sprites/win.png'))
drawImg = (pygame.image.load('sprites/draw.png'))
lossImg = (pygame.image.load('sprites/loss.png'))

#list of RPS choices for computer
list = ['Rock', 'Paper', 'Scissors']


#starting Hand Placement // Finish pos = 200, 325
rock_x = 0
rock_y = 350
paper_x = 200
paper_y = 350
scissors_x = 400
scissors_y = 350

#inital mouse positions
mx,my = pygame.mouse.get_pos()

#resets all positions
def restart():
    rock_x = 0
    rock_y = 350
    screen.blit(player_r, (rock_x, rock_y))
    paper_x = 200
    paper_y = 350
    screen.blit(player_p, (paper_x, paper_y))
    scissors_x = 400
    scissors_y = 350


#draws starting hand positions
onScreen = False
compState = False

def drawHands():
    screen.fill((128, 128, 128))
    screen.blit(player_s, (scissors_x, scissors_y))
    screen.blit(player_p, (paper_x, paper_y))
    screen.blit(player_r, (rock_x, rock_y))
    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
    pygame.display.update()



#computer chose rock
def compRock(compState):
    if compState == False:
        screen.blit(comp_r, (200, 0))
        compState = True


#computer chose paper
def compPaper(compState):
    if compState == False:
        screen.blit(comp_p, (200, 0))
        compState = True


#computer chose scissors
def compScissors(compState):
    if compState == False:
        screen.blit(comp_s, (200, 0))
        compState = True



#player chose rock
def playerRock():
    screen.blit(player_r, (200, 325))
#player chose paper
def playerPaper():
    screen.blit(player_p, (200,325))
#player chose scissors
def playerScissors():
    screen.blit(player_s, (200,325))

#draws win/draw/loss on screen
wx = 200
wy = 200

def playerWin():
    screen.blit(winImg, (wy, wx))
    pygame.display.update()
    time.sleep(5)



def playerDraw():
    screen.blit(drawImg, (wx, wy))
    pygame.display.update()
    time.sleep(5)



def playerLoss():
    screen.blit(lossImg, (wx, wy))
    pygame.display.update()
    time.sleep(5)




#game loop
running = True
while running:

    #screen colour / background colour
    screen.fill((128, 128, 128))


    #Checks if player hands are on screen, if not it draws them
    if onScreen == False:
        drawHands()
        compState = False
        onScreen = True


    #gets mouse positions
    mx,my = pygame.mouse.get_pos()

    #gets game events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #checks if game closed
            running = False

        #checks if mousebutton is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
            #checks if clicked rock
            if mx >= 0 and mx <= 100 and my >= 350 and my <= 500:


                #random rps for computer
                compchoice = random.choice(list)
                choice = 'Rock'

                #check if win
                if compchoice == 'Rock':
                    compRock(compState)
                    playerRock()
                    playerDraw()
                    drawHands()
                elif compchoice == 'Scissors':
                    compScissors(compState)
                    playerRock()
                    playerWin()
                    drawHands()
                elif compchoice == 'Paper':
                    compPaper(compState)
                    playerRock()
                    playerLoss()
                    drawHands()


            #checks if clicked paper
            if mx >= 190 and mx <= 350 and my >= 350 and my <= 500:

                #random rps for computer
                compchoice = random.choice(list)
                choice = 'Paper'

                #check if win
                if compchoice == 'Rock':
                    compRock(compState)
                    playerPaper()
                    playerWin()
                    drawHands()
                elif compchoice == 'Scissors':
                    compScissors(compState)
                    playerPaper()
                    playerLoss()
                    drawHands()
                elif compchoice == 'Paper':
                    compPaper(compState)
                    playerPaper()
                    playerDraw()
                    drawHands()

            #checks if clicked scissor
            if mx >= 390 and mx <= 500 and my >= 350 and my <= 500:
    
                #random rps for computer
                compchoice = random.choice(list)
                choice = 'Scissors'

                #Check if win
                if compchoice == 'Rock':
                    compRock(compState)
                    playerScissors()
                    playerLoss()
                    drawHands()
                elif compchoice == 'Scissors':
                    compScissors(compState)
                    playerScissors()
                    playerDraw()
                    drawHands()
                elif compchoice == 'Paper':
                    compPaper(compState)
                    playerScissors()
                    playerWin()
                    drawHands()
