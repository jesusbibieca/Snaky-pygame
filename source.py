import pygame, time, random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,225)
yellow = (185,185,0)

displayWidth = 800
displayHeight = 600

gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption ("Snaky!")

blockSize = 10
FPS = 15

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 25)

def snakeLenght(blockSize, snakeList):
	for XnY in snakeList:
		pygame.draw.rect(gameDisplay, black, [XnY[0], XnY[1], blockSize, blockSize])

def screenMessage(msg, color):
	screenText = font.render(msg, True, color)
	gameDisplay.blit(screenText, [displayWidth / 2, displayHeight / 2])
	pygame.display.update()
def gameLoop():

	leader_x = displayWidth / 2
	leader_y = displayHeight / 2
	leader_x_change = 0
	leader_y_change = 0

	snakeList = []
	snakeSize = 1

	randAppleX = round (random.randrange(0, displayWidth - blockSize)/10.0) * 10.0
	randAppleY = round (random.randrange(0, displayHeight - blockSize)/10.0) * 10.0

	gameExit = False
	gameOver = False

	while not gameExit:

		while gameOver == True:
			gameDisplay.fill(white)
			screenMessage("Game over, press C to play again or Q to quit", red)
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameDisplay.fill(white)
						pygame.display.update()
						gameOver = False
						gameExit = True
					if event.key == pygame.K_c:
						gameLoop()



		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					leader_x_change = -blockSize
					leader_y_change = 0
				elif event.key == pygame.K_RIGHT:
					leader_x_change = blockSize
					leader_y_change = 0
				elif event.key == pygame.K_UP:
					leader_y_change = -blockSize
					leader_x_change = 0
				elif event.key == pygame.K_DOWN:
					leader_y_change = blockSize
					leader_x_change = 0		

		if leader_x < 0 or leader_x >= displayWidth or leader_y < 0 or leader_y >= displayHeight:
			gameOver = True

		leader_x += leader_x_change
		leader_y += leader_y_change

		gameDisplay.fill(white)
		pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, blockSize, blockSize])
				
		snakeHead = []
		snakeHead.append(leader_x)
		snakeHead.append(leader_y)
		snakeList.append(snakeHead)

		if len (snakeList) > snakeSize:
			del snakeList[0]

		for eachSegment in snakeList[:-1]:
			if eachSegment == snakeHead:
				gameOver = True

		snakeLenght(blockSize, snakeList)

		pygame.display.update()

		if leader_x == randAppleX and leader_y == randAppleY:
			randAppleX = round (random.randrange(0, displayWidth - blockSize)/10.0) * 10.0
			randAppleY = round (random.randrange(0, displayHeight - blockSize)/10.0) * 10.0
			snakeSize += 1

		clock.tick(FPS)

	pygame.QUIT
	quit()

gameLoop()