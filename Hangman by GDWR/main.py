# Simple HangMan with GUI
# By GDWR

from tkinter import *
import pygame
import random
import time


# <-----------------------------------Screen Setup----------------------------------->
pygame.init()
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption('Hangman by GDWR')

# <--------------------------------------Sprites-------------------------------------->
font = pygame.font.Font('sprites/font.ttf', 72)
font2 = pygame.font.Font('sprites/font.ttf', 32)
keyboard = (pygame.image.load('sprites/keyboard.png'))
easyImg = (pygame.image.load('sprites/easy.png'))
mediumImg = (pygame.image.load('sprites/medium.png'))
hardImg = (pygame.image.load('sprites/hard.png'))
underline = (pygame.image.load('sprites/underline.png'))
cross = (pygame.image.load('sprites/cross.png'))

# <-------------------------------------Variables------------------------------------->
counterX = 0
letterPosX = []
mx,my = pygame.mouse.get_pos()
stage = 0
mode = ''
check = False


# <------------------------------------Initial Loop----------------------------------->
#  gets co-ords on sheet.png for each letter, saves them in arry letterPosX[]
while counterX < 27:
	posX1 = counterX * 49
	letterPosX.append(posX1)
	counterX += 1
letterPosX = list(map(int, letterPosX))



# <-------------------------------------Class and Funcs------------------------------------->
class game:
	# cut "sheet.png" into area for letters, x = coord for letter assigned by letterPosX
	def get_image(x):
		""" Grab a single image out of a larger spritesheet
			Pass in the x, y location of the sprite
			and the width and height of the sprite. """

		sprites = pygame.image.load("sprites/sheet.png").convert()
		# Create a new blank image
		image = pygame.Surface([48, 78]).convert()

		# Copy the sprite from the large sheet onto the smaller image
		image.blit(sprites, (0, 0), (x, 0, 48, 78))

		image.set_colorkey((255, 255, 255))

		# Return the image
		return image

	# cuts "hangSheet.png" ubti areas for each stage.
	def get_stage(x):
		""" Grab a single image out of a larger spritesheet
			Pass in the x, y location of the sprite
			and the width and height of the sprite. """
			# stageImg = game.get_stage(letterP[u])

		sprites = pygame.image.load("sprites/hangSheet.png").convert()
		# Create a new blank image
		image = pygame.Surface([148, 177]).convert()

		# Copy the sprite from the large sheet onto the smaller image
		image.blit(sprites, (0, 0), (x, 0, 148, 177))

		image.set_colorkey((255, 255, 255))

		# Return the image
		return image

	# gets random word based on difficulty; easy, medium and hard
	def randWord(difficulty):
		tempList = open(difficulty).read().splitlines()
		game.word = random.choice(tempList)
		game.mainGame(difficulty, game.word)

	# loads base sprites for game, x = mode/difficulty, y = word to be guessed
	def mainGame(x, y):
		if y == 'aaaa':
			screen.fill((210, 180, 140))
			screen.blit(keyboard, (250, 600))
			pygame.display.update()
			game.randWord('word_' + x + '.txt')
			game.lettersGuessed = []

		else:
			underlineX = 500
			underlineY = 550
			underlineX2 = 500
			underlineY2 = 550
			game.alt = False
			game.underlinePos = []

			# Draws a line for each letter in the word
			for z in y:
				if game.alt == False:
					screen.blit(underline, (underlineX, underlineY))
					game.underlinePos.append(underlineX)
					underlineX += 68
					game.alt = True

				elif game.alt == True:
					underlineX2 += -68
					screen.blit(underline, (underlineX2, underlineY))
					game.underlinePos.append(underlineX2)
					game.alt = False

			pygame.display.update()

	# start screen to pick difficulty, draws things to the screen
	def gameSelect():
		#screen colour / background colour
		screen.fill((210, 180, 140))
		if game.notFirst == True:
			endText = font2.render(game.endTxt, False, (0, 0, 0))
			screen.blit(endText, (400, 200))
			if game.win == True:
				winnerText = font2.render("You win!", False, (1, 50, 32))
				screen.blit(winnerText, (450, 100))
			if game.win == False:
				winnerText = font2.render("You lose!", False, (	139, 0, 0))
				screen.blit(winnerText, (450, 100))

		textGameSelect = font.render('Pick a difficulty!', False, (0, 0, 0))
		screen.blit(textGameSelect, (275, 350))
		screen.blit(easyImg, (100, 500))
		screen.blit(mediumImg, (400, 500))
		screen.blit(hardImg, (700, 500))
		pygame.display.update()

	# converts a letter to int, a = 0, b = 1, c = 2 .... z = 25
	def letterToInt(letter):
		alphabet = list('abcdefghijklmnopqrstuvwxyz')
		return alphabet.index(letter)

	def drawStage():
		y = len(game.wrongLettersGuessed)
		if y == 1:
			n = 0
			stageImg = game.get_stage(n)
			screen.blit(stageImg, (425, 175))
			pygame.display.update()
		elif y >= 2 and y <= 8:
			z = y * 150
			n = z - 150
			stageImg = game.get_stage(n)
			screen.blit(stageImg, (425, 175))
			pygame.display.update()
		elif y > 8:
			game.end()
			game.win = False

	def crossLetter(letter, index):
		if not index:
			game.wrongLettersGuessed.append(letter)
			game.drawStage()
		else:
			for a in index:
				game.underlinePos.sort()
				x = game.underlinePos[a]
				u = game.letterToInt(letter)

				letterImg = game.get_image(letterPosX[u])
				game.score += 1
				screen.blit(letterImg, (x, 468))
				if game.score == len(game.word):
					game.end()
					game.win = True
		pygame.display.update()

	# Checks if the letter clicked is in the word
	def checkLetterInWord(letter):
		game.l = []
		if letter in game.lettersGuessed:
			print('already tried')
		else:
			if letter in game.word:
				game.lettersGuessed.append(letter)
				for index, char in enumerate(game.word):
					if char == letter:
						game.l.append(index)
				game.crossLetter(letter, game.l)
			else:
				game.lettersGuessed.append(letter)
				game.crossLetter(letter, game.l)

	# Checks what letter is clicked x = mousePos on click. i = letter of clicked
	# interates through areas to find which letter was clicked then prints it for now
	def clickCheck(x, y):
		if y == 0:
			tempX = 254
			tempX2 = 302
			add = 61
			list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

		if y == 1:
			tempX = 254
			tempX2 = 302
			add = 61
			list = ['j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r']

		if y == 3:
			tempX = 258
			tempX2 = 306
			add = 68
			list = ['s', 't', 'u', 'v', 'w', 'x', 'y', 'z']

		for i in list:
			if x >= tempX and x <= tempX2:
				if y == 0:
					screen.blit(cross, (tempX, 604))
					game.checkLetterInWord(i)
				if y == 1:
					screen.blit(cross, (tempX, 695))
					game.checkLetterInWord(i)
				if y == 3:
					screen.blit(cross, (tempX, 787))
					game.checkLetterInWord(i)
				break
			else:
				tempX += add
				tempX2 += add

	def end():
		game.endTxt = "The word was: " + str(game.word)
		print('The word was: ' + game.word)
		game.difSelected = False
		game.guessing = False
		game.gameSelect()
		game.word = 'aaaa'
		game.notFirst = True
		game.wrongLettersGuessed = []
		game.score = 0

# <-------------------------------------Inital Game Vars------------------------------------->

game.difSelected = False
game.guessing = False
game.word = 'aaaa'
game.wrongLettersGuessed = []
game.notFirst = False
game.win = False
game.score = 0

# <-------------------------------------Game Loop------------------------------------->

running = True
while running:

	if game.difSelected == False:
		game.gameSelect()

	#keeps track of mouse pos
	mx,my = pygame.mouse.get_pos()

	# #draws current state of game
	# loadSprites(stage)

	#checks for game event
	for event in pygame.event.get():

		#checks if game closed
		if event.type == pygame.QUIT:
			running = False
			pygame.display.quit()
			pygame.quit()

		#checks what difficulty is selected on start
		if event.type == pygame.MOUSEBUTTONDOWN and game.difSelected == False:
			pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
			#checks if clicked rock
			if mx >= 100 and mx <= 300 and my >= 500 and my <= 600: #clicks easy
				mode = 'easy'
				game.difSelected = True
				game.guessing = True
				game.mainGame(mode, game.word)
			if mx >= 400 and mx <= 600 and my >= 500 and my <= 600: #clicks medium
				mode = 'medium'
				game.difSelected = True
				game.guessing = True
				game.mainGame(mode, game.word)
			if mx >= 700 and mx <= 900 and my >= 500 and my <= 600: #clicks hard
				mode = 'hard'
				game.difSelected = True
				game.guessing = True
				game.mainGame(mode, game.word)
			pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)

		if event.type == pygame.MOUSEBUTTONDOWN and game.guessing == True:
			pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
			if mx >= 254 and mx <= 790 and my >= 604 and my <= 682: # clicks on keyboard 1st line
				game.clickCheck(mx, 0)
			if mx >= 254 and mx <= 790 and my >= 695 and my <= 773: # clicks on keyboard 2nd line
				game.clickCheck(mx, 1)
			if mx >= 258 and mx <= 782 and my >= 787 and my <= 865: # clicks on keyboard 3rd line
				game.clickCheck(mx, 3)
			pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
