
import pygame
import os
import random
pygame.init()

os.system('cls')

#fps activator
clock = pygame.time.Clock()

win = pygame.display.set_mode((750, 750))
pygame.display.set_caption("Bomb Brawl")

muH = 1
muV = 1

while True:
	MU_11 = pygame.image.load('MU_11.png')
	MU_12 = pygame.image.load('MU_12.png')
	MU_21 = pygame.image.load('MU_21.png')
	MU_22 = pygame.image.load('MU_22.png')
	MU_31 = pygame.image.load('MU_31.png')
	MU_32 = pygame.image.load('MU_32.png')

	dl = 0
	dr = 0
	du = 0
	dd = 0

	loop = True
	while loop:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		keys = pygame.key.get_pressed()

		if keys[pygame.K_LEFT]:
			if dl == 0 and muH > 1:
				muH -= 1
			dl += 1
		else:
			dl = 0

		if keys[pygame.K_RIGHT]:
			if dr == 0 and muH < 2:
				muH += 1
			dr += 1
		else:
			dr = 0

		if keys[pygame.K_UP]:
			if du == 0 and muV > 1:
				muV -= 1
			du += 1
		else:
			du = 0

		if keys[pygame.K_DOWN]:
			if dd == 0 and muV < 3:
				muV += 1
			dd += 1
		else:
			dd = 0

		if keys[pygame.K_RETURN]:
			loop = False

		if muV == 1 and muH == 1:
			win.blit(MU_11, (0,0))

		if muV == 1 and muH == 2:
			win.blit(MU_12, (0,0))

		if muV == 2 and muH == 1:
			win.blit(MU_21, (0,0))

		if muV == 2 and muH == 2:
			win.blit(MU_22, (0,0))

		if muV == 3 and muH == 1:
			win.blit(MU_31, (0,0))

		if muV == 3 and muH == 2:
			win.blit(MU_32, (0,0))

		pygame.display.update()





	if muV == 1 and muH == 1: 
		#import images
		BG = pygame.image.load('BG.png')
		RR = [pygame.image.load('RR_01.png'), pygame.image.load('RR_02.png'), pygame.image.load('RR_03.png'), pygame.image.load('RR_04.png'), pygame.image.load('RR_05.png'), pygame.image.load('RR_06.png'), pygame.image.load('RR_07.png'), pygame.image.load('RR_08.png')]
		RL = [pygame.image.load('RL_01.png'), pygame.image.load('RL_02.png'), pygame.image.load('RL_03.png'), pygame.image.load('RL_04.png'), pygame.image.load('RL_05.png'), pygame.image.load('RL_06.png'), pygame.image.load('RL_07.png'), pygame.image.load('RL_08.png')]
		RI = pygame.image.load('RI_01.png')
		RW = pygame.image.load('RW_01.png')
		BR = [pygame.image.load('BR_01.png'), pygame.image.load('BR_02.png'), pygame.image.load('BR_03.png'), pygame.image.load('BR_04.png'), pygame.image.load('BR_05.png'), pygame.image.load('BR_06.png'), pygame.image.load('BR_07.png'), pygame.image.load('BR_08.png')]
		BL = [pygame.image.load('BL_01.png'), pygame.image.load('BL_02.png'), pygame.image.load('BL_03.png'), pygame.image.load('BL_04.png'), pygame.image.load('BL_05.png'), pygame.image.load('BL_06.png'), pygame.image.load('BL_07.png'), pygame.image.load('BL_08.png')]
		BI = pygame.image.load('BI_01.png')
		BW = pygame.image.load('BW_01.png')
		BME = [pygame.image.load('BME_01.png'), pygame.image.load('BME_02.png'), pygame.image.load('BME_03.png'), pygame.image.load('BME_04.png'), pygame.image.load('BME_05.png'), pygame.image.load('BME_06.png'), pygame.image.load('BME_07.png'), pygame.image.load('BME_08.png')]
		BM = pygame.image.load('BM_01.png')

		EXP = pygame.mixer.Sound('PEW.wav')
		POP = pygame.mixer.Sound('pling.wav')

		class player(object):
			def __init__(self, x, y, w, h):
				self.x = x
				self.y = y
				self.w = w
				self.h = h
				self.left = False
				self.right = False
				self.vel = 10
				self.walkCount = 0
				self.jump_nyc = 0
				self.jump_change = 3
				self.jumping = False
				self.xplat = [730]
				self.plat_below = []
				self.targ_plat = 730
				self.hasBomb = 3
				self.score = 0
				self.superjumpcount = 0
				self.superjumping = False

			def move_left(self):
				self.left = True
				self.right = False
				self.x -= self.vel

			def move_right(self):
				self.left = False
				self.right = True
				self.x += self.vel

			def falling(self):
				#check if falling
				if self.y != (self.targ_plat - 100) and not self.jumping:
					self.jumping = True
					self.jump_nyc = 0
					self.jump()

					print(self.y)
					print(self.targ_plat + 100)

			def jump(self):
				#check platforms at same x
				self.xplat = [730]
				if ((self.x + 13) >= plat_1.x) and ((self.x + 13) <= (plat_1.x + plat_1.w)):
					self.xplat.append(plat_1.y)

				if ((self.x + 13) >= plat_2.x) and ((self.x + 13) <= (plat_2.x + plat_2.w)):
					self.xplat.append(plat_2.y)

				if ((self.x + 13) >= plat_3.x) and ((self.x + 13) <= (plat_3.x + plat_3.w)):
					self.xplat.append(plat_3.y)

				if ((self.x + 13) >= plat_4.x) and ((self.x + 13) <= (plat_4.x + plat_4.w)):
					self.xplat.append(plat_4.y)

				if ((self.x + 13) >= plat_5.x) and ((self.x + 13) <= (plat_5.x + plat_5.w)):
					self.xplat.append(plat_5.y)

				self.plat_below = []
				for plat_val in self.xplat:
					if plat_val > (self.y + 99):
						self.plat_below.append(plat_val)
					
				#find nearst platform under player
				self.targ_plat = 1000
				for plat_val2 in self.plat_below:
					if self.targ_plat > plat_val2 :
						self.targ_plat = plat_val2

				if self.y != (self.targ_plat - 100) and not self.jumping:
					self.jumping = True
					self.jump_nyc = 0

				#check if about to land
				if self.jumping:
					if (self.y + 99) - self.jump_nyc > self.targ_plat:
						self.y = self.targ_plat - 100
						self.jumping = False
						self.superjumping = False

					if self.jumping == True:
						self.y -= self.jump_nyc
						self.jump_nyc -= self.jump_change

		#init players
		red = player(50, 600, 26, 100)
		blue = player(674, 600, 26, 100)

		class bomb(object):
			def __init__(self, x, y):
				self.x = x
				self.y = y
				self.nyc = 0
				self.fall_speed = 3
				self.explode = True
				self.exploding = 20

			def fall(self):
				#make bomb fall
				if self.y < 1000 and self.explode == False:
					self.y -= self.nyc
					self.nyc -= self.fall_speed

					#expload on floor
					if (self.y + self.nyc) > 727:
						self.y = 727
						
						EXP.play()

						self.explode = True
						self.exploding = 0

			def draw(self, win):
				#draw bomb
				if self.explode == False:
					win.blit(BM, (self.x - 50, self.y - 50))

				#draw explosion
				if self.explode == True and self.exploding < 16:
					win.blit(BME[self.exploding//2], (self.x - 50,self.y - 50))

					self.exploding += 1

		#init freeze
		freeze = False
		freeze_count = 0

		#init red and blue bomb
		rBomb = bomb(0, 1001)
		bBomb = bomb(0, 1001)

		plat_change = 1999
		set_plat_change = 320

		class plat(object):
			def __init__(self, x, y, w, h):
				self.x = x
				self.y = y
				self.w = w
				self.h = h
				self.place = 0
				self.colour = (0, 0, 0)

			def random(self):
				#randomize platfoarm locations
				self.place = random.randint(1, 5)
				
				if self.place == 1:
					self.x = 50
					self.y = 600

				if self.place == 2:
					self.x = 500
					self.y = 600

				if self.place == 3:
					self.x = 275
					self.y = 450

				if self.place == 4:
					self.x = 50
					self.y = 300

				if self.place == 5:
					self.x = 500
					self.y = 300

			def create(self, win):
				#draw platforms
				pygame.draw.rect(win, self.colour, (self.x, self.y, self.w, self.h))

		#init platforms
		plat_main = plat(0, 730, 750, 20)
		plat_1 = plat(0, 0, 200, 10)
		plat_2 = plat(0, 0, 200, 10)
		plat_3 = plat(0, 0, 200, 10)
		plat_4 = plat(0, 0, 200, 10)
		plat_5 = plat(0, 0, 200, 10)

		font_name = pygame.font.match_font('impact')
		#draw scores
		def red_text(surf, text, size, x, y, colour):
			font = pygame.font.Font(font_name, size)
			text_surface = font.render(text, True, (colour))
			text_rect = text_surface.get_rect()
			text_rect.topleft = (x, y)
			surf.blit(text_surface, text_rect)

		def blue_text(surf, text, size, x, y, colour):
			font = pygame.font.Font(font_name, size)
			text_surface = font.render(text, True, (colour))
			text_rect = text_surface.get_rect()
			text_rect.topright = (x, y)
			surf.blit(text_surface, text_rect)

		def draw():
			pygame.draw.rect(win, (255, 255, 255), (0, 0, 750, 750))

			#draw background
			win.blit(BG, (0,0))

			#red walk animation
			if red.walkCount + 1 >= 16:
					red.walkCount = 0

			if red.left and red.superjumping == False:
				win.blit(RL[red.walkCount//2], (red.x - 37,red.y))
				red.walkCount += 1

			elif red.right and red.superjumping == False:
				win.blit(RR[red.walkCount//2], (red.x - 37,red.y))
				red.walkCount += 1

			else:
				if red.superjumpcount >= 96 or red.superjumping == True:
					win.blit(RW, (red.x - 37,red.y))
				else:
					win.blit(RI, (red.x - 37,red.y))


			#blue walk animation
			if blue.walkCount + 1 >= 16:
					blue.walkCount = 0

			if blue.left and blue.superjumping == False:
				win.blit(BL[blue.walkCount//2], (blue.x - 37,blue.y))
				blue.walkCount += 1

			elif blue.right and blue.superjumping == False:
				win.blit(BR[blue.walkCount//2], (blue.x - 37,blue.y))
				blue.walkCount += 1

			else:
				if blue.superjumpcount >= 96 or blue.superjumping == True:
					win.blit(BW, (blue.x - 37,blue.y))
				else:
					win.blit(BI, (blue.x - 37,blue.y))

			#draw platforms
			plat_main.create(win)
			if (plat_change >= (set_plat_change - 4) and plat_change <= (set_plat_change - 2)) or (plat_change >= (set_plat_change - 10) and plat_change <= (set_plat_change - 7)) or (plat_change >= (set_plat_change - 18) and plat_change <= (set_plat_change - 14)) or (plat_change >= (set_plat_change - 28) and plat_change <= (set_plat_change - 23)) or (plat_change >= (set_plat_change - 40) and plat_change <= (set_plat_change - 34)) or (plat_change >= (set_plat_change - 54) and plat_change <= (set_plat_change - 47)) or (plat_change <= (set_plat_change - 62)):
				plat_1.create(win)
				plat_2.create(win)
				plat_3.create(win)
				plat_4.create(win)
				plat_5.create(win)

			#draw bombs
			rBomb.draw(win)
			bBomb.draw(win)

			#draw scores
			red_text(win, str(red.score), 30, 5, 5, (255, 0, 0))
			red_text(win, str(red.hasBomb), 20, 5, 35, (255, 0, 0))

			blue_text(win, str(blue.score), 30, 745, 5, (0, 0, 255))
			blue_text(win, str(blue.hasBomb), 20, 745, 35, (0, 0, 255))

			pygame.display.update()

		#main game loop
		loop = True
		while loop:
			#set fps
			clock.tick(32)

			#exit
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()

			keys = pygame.key.get_pressed()

			if freeze == False:

				if keys[pygame.K_b]:
					loop = False

				#move red
				if keys[pygame.K_a] and keys[pygame.K_d]:
					red.left = False
					red.right = False

				else:	
					if keys[pygame.K_a] and red.x >= red.vel:
						red.move_left()
						red.superjumpcount = 0

					elif keys[pygame.K_d] and (red.x + red.w) <= (750 - red.vel):
						red.move_right()
						red.superjumpcount = 0

					else:
						red.left = False
						red.right = False

						if red.y == 630:
							red.superjumpcount += 1

						else:
							red.superjumpcount = 0

				#move blue
				if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
					blue.left = False
					blue.right = False
				
				else:
					if keys[pygame.K_LEFT] and blue.x >= blue.vel:
						blue.move_left()
						blue.superjumpcount = 0

					elif keys[pygame.K_RIGHT] and (blue.x + blue.w) <= (750 - blue.vel):
						blue.move_right()
						blue.superjumpcount = 0

					else:
						blue.left = False
						blue.right = False

						if blue.y == 630:
							blue.superjumpcount += 1

						else:
							blue.superjumpcount = 0

				#red jump
				if (not red.jumping) and keys[pygame.K_w]:
					red.jumping = True
					if red.superjumpcount >= 96:
						red.jump_nyc = 60
						red.superjumping = True
					else:
						red.jump_nyc = 30

				#blue jump
				if (not blue.jumping) and keys[pygame.K_UP]:
					blue.jumping = True
					if blue.superjumpcount >= 96:
						blue.jump_nyc = 60
						blue.superjumping = True
					else:
						blue.jump_nyc = 30

				red.jump()
				blue.jump()

				#randomize platforms
				plat_change += 1
				if plat_change >= set_plat_change:
					plat_1.random()
					plat_2.random()
					plat_3.random()
					plat_4.random()
					plat_5.random()

					plat_change = 0

				#gives players bombs
				if red.y == 630:
					red.hasBomb = 3

				if blue.y == 630:
					blue.hasBomb = 3

				#red drop bomb
				if keys[pygame.K_s] and red.hasBomb > 0 and rBomb.exploding >= 16 and rBomb.explode == True and red.y < 460:
					rBomb.y = red.y + 100
					rBomb.x = red.x + 13

					rBomb.nyc = 0

					rBomb.exploding = 0
					rBomb.explode = False
					red.hasBomb -= 1

				#blue drop bomb
				if keys[pygame.K_DOWN] and blue.hasBomb > 0 and bBomb.exploding >= 16 and bBomb.explode == True and blue.y < 460:
					bBomb.y = blue.y + 100
					bBomb.x = blue.x + 13

					bBomb.nyc = 0

					bBomb.exploding = 0
					bBomb.explode = False
					blue.hasBomb -= 1

				#makes bombs fall
				rBomb.fall()
				bBomb.fall()

				#expload red bomb if hit blue player
				if rBomb.x >= blue.x - 37 and rBomb.x <= blue.x + 62 and rBomb.y >= blue.y + 25 and rBomb.y <= blue.y + 99 and rBomb.explode == False:
					rBomb.explode = True
					red.score += 1
					freeze = True
					POP.play()
					EXP.play()

				#expload blue bomb if hit red player
				if bBomb.x >= red.x - 37 and bBomb.x <= red.x + 62 and bBomb.y >= red.y + 25 and bBomb.y <= red.y + 99 and bBomb.explode == False:
					bBomb.explode = True
					blue.score += 1
					freeze = True
					POP.play()
					EXP.play()

			#freeze game if bomb hit player
			if freeze == True:
				freeze_count += 1

				if freeze_count == 32:
					freeze = False
					freeze_count = 0

					red.y = 600
					blue.y = 600
					red.x = 50
					blue.x = 674

					blue.jump_nyc = 0
					red.jump_nyc = 0

			#draw game
			draw()





	if muV == 1 and muH == 2: 
		#import images
		BG = pygame.image.load('BG.png')
		RR = [pygame.image.load('RR_01.png'), pygame.image.load('RR_02.png'), pygame.image.load('RR_03.png'), pygame.image.load('RR_04.png'), pygame.image.load('RR_05.png'), pygame.image.load('RR_06.png'), pygame.image.load('RR_07.png'), pygame.image.load('RR_08.png')]
		RL = [pygame.image.load('RL_01.png'), pygame.image.load('RL_02.png'), pygame.image.load('RL_03.png'), pygame.image.load('RL_04.png'), pygame.image.load('RL_05.png'), pygame.image.load('RL_06.png'), pygame.image.load('RL_07.png'), pygame.image.load('RL_08.png')]
		RI = pygame.image.load('RI_01.png')
		RW = pygame.image.load('RW_01.png')
		BR = [pygame.image.load('BR_01.png'), pygame.image.load('BR_02.png'), pygame.image.load('BR_03.png'), pygame.image.load('BR_04.png'), pygame.image.load('BR_05.png'), pygame.image.load('BR_06.png'), pygame.image.load('BR_07.png'), pygame.image.load('BR_08.png')]
		BL = [pygame.image.load('BL_01.png'), pygame.image.load('BL_02.png'), pygame.image.load('BL_03.png'), pygame.image.load('BL_04.png'), pygame.image.load('BL_05.png'), pygame.image.load('BL_06.png'), pygame.image.load('BL_07.png'), pygame.image.load('BL_08.png')]
		BI = pygame.image.load('BI_01.png')
		BW = pygame.image.load('BW_01.png')
		BME = [pygame.image.load('BME_01.png'), pygame.image.load('BME_02.png'), pygame.image.load('BME_03.png'), pygame.image.load('BME_04.png'), pygame.image.load('BME_05.png'), pygame.image.load('BME_06.png'), pygame.image.load('BME_07.png'), pygame.image.load('BME_08.png')]
		BM = pygame.image.load('BM_01.png')
		SBG = pygame.image.load('score_BG.png')

		EXP = pygame.mixer.Sound('PEW.wav')
		POP = pygame.mixer.Sound('pling.wav')

		bluerand = random.randint(0, 724)

		class player(object):
			def __init__(self, x, y, w, h):
				self.x = x
				self.y = y
				self.w = w
				self.h = h
				self.left = False
				self.right = False
				self.vel = 10
				self.walkCount = 0
				self.jump_nyc = 0
				self.jump_change = 3
				self.jumping = False
				self.xplat = [730]
				self.plat_below = []
				self.targ_plat = 730
				self.hasBomb = 3
				self.score = 0
				self.superjumpcount = 0
				self.superjumping = False

			def move_left(self):
				self.left = True
				self.right = False
				self.x -= self.vel

			def move_right(self):
				self.left = False
				self.right = True
				self.x += self.vel

			def falling(self):
				#check if falling
				if self.y != (self.targ_plat - 100) and not self.jumping:
					self.jumping = True
					self.jump_nyc = 0
					self.jump()

					print(self.y)
					print(self.targ_plat + 100)

			def jump(self):
				#check platforms at same x
				self.xplat = [730]
				if ((self.x + 13) >= plat_1.x) and ((self.x + 13) <= (plat_1.x + plat_1.w)):
					self.xplat.append(plat_1.y)

				if ((self.x + 13) >= plat_2.x) and ((self.x + 13) <= (plat_2.x + plat_2.w)):
					self.xplat.append(plat_2.y)

				if ((self.x + 13) >= plat_3.x) and ((self.x + 13) <= (plat_3.x + plat_3.w)):
					self.xplat.append(plat_3.y)

				if ((self.x + 13) >= plat_4.x) and ((self.x + 13) <= (plat_4.x + plat_4.w)):
					self.xplat.append(plat_4.y)

				if ((self.x + 13) >= plat_5.x) and ((self.x + 13) <= (plat_5.x + plat_5.w)):
					self.xplat.append(plat_5.y)

				self.plat_below = []
				for plat_val in self.xplat:
					if plat_val > (self.y + 99):
						self.plat_below.append(plat_val)
					
				#find nearst platform under player
				self.targ_plat = 1000
				for plat_val2 in self.plat_below:
					if self.targ_plat > plat_val2 :
						self.targ_plat = plat_val2

				if self.y != (self.targ_plat - 100) and not self.jumping:
					self.jumping = True
					self.jump_nyc = 0

				#check if about to land
				if self.jumping:
					if (self.y + 99) - self.jump_nyc > self.targ_plat:
						self.y = self.targ_plat - 100
						self.jumping = False
						self.superjumping = False

					if self.jumping == True:
						self.y -= self.jump_nyc
						self.jump_nyc -= self.jump_change

		#init players
		red = player(50, 600, 26, 100)
		blue = player(674, 600, 26, 100)
		blue.vel = 10
		move_count = 0

		class bomb(object):
			def __init__(self, x, y):
				self.x = x
				self.y = y
				self.nyc = 0
				self.fall_speed = 3
				self.explode = True
				self.exploding = 20

			def fall(self):
				#make bomb fall
				if self.y < 1000 and self.explode == False:
					self.y -= self.nyc
					self.nyc -= self.fall_speed

					#expload on floor
					if (self.y + self.nyc) > 727:
						self.y = 727
						
						EXP.play()

						self.explode = True
						self.exploding = 0

			def draw(self, win):
				#draw bomb
				if self.explode == False:
					win.blit(BM, (self.x - 50, self.y - 50))

				#draw explosion
				if self.explode == True and self.exploding < 16:
					win.blit(BME[self.exploding//2], (self.x - 50,self.y - 50))

					self.exploding += 1

		#init freeze
		freeze = False
		freeze_count = 0

		#init red and blue bomb
		rBomb = bomb(0, 1001)
		bBomb = bomb(0, 1001)

		plat_change = 1999
		set_plat_change = 320

		class plat(object):
			def __init__(self, x, y, w, h):
				self.x = x
				self.y = y
				self.w = w
				self.h = h
				self.place = 0
				self.colour = (0, 0, 0)

			def random(self):
				#randomize platfoarm locations
				self.place = random.randint(1, 5)
				
				if self.place == 1:
					self.x = 50
					self.y = 600

				if self.place == 2:
					self.x = 500
					self.y = 600

				if self.place == 3:
					self.x = 275
					self.y = 450

				if self.place == 4:
					self.x = 50
					self.y = 300

				if self.place == 5:
					self.x = 500
					self.y = 300

			def create(self, win):
				#draw platforms
				pygame.draw.rect(win, self.colour, (self.x, self.y, self.w, self.h))

		#init platforms
		plat_main = plat(0, 730, 750, 20)
		plat_1 = plat(0, 0, 200, 10)
		plat_2 = plat(0, 0, 200, 10)
		plat_3 = plat(0, 0, 200, 10)
		plat_4 = plat(0, 0, 200, 10)
		plat_5 = plat(0, 0, 200, 10)

		font_name = pygame.font.match_font('impact')
		#draw scores
		def red_text(surf, text, size, x, y, colour):
			font = pygame.font.Font(font_name, size)
			text_surface = font.render(text, True, (colour))
			text_rect = text_surface.get_rect()
			text_rect.topleft = (x, y)
			surf.blit(text_surface, text_rect)

		def blue_text(surf, text, size, x, y, colour):
			font = pygame.font.Font(font_name, size)
			text_surface = font.render(text, True, (colour))
			text_rect = text_surface.get_rect()
			text_rect.topright = (x, y)
			surf.blit(text_surface, text_rect)

		def score_text(surf, text, size, x, y, colour):
			font = pygame.font.Font(font_name, size)
			text_surface = font.render(text, True, (colour))
			text_rect = text_surface.get_rect()
			text_rect.midtop = (x, y)
			surf.blit(text_surface, text_rect)

		def draw():
			if second >= 0:
				pygame.draw.rect(win, (255, 255, 255), (0, 0, 750, 750))

				#draw background
				win.blit(BG, (0,0))

				#red walk animation
				if red.walkCount + 1 >= 16:
						red.walkCount = 0

				if red.left and red.superjumping == False:
					win.blit(RL[red.walkCount//2], (red.x - 37,red.y))
					red.walkCount += 1

				elif red.right and red.superjumping == False:
					win.blit(RR[red.walkCount//2], (red.x - 37,red.y))
					red.walkCount += 1

				else:
					if red.superjumpcount >= 96 or red.superjumping == True:
						win.blit(RW, (red.x - 37,red.y))
					else:
						win.blit(RI, (red.x - 37,red.y))


				#blue walk animation
				if blue.walkCount + 1 >= 16:
						blue.walkCount = 0

				if blue.left and blue.superjumping == False:
					win.blit(BL[blue.walkCount//2], (blue.x - 37,blue.y))
					blue.walkCount += 1

				elif blue.right and blue.superjumping == False:
					win.blit(BR[blue.walkCount//2], (blue.x - 37,blue.y))
					blue.walkCount += 1

				else:
					if blue.superjumpcount >= 96 or blue.superjumping == True:
						win.blit(BW, (blue.x - 37,blue.y))
					else:
						win.blit(BI, (blue.x - 37,blue.y))

				#draw platforms
				plat_main.create(win)
				if (plat_change >= (set_plat_change - 4) and plat_change <= (set_plat_change - 2)) or (plat_change >= (set_plat_change - 10) and plat_change <= (set_plat_change - 7)) or (plat_change >= (set_plat_change - 18) and plat_change <= (set_plat_change - 14)) or (plat_change >= (set_plat_change - 28) and plat_change <= (set_plat_change - 23)) or (plat_change >= (set_plat_change - 40) and plat_change <= (set_plat_change - 34)) or (plat_change >= (set_plat_change - 54) and plat_change <= (set_plat_change - 47)) or (plat_change <= (set_plat_change - 62)):
					plat_1.create(win)
					plat_2.create(win)
					plat_3.create(win)
					plat_4.create(win)
					plat_5.create(win)

				#draw bombs
				rBomb.draw(win)
				bBomb.draw(win)

				#draw scores
				red_text(win, str(red.score), 30, 5, 5, (255, 0, 0))
				red_text(win, str(red.hasBomb), 20, 5, 35, (255, 0, 0))

				blue_text(win, str(second), 40, 745, 5, (0, 0, 255))
				#blue_text(win, str(blue.hasBomb), 20, 745, 35, (0, 0, 255))

			if second < 0:
				print_score = ("Your final score is: " + str(red.score))
				win.blit(SBG, (0,0))
				score_text(win, str(print_score), 50, 375, 275, (255, 0, 0))

			pygame.display.update()

		#main game loop
		second = 60
		tick = 0

		loop = True
		while loop:
			#set fps
			clock.tick(32)

			tick += 1
			if tick == 32:
				second -= 1
				tick = 0

			#exit
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()

			keys = pygame.key.get_pressed()

			if freeze == False:

				if keys[pygame.K_b]:
					loop = False

				#move red
				if keys[pygame.K_a] and keys[pygame.K_d]:
					red.left = False
					red.right = False

				else:	
					if keys[pygame.K_a] and red.x >= red.vel:
						red.move_left()
						red.superjumpcount = 0
						move_count = 16

					elif keys[pygame.K_d] and (red.x + red.w) <= (750 - red.vel):
						red.move_right()
						red.superjumpcount = 0
						move_count = 16

					else:
						red.left = False
						red.right = False

						if red.y == 630:
							red.superjumpcount += 1

						else:
							red.superjumpcount = 0

				#move blue
				if move_count > 0:
					move_count -= 1
					bluedir = bluerand - blue.x

					if bluedir < 0 and blue.x >= blue.vel:
						blue.move_left()

					if bluedir > 0 and (blue.x + blue.w) <= (750 - blue.vel):
						blue.move_right()

					if blue.x > (bluerand - 10) and blue.x < (bluerand + 10):
						bluerand = random.randint(0, 724)

				elif rBomb.explode == False:
					bluedir = (blue.x + 13) - rBomb.x

					if bluedir < 0 and blue.x >= blue.vel:
						blue.move_left()

					if bluedir > 0 and (blue.x + blue.w) <= (750 - blue.vel):
						blue.move_right()

				#red jump
				if (not red.jumping) and keys[pygame.K_w]:
					red.jumping = True
					if red.superjumpcount >= 96:
						red.jump_nyc = 60
						red.superjumping = True
					else:
						red.jump_nyc = 30

				if red.left == False and red.right == False and move_count == 0 and rBomb.explode == True:
					blue.left = False
					blue.right = False

				red.jump()
				blue.jump()

				#randomize platforms
				plat_change += 1
				if plat_change >= set_plat_change:
					plat_1.random()
					plat_2.random()
					plat_3.random()
					plat_4.random()
					plat_5.random()

					plat_change = 0

				#gives players bombs
				if red.y == 630:
					red.hasBomb = 3

				#red drop bomb
				if keys[pygame.K_s] and red.hasBomb > 0 and rBomb.exploding >= 16 and rBomb.explode == True and red.y < 460:
					rBomb.y = red.y + 100
					rBomb.x = red.x + 13

					rBomb.nyc = 0

					rBomb.exploding = 0
					rBomb.explode = False
					red.hasBomb -= 1

				#makes bombs fall
				rBomb.fall()

				#expload red bomb if hit blue player
				if rBomb.x >= blue.x - 37 and rBomb.x <= blue.x + 62 and rBomb.y >= blue.y + 25 and rBomb.y <= blue.y + 99 and rBomb.explode == False:
					rBomb.explode = True
					red.score += 1
					freeze = True
					POP.play()
					EXP.play()

			#freeze game if bomb hit player
			if freeze == True:
				freeze_count += 1

				if freeze_count == 32:
					freeze = False
					freeze_count = 0

					red.y = 600
					blue.y = 600
					red.x = random.randint(0, 724)
					blue.x = random.randint(0, 724)

					blue.jump_nyc = 0
					red.jump_nyc = 0

			#draw game
			draw()





	if muV == 2 and muH == 1: 
		#import images
		BG = pygame.image.load('BG_GN.png')
		RR = [pygame.image.load('RR_01.png'), pygame.image.load('RR_02.png'), pygame.image.load('RR_03.png'), pygame.image.load('RR_04.png'), pygame.image.load('RR_05.png'), pygame.image.load('RR_06.png'), pygame.image.load('RR_07.png'), pygame.image.load('RR_08.png')]
		RL = [pygame.image.load('RL_01.png'), pygame.image.load('RL_02.png'), pygame.image.load('RL_03.png'), pygame.image.load('RL_04.png'), pygame.image.load('RL_05.png'), pygame.image.load('RL_06.png'), pygame.image.load('RL_07.png'), pygame.image.load('RL_08.png')]
		RI = pygame.image.load('RI_01.png')
		RW = pygame.image.load('RW_01.png')
		BR = [pygame.image.load('BR_01.png'), pygame.image.load('BR_02.png'), pygame.image.load('BR_03.png'), pygame.image.load('BR_04.png'), pygame.image.load('BR_05.png'), pygame.image.load('BR_06.png'), pygame.image.load('BR_07.png'), pygame.image.load('BR_08.png')]
		BL = [pygame.image.load('BL_01.png'), pygame.image.load('BL_02.png'), pygame.image.load('BL_03.png'), pygame.image.load('BL_04.png'), pygame.image.load('BL_05.png'), pygame.image.load('BL_06.png'), pygame.image.load('BL_07.png'), pygame.image.load('BL_08.png')]
		BI = pygame.image.load('BI_01.png')
		BW = pygame.image.load('BW_01.png')
		BME = [pygame.image.load('BME_01.png'), pygame.image.load('BME_02.png'), pygame.image.load('BME_03.png'), pygame.image.load('BME_04.png'), pygame.image.load('BME_05.png'), pygame.image.load('BME_06.png'), pygame.image.load('BME_07.png'), pygame.image.load('BME_08.png')]
		BM = pygame.image.load('GN_01.png')

		EXP = pygame.mixer.Sound('PEW.wav')
		POP = pygame.mixer.Sound('pling.wav')

		class player(object):
			def __init__(self, x, y, w, h):
				self.x = x
				self.y = y
				self.w = w
				self.h = h
				self.left = False
				self.right = False
				self.vel = 10
				self.walkCount = 0
				self.jump_nyc = 0
				self.jump_change = 3
				self.jumping = False
				self.xplat = [730]
				self.plat_below = []
				self.targ_plat = 730
				self.hasBomb = 3
				self.score = 0
				self.superjumpcount = 0
				self.superjumping = False

			def move_left(self):
				self.left = True
				self.right = False
				self.x -= self.vel

			def move_right(self):
				self.left = False
				self.right = True
				self.x += self.vel

			def falling(self):
				#check if falling
				if self.y != (self.targ_plat - 100) and not self.jumping:
					self.jumping = True
					self.jump_nyc = 0
					self.jump()

					print(self.y)
					print(self.targ_plat + 100)

			def jump(self):
				#check platforms at same x
				self.xplat = [730]
				if ((self.x + 13) >= plat_1.x) and ((self.x + 13) <= (plat_1.x + plat_1.w)):
					self.xplat.append(plat_1.y)

				if ((self.x + 13) >= plat_2.x) and ((self.x + 13) <= (plat_2.x + plat_2.w)):
					self.xplat.append(plat_2.y)

				if ((self.x + 13) >= plat_3.x) and ((self.x + 13) <= (plat_3.x + plat_3.w)):
					self.xplat.append(plat_3.y)

				if ((self.x + 13) >= plat_4.x) and ((self.x + 13) <= (plat_4.x + plat_4.w)):
					self.xplat.append(plat_4.y)

				if ((self.x + 13) >= plat_5.x) and ((self.x + 13) <= (plat_5.x + plat_5.w)):
					self.xplat.append(plat_5.y)

				self.plat_below = []
				for plat_val in self.xplat:
					if plat_val > (self.y + 99):
						self.plat_below.append(plat_val)
					
				#find nearst platform under player
				self.targ_plat = 1000
				for plat_val2 in self.plat_below:
					if self.targ_plat > plat_val2 :
						self.targ_plat = plat_val2

				if self.y != (self.targ_plat - 100) and not self.jumping:
					self.jumping = True
					self.jump_nyc = 0

				#check if about to land
				if self.jumping:
					if (self.y + 99) - self.jump_nyc > self.targ_plat:
						self.y = self.targ_plat - 100
						self.jumping = False
						self.superjumping = False

					if self.jumping == True:
						self.y -= self.jump_nyc
						self.jump_nyc -= self.jump_change

		#init players
		red = player(50, 600, 26, 100)
		blue = player(674, 600, 26, 100)

		class bomb(object):
			def __init__(self, x, y):
				self.x = x
				self.y = y
				self.nyc = 0
				self.fall_speed = 0.75
				self.explode = True
				self.exploding = 20
				self.vel = 20
				self.dir = 0

			def fall(self):
				#make bomb fall
				if self.y < 1000 and self.explode == False:
					self.y -= self.nyc
					self.nyc -= self.fall_speed

					#expload on floor
					if (self.x + self.vel) > 750:
						self.x = 725
						
						EXP.play()

						self.explode = True
						self.exploding = 0

					if (self.x + self.vel) < 0:
						self.x = 25
						
						EXP.play()

						self.explode = True
						self.exploding = 0

					if (self.y + self.nyc) > 727:
						self.y = 727
						
						EXP.play()

						self.explode = True
						self.exploding = 0

					self.x += (self.vel * self.dir)

			def draw(self, win):
				#draw bomb
				if self.explode == False:
					win.blit(BM, (self.x - 50, self.y - 50))

				#draw explosion
				if self.explode == True and self.exploding < 16:
					win.blit(BME[self.exploding//2], (self.x - 50,self.y - 50))

					self.exploding += 1

		#init freeze
		freeze = False
		freeze_count = 0

		#init red and blue bomb
		rBomb = bomb(0, 1001)
		bBomb = bomb(0, 1001)

		plat_change = 1999
		set_plat_change = 320

		class plat(object):
			def __init__(self, x, y, w, h):
				self.x = x
				self.y = y
				self.w = w
				self.h = h
				self.place = 0
				self.colour = (0, 0, 0)

			def random(self):
				#randomize platfoarm locations
				self.place = random.randint(1, 5)
				
				if self.place == 1:
					self.x = 50
					self.y = 600

				if self.place == 2:
					self.x = 500
					self.y = 600

				if self.place == 3:
					self.x = 275
					self.y = 450

				if self.place == 4:
					self.x = 50
					self.y = 300

				if self.place == 5:
					self.x = 500
					self.y = 300

			def create(self, win):
				#draw platforms
				pygame.draw.rect(win, self.colour, (self.x, self.y, self.w, self.h))

		#init platforms
		plat_main = plat(0, 730, 750, 20)
		plat_1 = plat(0, 0, 200, 10)
		plat_2 = plat(0, 0, 200, 10)
		plat_3 = plat(0, 0, 200, 10)
		plat_4 = plat(0, 0, 200, 10)
		plat_5 = plat(0, 0, 200, 10)

		font_name = pygame.font.match_font('impact')
		#draw scores
		def red_text(surf, text, size, x, y, colour):
			font = pygame.font.Font(font_name, size)
			text_surface = font.render(text, True, (colour))
			text_rect = text_surface.get_rect()
			text_rect.topleft = (x, y)
			surf.blit(text_surface, text_rect)

		def blue_text(surf, text, size, x, y, colour):
			font = pygame.font.Font(font_name, size)
			text_surface = font.render(text, True, (colour))
			text_rect = text_surface.get_rect()
			text_rect.topright = (x, y)
			surf.blit(text_surface, text_rect)

		def draw():
			pygame.draw.rect(win, (255, 255, 255), (0, 0, 750, 750))

			#draw background
			win.blit(BG, (0,0))

			#red walk animation
			if red.walkCount + 1 >= 16:
					red.walkCount = 0

			if red.left and red.superjumping == False:
				win.blit(RL[red.walkCount//2], (red.x - 37,red.y))
				red.walkCount += 1

			elif red.right and red.superjumping == False:
				win.blit(RR[red.walkCount//2], (red.x - 37,red.y))
				red.walkCount += 1

			else:
				if red.superjumpcount >= 96 or red.superjumping == True:
					win.blit(RW, (red.x - 37,red.y))
				else:
					win.blit(RI, (red.x - 37,red.y))


			#blue walk animation
			if blue.walkCount + 1 >= 16:
					blue.walkCount = 0

			if blue.left and blue.superjumping == False:
				win.blit(BL[blue.walkCount//2], (blue.x - 37,blue.y))
				blue.walkCount += 1

			elif blue.right and blue.superjumping == False:
				win.blit(BR[blue.walkCount//2], (blue.x - 37,blue.y))
				blue.walkCount += 1

			else:
				if blue.superjumpcount >= 96 or blue.superjumping == True:
					win.blit(BW, (blue.x - 37,blue.y))
				else:
					win.blit(BI, (blue.x - 37,blue.y))

			#draw platforms
			plat_main.create(win)
			if (plat_change >= (set_plat_change - 4) and plat_change <= (set_plat_change - 2)) or (plat_change >= (set_plat_change - 10) and plat_change <= (set_plat_change - 7)) or (plat_change >= (set_plat_change - 18) and plat_change <= (set_plat_change - 14)) or (plat_change >= (set_plat_change - 28) and plat_change <= (set_plat_change - 23)) or (plat_change >= (set_plat_change - 40) and plat_change <= (set_plat_change - 34)) or (plat_change >= (set_plat_change - 54) and plat_change <= (set_plat_change - 47)) or (plat_change <= (set_plat_change - 62)):
				plat_1.create(win)
				plat_2.create(win)
				plat_3.create(win)
				plat_4.create(win)
				plat_5.create(win)

			#draw bombs
			rBomb.draw(win)
			bBomb.draw(win)

			#draw scores
			red_text(win, str(red.score), 30, 5, 5, (255, 0, 0))
			red_text(win, str(red.hasBomb), 20, 5, 35, (255, 0, 0))

			blue_text(win, str(blue.score), 30, 745, 5, (0, 0, 255))
			blue_text(win, str(blue.hasBomb), 20, 745, 35, (0, 0, 255))

			pygame.display.update()

		#main game loop
		loop = True
		while loop:
			#set fps
			clock.tick(32)

			#exit
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()

			keys = pygame.key.get_pressed()

			if freeze == False:

				if keys[pygame.K_b]:
					loop = False

				#move red
				if keys[pygame.K_a] and keys[pygame.K_d]:
					red.left = False
					red.right = False

				else:	
					if keys[pygame.K_a] and red.x >= red.vel:
						red.move_left()
						red.superjumpcount = 0

					elif keys[pygame.K_d] and (red.x + red.w) <= (750 - red.vel):
						red.move_right()
						red.superjumpcount = 0

					else:
						red.left = False
						red.right = False

						if red.y == 630:
							red.superjumpcount += 1

						else:
							red.superjumpcount = 0

				#move blue
				if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
					blue.left = False
					blue.right = False
				
				else:
					if keys[pygame.K_LEFT] and blue.x >= blue.vel:
						blue.move_left()
						blue.superjumpcount = 0

					elif keys[pygame.K_RIGHT] and (blue.x + blue.w) <= (750 - blue.vel):
						blue.move_right()
						blue.superjumpcount = 0

					else:
						blue.left = False
						blue.right = False

						if blue.y == 630:
							blue.superjumpcount += 1

						else:
							blue.superjumpcount = 0

				#red jump
				if (not red.jumping) and keys[pygame.K_w]:
					red.jumping = True
					if red.superjumpcount >= 96:
						red.jump_nyc = 60
						red.superjumping = True
					else:
						red.jump_nyc = 30

				#blue jump
				if (not blue.jumping) and keys[pygame.K_UP]:
					blue.jumping = True
					if blue.superjumpcount >= 96:
						blue.jump_nyc = 60
						blue.superjumping = True
					else:
						blue.jump_nyc = 30

				red.jump()
				blue.jump()

				#randomize platforms
				plat_change += 1
				if plat_change >= set_plat_change:
					plat_1.random()
					plat_2.random()
					plat_3.random()
					plat_4.random()
					plat_5.random()

					plat_change = 0

				#gives players bombs
				if red.y == 630:
					red.hasBomb = 3

				if blue.y == 630:
					blue.hasBomb = 3

				#red drop bomb
				if keys[pygame.K_s] and keys[pygame.K_d] and red.hasBomb > 0 and rBomb.exploding >= 16 and rBomb.explode == True:
					rBomb.y = red.y + 50
					rBomb.x = red.x + 13

					rBomb.nyc = 10

					rBomb.exploding = 0
					rBomb.explode = False
					red.hasBomb -= 1

					rBomb.dir = 1

				if keys[pygame.K_s] and keys[pygame.K_a] and red.hasBomb > 0 and rBomb.exploding >= 16 and rBomb.explode == True:
					rBomb.y = red.y + 50
					rBomb.x = red.x + 13

					rBomb.nyc = 10

					rBomb.exploding = 0
					rBomb.explode = False
					red.hasBomb -= 1

					rBomb.dir = -1

				#blue drop bomb
				if keys[pygame.K_DOWN] and keys[pygame.K_RIGHT] and blue.hasBomb > 0 and bBomb.exploding >= 16 and bBomb.explode == True:
					bBomb.y = blue.y + 50
					bBomb.x = blue.x + 13

					bBomb.nyc = 10

					bBomb.exploding = 0
					bBomb.explode = False
					blue.hasBomb -= 1

					bBomb.dir = 1

				if keys[pygame.K_DOWN] and keys[pygame.K_LEFT] and blue.hasBomb > 0 and bBomb.exploding >= 16 and bBomb.explode == True:
					bBomb.y = blue.y + 50
					bBomb.x = blue.x + 13

					bBomb.nyc = 10

					bBomb.exploding = 0
					bBomb.explode = False
					blue.hasBomb -= 1

					bBomb.dir = -1

				#makes bombs fall
				rBomb.fall()
				bBomb.fall()

				#expload red bomb if hit blue player
				if rBomb.x >= blue.x - 37 and rBomb.x <= blue.x + 62 and rBomb.y >= blue.y and rBomb.y <= blue.y + 99 and rBomb.explode == False:
					rBomb.explode = True
					red.score += 1
					freeze = True
					POP.play()
					EXP.play()

				#expload blue bomb if hit red player
				if bBomb.x >= red.x - 37 and bBomb.x <= red.x + 62 and bBomb.y >= red.y and bBomb.y <= red.y + 99 and bBomb.explode == False:
					bBomb.explode = True
					blue.score += 1
					freeze = True
					POP.play()
					EXP.play()

				if bBomb.x >= rBomb.x - 50 and bBomb.x <= rBomb.x + 50 and bBomb.y >= rBomb.y - 50 and bBomb.y <= rBomb.y + 50 and bBomb.explode == False and rBomb.explode == False:
					bBomb.explode = True
					rBomb.explode = True
					EXP.play()

			#freeze game if bomb hit player
			if freeze == True:
				bBomb.explode = True
				rBomb.explode = True
				freeze_count += 1

				if freeze_count == 32:
					freeze = False
					freeze_count = 0

					red.y = 600
					blue.y = 600
					red.x = 50
					blue.x = 674

					blue.jump_nyc = 0
					red.jump_nyc = 0

			#draw game
			draw()





	if muV == 2 and muH == 2: 
		#import images
		BG = pygame.image.load('BG_GN.png')
		RR = [pygame.image.load('RR_01.png'), pygame.image.load('RR_02.png'), pygame.image.load('RR_03.png'), pygame.image.load('RR_04.png'), pygame.image.load('RR_05.png'), pygame.image.load('RR_06.png'), pygame.image.load('RR_07.png'), pygame.image.load('RR_08.png')]
		RL = [pygame.image.load('RL_01.png'), pygame.image.load('RL_02.png'), pygame.image.load('RL_03.png'), pygame.image.load('RL_04.png'), pygame.image.load('RL_05.png'), pygame.image.load('RL_06.png'), pygame.image.load('RL_07.png'), pygame.image.load('RL_08.png')]
		RI = pygame.image.load('RI_01.png')
		RW = pygame.image.load('RW_01.png')
		BR = [pygame.image.load('BR_01.png'), pygame.image.load('BR_02.png'), pygame.image.load('BR_03.png'), pygame.image.load('BR_04.png'), pygame.image.load('BR_05.png'), pygame.image.load('BR_06.png'), pygame.image.load('BR_07.png'), pygame.image.load('BR_08.png')]
		BL = [pygame.image.load('BL_01.png'), pygame.image.load('BL_02.png'), pygame.image.load('BL_03.png'), pygame.image.load('BL_04.png'), pygame.image.load('BL_05.png'), pygame.image.load('BL_06.png'), pygame.image.load('BL_07.png'), pygame.image.load('BL_08.png')]
		BI = pygame.image.load('BI_01.png')
		BW = pygame.image.load('BW_01.png')
		BME = [pygame.image.load('BME_01.png'), pygame.image.load('BME_02.png'), pygame.image.load('BME_03.png'), pygame.image.load('BME_04.png'), pygame.image.load('BME_05.png'), pygame.image.load('BME_06.png'), pygame.image.load('BME_07.png'), pygame.image.load('BME_08.png')]
		BM = pygame.image.load('GN_01.png')
		SBG = pygame.image.load('score_BG.png')
		TG = pygame.image.load('TG_01.png')

		EXP = pygame.mixer.Sound('PEW.wav')
		POP = pygame.mixer.Sound('pling.wav')

		class player(object):
			def __init__(self, x, y, w, h):
				self.x = x
				self.y = y
				self.w = w
				self.h = h
				self.left = False
				self.right = False
				self.vel = 10
				self.walkCount = 0
				self.jump_nyc = 0
				self.jump_change = 3
				self.jumping = False
				self.xplat = [730]
				self.plat_below = []
				self.targ_plat = 730
				self.hasBomb = 3
				self.score = 0
				self.superjumpcount = 0
				self.superjumping = False

			def move_left(self):
				self.left = True
				self.right = False
				self.x -= self.vel

			def move_right(self):
				self.left = False
				self.right = True
				self.x += self.vel

			def falling(self):
				#check if falling
				if self.y != (self.targ_plat - 100) and not self.jumping:
					self.jumping = True
					self.jump_nyc = 0
					self.jump()

					print(self.y)
					print(self.targ_plat + 100)

			def jump(self):
				#check platforms at same x
				self.xplat = [730]
				if ((self.x + 13) >= plat_1.x) and ((self.x + 13) <= (plat_1.x + plat_1.w)):
					self.xplat.append(plat_1.y)

				if ((self.x + 13) >= plat_2.x) and ((self.x + 13) <= (plat_2.x + plat_2.w)):
					self.xplat.append(plat_2.y)

				if ((self.x + 13) >= plat_3.x) and ((self.x + 13) <= (plat_3.x + plat_3.w)):
					self.xplat.append(plat_3.y)

				if ((self.x + 13) >= plat_4.x) and ((self.x + 13) <= (plat_4.x + plat_4.w)):
					self.xplat.append(plat_4.y)

				if ((self.x + 13) >= plat_5.x) and ((self.x + 13) <= (plat_5.x + plat_5.w)):
					self.xplat.append(plat_5.y)

				self.plat_below = []
				for plat_val in self.xplat:
					if plat_val > (self.y + 99):
						self.plat_below.append(plat_val)
					
				#find nearst platform under player
				self.targ_plat = 1000
				for plat_val2 in self.plat_below:
					if self.targ_plat > plat_val2 :
						self.targ_plat = plat_val2

				if self.y != (self.targ_plat - 100) and not self.jumping:
					self.jumping = True
					self.jump_nyc = 0

				#check if about to land
				if self.jumping:
					if (self.y + 99) - self.jump_nyc > self.targ_plat:
						self.y = self.targ_plat - 100
						self.jumping = False
						self.superjumping = False

					if self.jumping == True:
						self.y -= self.jump_nyc
						self.jump_nyc -= self.jump_change

		#init players
		red = player(50, 600, 26, 100)

		class bomb(object):
			def __init__(self, x, y):
				self.x = x
				self.y = y
				self.nyc = 0
				self.fall_speed = 0.75
				self.explode = True
				self.exploding = 20
				self.vel = 20
				self.dir = 0

			def fall(self):
				#make bomb fall
				if self.y < 1000 and self.explode == False:
					self.y -= self.nyc
					self.nyc -= self.fall_speed

					#expload on floor
					if (self.x + self.vel) > 750:
						self.x = 725
						
						EXP.play()

						self.explode = True
						self.exploding = 0

					if (self.x + self.vel) < 0:
						self.x = 25
						
						EXP.play()

						self.explode = True
						self.exploding = 0

					if (self.y + self.nyc) > 727:
						self.y = 727
						
						EXP.play()

						self.explode = True
						self.exploding = 0

					self.x += (self.vel * self.dir)

			def draw(self, win):
				#draw bomb
				if self.explode == False:
					win.blit(BM, (self.x - 50, self.y - 50))

				#draw explosion
				if self.explode == True and self.exploding < 16:
					win.blit(BME[self.exploding//2], (self.x - 50,self.y - 50))

					self.exploding += 1

		#init freeze
		freeze = False
		freeze_count = 0

		#init red and blue bomb
		rBomb = bomb(0, 1001)

		plat_change = 1999
		set_plat_change = 320

		class target(object):
			def __init__(self, x, y):
				self.x = x
				self.y = y
				self.side = 0
				self.dir = 1
				self.targ_y = 0
				self.vel = 10

			def new_targ(self):
				self.targ_y = random.randint(50, 700)

			def hit(self):
				self.side = random.randint(0, 1)
				
				if self.side == 0:
					self.x = 25

				if self.side == 1:
					self.x = 725

			def move(self):
				if self.targ_y - self.y > 0:
					self.dir = 1

				if self.targ_y - self.y < 0:
					self.dir = -1

				self.y += self.vel * self.dir

				if self.y < self.targ_y + 10 and self.y > self.targ_y - 10:
					self.new_targ()

				if targ.x >= rBomb.x - 50 and targ.x <= rBomb.x + 50 and targ.y >= rBomb.y - 50 and targ.y <= rBomb.y + 50 and rBomb.explode == False:
					rBomb.explode = True
					red.score += 1
					freeze = True
					POP.play()
					EXP.play()

					self.hit()

		targ = target(25, 25)
		targ.hit()
		targ.new_targ()

		class plat(object):
			def __init__(self, x, y, w, h):
				self.x = x
				self.y = y
				self.w = w
				self.h = h
				self.place = 0
				self.colour = (0, 0, 0)

			def random(self):
				#randomize platfoarm locations
				self.place = random.randint(1, 5)
				
				if self.place == 1:
					self.x = 50
					self.y = 600

				if self.place == 2:
					self.x = 500
					self.y = 600

				if self.place == 3:
					self.x = 275
					self.y = 450

				if self.place == 4:
					self.x = 50
					self.y = 300

				if self.place == 5:
					self.x = 500
					self.y = 300

			def create(self, win):
				#draw platforms
				pygame.draw.rect(win, self.colour, (self.x, self.y, self.w, self.h))

		#init platforms
		plat_main = plat(0, 730, 750, 20)
		plat_1 = plat(0, 0, 200, 10)
		plat_2 = plat(0, 0, 200, 10)
		plat_3 = plat(0, 0, 200, 10)
		plat_4 = plat(0, 0, 200, 10)
		plat_5 = plat(0, 0, 200, 10)

		font_name = pygame.font.match_font('impact')
		#draw scores
		def red_text(surf, text, size, x, y, colour):
			font = pygame.font.Font(font_name, size)
			text_surface = font.render(text, True, (colour))
			text_rect = text_surface.get_rect()
			text_rect.topleft = (x, y)
			surf.blit(text_surface, text_rect)

		def blue_text(surf, text, size, x, y, colour):
			font = pygame.font.Font(font_name, size)
			text_surface = font.render(text, True, (colour))
			text_rect = text_surface.get_rect()
			text_rect.topright = (x, y)
			surf.blit(text_surface, text_rect)

		def score_text(surf, text, size, x, y, colour):
			font = pygame.font.Font(font_name, size)
			text_surface = font.render(text, True, (colour))
			text_rect = text_surface.get_rect()
			text_rect.midtop = (x, y)
			surf.blit(text_surface, text_rect)

		def draw():
			if second >= 0:
				pygame.draw.rect(win, (255, 255, 255), (0, 0, 750, 750))

				#draw background
				win.blit(BG, (0,0))

				#red walk animation
				if red.walkCount + 1 >= 16:
						red.walkCount = 0

				if red.left and red.superjumping == False:
					win.blit(RL[red.walkCount//2], (red.x - 37,red.y))
					red.walkCount += 1

				elif red.right and red.superjumping == False:
					win.blit(RR[red.walkCount//2], (red.x - 37,red.y))
					red.walkCount += 1

				else:
					if red.superjumpcount >= 96 or red.superjumping == True:
						win.blit(RW, (red.x - 37,red.y))
					else:
						win.blit(RI, (red.x - 37,red.y))

				#draw platforms
				plat_main.create(win)
				if (plat_change >= (set_plat_change - 4) and plat_change <= (set_plat_change - 2)) or (plat_change >= (set_plat_change - 10) and plat_change <= (set_plat_change - 7)) or (plat_change >= (set_plat_change - 18) and plat_change <= (set_plat_change - 14)) or (plat_change >= (set_plat_change - 28) and plat_change <= (set_plat_change - 23)) or (plat_change >= (set_plat_change - 40) and plat_change <= (set_plat_change - 34)) or (plat_change >= (set_plat_change - 54) and plat_change <= (set_plat_change - 47)) or (plat_change <= (set_plat_change - 62)):
					plat_1.create(win)
					plat_2.create(win)
					plat_3.create(win)
					plat_4.create(win)
					plat_5.create(win)

				#draw bombs
				rBomb.draw(win)

				win.blit(TG, (targ.x - 50, targ.y - 50))

				#draw scores
				red_text(win, str(red.score), 30, 5, 5, (255, 0, 0))
				red_text(win, str(red.hasBomb), 20, 5, 35, (255, 0, 0))

				blue_text(win, str(second), 40, 745, 5, (0, 0, 255))
				# blue_text(win, str(blue.hasBomb), 20, 745, 35, (0, 0, 255))
			else:
				print_score = ("Your final score is: " + str(red.score))
				win.blit(SBG, (0,0))
				score_text(win, str(print_score), 50, 375, 275, (255, 0, 0))

			pygame.display.update()

		second = 60
		tick = 0

		#main game loop
		loop = True
		while loop:
			#set fps
			clock.tick(32)

			tick += 1
			if tick == 32:
				second -= 1
				tick = 0

			#exit
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()

			keys = pygame.key.get_pressed()

			if freeze == False:

				if keys[pygame.K_b]:
					loop = False

				#move red
				if keys[pygame.K_a] and keys[pygame.K_d]:
					red.left = False
					red.right = False

				else:	
					if keys[pygame.K_a] and red.x >= red.vel:
						red.move_left()
						red.superjumpcount = 0

					elif keys[pygame.K_d] and (red.x + red.w) <= (750 - red.vel):
						red.move_right()
						red.superjumpcount = 0

					else:
						red.left = False
						red.right = False

						if red.y == 630:
							red.superjumpcount += 1

						else:
							red.superjumpcount = 0

				#red jump
				if (not red.jumping) and keys[pygame.K_w]:
					red.jumping = True
					if red.superjumpcount >= 96:
						red.jump_nyc = 60
						red.superjumping = True
					else:
						red.jump_nyc = 30

				red.jump()

				#move target
				targ.move()

				#randomize platforms
				plat_change += 1
				if plat_change >= set_plat_change:
					plat_1.random()
					plat_2.random()
					plat_3.random()
					plat_4.random()
					plat_5.random()

					plat_change = 0

				#gives players bombs
				if red.y == 630:
					red.hasBomb = 3

				#red drop bomb
				if keys[pygame.K_s] and keys[pygame.K_d] and red.hasBomb > 0 and rBomb.exploding >= 16 and rBomb.explode == True:
					rBomb.y = red.y + 50
					rBomb.x = red.x + 13

					rBomb.nyc = 10

					rBomb.exploding = 0
					rBomb.explode = False
					red.hasBomb -= 1

					rBomb.dir = 1

				if keys[pygame.K_s] and keys[pygame.K_a] and red.hasBomb > 0 and rBomb.exploding >= 16 and rBomb.explode == True:
					rBomb.y = red.y + 50
					rBomb.x = red.x + 13

					rBomb.nyc = 10

					rBomb.exploding = 0
					rBomb.explode = False
					red.hasBomb -= 1

					rBomb.dir = -1

				#makes bombs fall
				rBomb.fall()

				#expload red bomb if hit blue player
				# if rBomb.x >= blue.x - 37 and rBomb.x <= blue.x + 62 and rBomb.y >= blue.y and rBomb.y <= blue.y + 99 and rBomb.explode == False:
				# 	rBomb.explode = True
				# 	red.score += 1
				# 	freeze = True
				# 	POP.play()
				# 	EXP.play()

				# if bBomb.x >= rBomb.x - 50 and bBomb.x <= rBomb.x +0 50 and bBomb.y >= rBomb.y - 50 and bBomb.y <= rBomb.y + 50 and bBomb.explode == False and rBomb.explode == False:
				# 	bBomb.explode = True
				# 	rBomb.explode = True
				# 	EXP.play()

			#freeze game if bomb hit player
			if freeze == True:
				rBomb.explode = True
				freeze_count += 1

				if freeze_count == 32:
					freeze = False
					freeze_count = 0

					red.y = 600
					red.x = 50

					red.jump_nyc = 0

			#draw game
			draw()





	if muV == 3 and muH == 1: 
		#import images
		BG = pygame.image.load('falling_BG.png')
		BG_power = pygame.image.load('falling_power.png')
		RR = [pygame.image.load('RR_01.png'), pygame.image.load('RR_02.png'), pygame.image.load('RR_03.png'), pygame.image.load('RR_04.png'), pygame.image.load('RR_05.png'), pygame.image.load('RR_06.png'), pygame.image.load('RR_07.png'), pygame.image.load('RR_08.png')]
		RL = [pygame.image.load('RL_01.png'), pygame.image.load('RL_02.png'), pygame.image.load('RL_03.png'), pygame.image.load('RL_04.png'), pygame.image.load('RL_05.png'), pygame.image.load('RL_06.png'), pygame.image.load('RL_07.png'), pygame.image.load('RL_08.png')]
		RI = pygame.image.load('RI_01.png')
		RW = pygame.image.load('RW_01.png')
		BR = [pygame.image.load('BR_01.png'), pygame.image.load('BR_02.png'), pygame.image.load('BR_03.png'), pygame.image.load('BR_04.png'), pygame.image.load('BR_05.png'), pygame.image.load('BR_06.png'), pygame.image.load('BR_07.png'), pygame.image.load('BR_08.png')]
		BL = [pygame.image.load('BL_01.png'), pygame.image.load('BL_02.png'), pygame.image.load('BL_03.png'), pygame.image.load('BL_04.png'), pygame.image.load('BL_05.png'), pygame.image.load('BL_06.png'), pygame.image.load('BL_07.png'), pygame.image.load('BL_08.png')]
		BI = pygame.image.load('BI_01.png')
		BW = pygame.image.load('BW_01.png')
		BME = [pygame.image.load('BME_01.png'), pygame.image.load('BME_02.png'), pygame.image.load('BME_03.png'), pygame.image.load('BME_04.png'), pygame.image.load('BME_05.png'), pygame.image.load('BME_06.png'), pygame.image.load('BME_07.png'), pygame.image.load('BME_08.png')]
		BM = pygame.image.load('BM_01.png')

		EXP = pygame.mixer.Sound('PEW.wav')
		POP = pygame.mixer.Sound('pling.wav')

		class player(object):
			def __init__(self, x, y, w, h):
				self.x = x
				self.y = y
				self.w = w
				self.h = h
				self.left = False
				self.right = False
				self.vel = 10
				self.walkCount = 0
				self.jump_nyc = 0
				self.jump_change = 3
				self.jumping = False
				self.xplat = [730]
				self.plat_below = []
				self.targ_plat = 730
				self.hasBomb = 3
				self.score = 0
				self.superjumpcount = 0
				self.superjumping = False

			def move_left(self):
				self.left = True
				self.right = False
				self.x -= self.vel

			def move_right(self):
				self.left = False
				self.right = True
				self.x += self.vel

			def falling(self):
				#check if falling
				if self.y != (self.targ_plat - 100) and not self.jumping:
					self.jumping = True
					self.jump_nyc = 0
					self.jump()

					print(self.y)
					print(self.targ_plat + 100)

			def jump(self):
				#check platforms at same x
				self.xplat = [730]
				if ((self.x + 13) >= plat_1.x) and ((self.x + 13) <= (plat_1.x + plat_1.w)):
					self.xplat.append(plat_1.y)

				if ((self.x + 13) >= plat_2.x) and ((self.x + 13) <= (plat_2.x + plat_2.w)):
					self.xplat.append(plat_2.y)

				if ((self.x + 13) >= plat_3.x) and ((self.x + 13) <= (plat_3.x + plat_3.w)):
					self.xplat.append(plat_3.y)

				if ((self.x + 13) >= plat_4.x) and ((self.x + 13) <= (plat_4.x + plat_4.w)):
					self.xplat.append(plat_4.y)

				if ((self.x + 13) >= plat_5.x) and ((self.x + 13) <= (plat_5.x + plat_5.w)):
					self.xplat.append(plat_5.y)

				self.plat_below = []
				for plat_val in self.xplat:
					if plat_val > (self.y + 99):
						self.plat_below.append(plat_val)
					
				#find nearst platform under player
				self.targ_plat = 1000
				for plat_val2 in self.plat_below:
					if self.targ_plat > plat_val2 :
						self.targ_plat = plat_val2

				if self.y != (self.targ_plat - 100) and not self.jumping:
					self.jumping = True
					self.jump_nyc = 0

				#check if about to land
				if self.jumping:
					if (self.y + 99) - self.jump_nyc > self.targ_plat:
						self.y = self.targ_plat - 100
						self.jumping = False
						self.superjumping = False

					if self.jumping == True:
						self.y -= self.jump_nyc
						self.jump_nyc -= self.jump_change

		#init players
		red = player(50, 600, 26, 100)
		blue = player(674, 600, 26, 100)

		class bomb(object):
			def __init__(self, x, y):
				self.x = x
				self.y = y
				self.nyc = 0
				self.fall_speed = 2
				self.explode = True
				self.exploding = 20

			def fall(self):
				#make bomb fall
				if self.y < 1000 and self.explode == False:
					self.y -= self.nyc
					self.nyc -= self.fall_speed

					#expload on floor
					if (self.y + self.nyc) > 727:
						self.y = 727
						
						EXP.play()

						self.explode = True
						self.exploding = 0

				if self.exploding >= 16 and self.explode == True:
					self.rand()

			def draw(self, win):
				#draw bomb
				if self.explode == False:
					win.blit(BM, (self.x - 50, self.y - 50))

				#draw explosion
				if self.explode == True and self.exploding < 16:
					win.blit(BME[self.exploding//2], (self.x - 50,self.y - 50))

					self.exploding += 1

			def hit(self):
				#expload bomb if hit blue player
				if self.x >= blue.x - 37 and self.x <= blue.x + 62 and self.y >= blue.y + 25 and self.y <= blue.y + 99 and self.explode == False:
					self.explode = True
					blue.score += 1
					freeze = True
					POP.play()
					EXP.play()

				#expload bomb if hit red player
				if self.x >= red.x - 37 and self.x <= red.x + 62 and self.y >= red.y + 25 and self.y <= red.y + 99 and self.explode == False:
					self.explode = True
					red.score += 1
					freeze = True
					POP.play()
					EXP.play()	

			def rand(self):
				self.x = random.randint(25, 725)
				self.y = random.randint(25, 100) * -1

				self.nyc = 0

				self.exploding = 0
				self.explode = False

		#init freeze
		freeze = False
		freeze_count = 0

		#init red and blue bomb
		bomb1 = bomb(0, 1001)
		bomb2 = bomb(0, 1001)
		bomb3 = bomb(0, 1001)

		plat_change = 1999
		set_plat_change = 320

		class plat(object):
			def __init__(self, x, y, w, h):
				self.x = x
				self.y = y
				self.w = w
				self.h = h
				self.place = 0
				self.colour = (0, 0, 0)

			def random(self):
				#randomize platfoarm locations
				self.place = random.randint(1, 5)
				
				if self.place == 1:
					self.x = 50
					self.y = 600

				if self.place == 2:
					self.x = 500
					self.y = 600

				if self.place == 3:
					self.x = 275
					self.y = 450

				if self.place == 4:
					self.x = 50
					self.y = 300

				if self.place == 5:
					self.x = 500
					self.y = 300

			def create(self, win):
				#draw platforms
				pygame.draw.rect(win, self.colour, (self.x, self.y, self.w, self.h))

		#init platforms
		plat_main = plat(0, 730, 750, 20)
		plat_1 = plat(0, 0, 200, 10)
		plat_2 = plat(0, 0, 200, 10)
		plat_3 = plat(0, 0, 200, 10)
		plat_4 = plat(0, 0, 200, 10)
		plat_5 = plat(0, 0, 200, 10)

		font_name = pygame.font.match_font('impact')
		#draw scores
		def red_text(surf, text, size, x, y, colour):
			font = pygame.font.Font(font_name, size)
			text_surface = font.render(text, True, (colour))
			text_rect = text_surface.get_rect()
			text_rect.topleft = (x, y)
			surf.blit(text_surface, text_rect)

		def blue_text(surf, text, size, x, y, colour):
			font = pygame.font.Font(font_name, size)
			text_surface = font.render(text, True, (colour))
			text_rect = text_surface.get_rect()
			text_rect.topright = (x, y)
			surf.blit(text_surface, text_rect)

		newpower = True

		def draw():
			pygame.draw.rect(win, (255, 255, 255), (0, 0, 750, 750))

			#draw background
			if newpower == False:
				win.blit(BG, (0,0))
			else:
				win.blit(BG_power, (0,0))

			#red walk animation
			if red.walkCount + 1 >= 16:
					red.walkCount = 0

			if red.left and red.superjumping == False:
				win.blit(RL[red.walkCount//2], (red.x - 37,red.y))
				red.walkCount += 1

			elif red.right and red.superjumping == False:
				win.blit(RR[red.walkCount//2], (red.x - 37,red.y))
				red.walkCount += 1

			else:
				win.blit(RI, (red.x - 37,red.y))

				if red.superjumpcount >= 96:
					red.score += 1
					red.superjumpcount = 0
					EXP.play()


			#blue walk animation
			if blue.walkCount + 1 >= 16:
					blue.walkCount = 0

			if blue.left and blue.superjumping == False:
				win.blit(BL[blue.walkCount//2], (blue.x - 37,blue.y))
				blue.walkCount += 1

			elif blue.right and blue.superjumping == False:
				win.blit(BR[blue.walkCount//2], (blue.x - 37,blue.y))
				blue.walkCount += 1

			else:
				win.blit(BI, (blue.x - 37,blue.y))

				if blue.superjumpcount >= 96:
					blue.score += 1
					blue.superjumpcount = 0

			#draw platforms
			plat_main.create(win)
			if (plat_change >= (set_plat_change - 4) and plat_change <= (set_plat_change - 2)) or (plat_change >= (set_plat_change - 10) and plat_change <= (set_plat_change - 7)) or (plat_change >= (set_plat_change - 18) and plat_change <= (set_plat_change - 14)) or (plat_change >= (set_plat_change - 28) and plat_change <= (set_plat_change - 23)) or (plat_change >= (set_plat_change - 40) and plat_change <= (set_plat_change - 34)) or (plat_change >= (set_plat_change - 54) and plat_change <= (set_plat_change - 47)) or (plat_change <= (set_plat_change - 62)):
				plat_1.create(win)
				plat_2.create(win)
				plat_3.create(win)
				plat_4.create(win)
				plat_5.create(win)

			#draw bombs
			bomb1.draw(win)
			bomb2.draw(win)
			bomb3.draw(win)

			#draw scores
			red_text(win, str(red.score), 40, 5, 5, (255, 0, 0))
			# red_text(win, str(red.hasBomb), 20, 5, 35, (255, 0, 0))

			blue_text(win, str(blue.score), 40, 745, 5, (0, 0, 255))
			# blue_text(win, str(blue.hasBomb), 20, 745, 35, (0, 0, 255))

			pygame.display.update()

		#main game loop
		loop = True
		while loop:
			#set fps
			clock.tick(32)

			#exit
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()

			keys = pygame.key.get_pressed()

			if freeze == False:

				if keys[pygame.K_b]:
					loop = False

				#move red
				if keys[pygame.K_a] and keys[pygame.K_d]:
					red.left = False
					red.right = False

				else:	
					if keys[pygame.K_a] and red.x >= red.vel:
						red.move_left()
						red.superjumpcount = 0

					elif keys[pygame.K_d] and (red.x + red.w) <= (750 - red.vel):
						red.move_right()
						red.superjumpcount = 0

					else:
						red.left = False
						red.right = False

						if red.y == 630:
							red.superjumpcount += 1

						else:
							red.superjumpcount = 0

				#move blue
				if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
					blue.left = False
					blue.right = False
				
				else:
					if keys[pygame.K_LEFT] and blue.x >= blue.vel:
						blue.move_left()
						blue.superjumpcount = 0

					elif keys[pygame.K_RIGHT] and (blue.x + blue.w) <= (750 - blue.vel):
						blue.move_right()
						blue.superjumpcount = 0

					else:
						blue.left = False
						blue.right = False

						if blue.y == 630:
							blue.superjumpcount += 1

						else:
							blue.superjumpcount = 0

				#red jump
				if (not red.jumping) and keys[pygame.K_w]:
					red.jumping = True
					red.jump_nyc = 30

				#blue jump
				if (not blue.jumping) and keys[pygame.K_UP]:
					blue.jumping = True
					blue.jump_nyc = 30

				red.jump()
				blue.jump()

				if red.y == 35 and newpower == True:
					# red.y = 630
					if red.score >= 1:
						red.score -= 1
					elif red.score > 0:
						red.score = 0

					newpower = False

				if blue.y == 35 and newpower == True:
					# blue.y = 630
					if blue.score >= 1:
						blue.score -= 1
					elif blue.score > 0:
						blue.score = 0

					newpower = False


				#randomize platforms
				plat_change += 1
				if plat_change >= set_plat_change:
					plat_1.random()
					plat_2.random()
					plat_3.random()
					plat_4.random()
					plat_5.random()

					plat_change = 0

					newpower = True

				#makes bombs fall
				bomb1.fall()
				bomb2.fall()
				bomb3.fall()

				bomb1.hit()
				bomb2.hit()
				bomb3.hit()

			#freeze game if bomb hit player
			if freeze == True:
				freeze_count += 1

				if freeze_count == 32:
					freeze = False
					freeze_count = 0

					red.y = 600
					blue.y = 600
					red.x = 50
					blue.x = 674

					blue.jump_nyc = 0
					red.jump_nyc = 0

			#draw game
			draw()





	if muV == 3 and muH == 2: 
		#import images
		BG = pygame.image.load('falling_BG.png')
		BG_power = pygame.image.load('falling_power.png')
		RR = [pygame.image.load('RR_01.png'), pygame.image.load('RR_02.png'), pygame.image.load('RR_03.png'), pygame.image.load('RR_04.png'), pygame.image.load('RR_05.png'), pygame.image.load('RR_06.png'), pygame.image.load('RR_07.png'), pygame.image.load('RR_08.png')]
		RL = [pygame.image.load('RL_01.png'), pygame.image.load('RL_02.png'), pygame.image.load('RL_03.png'), pygame.image.load('RL_04.png'), pygame.image.load('RL_05.png'), pygame.image.load('RL_06.png'), pygame.image.load('RL_07.png'), pygame.image.load('RL_08.png')]
		RI = pygame.image.load('RI_01.png')
		RW = pygame.image.load('RW_01.png')
		BR = [pygame.image.load('BR_01.png'), pygame.image.load('BR_02.png'), pygame.image.load('BR_03.png'), pygame.image.load('BR_04.png'), pygame.image.load('BR_05.png'), pygame.image.load('BR_06.png'), pygame.image.load('BR_07.png'), pygame.image.load('BR_08.png')]
		BL = [pygame.image.load('BL_01.png'), pygame.image.load('BL_02.png'), pygame.image.load('BL_03.png'), pygame.image.load('BL_04.png'), pygame.image.load('BL_05.png'), pygame.image.load('BL_06.png'), pygame.image.load('BL_07.png'), pygame.image.load('BL_08.png')]
		BI = pygame.image.load('BI_01.png')
		BW = pygame.image.load('BW_01.png')
		BME = [pygame.image.load('BME_01.png'), pygame.image.load('BME_02.png'), pygame.image.load('BME_03.png'), pygame.image.load('BME_04.png'), pygame.image.load('BME_05.png'), pygame.image.load('BME_06.png'), pygame.image.load('BME_07.png'), pygame.image.load('BME_08.png')]
		BM = pygame.image.load('BM_01.png')
		SBG = pygame.image.load('score_BG.png')

		EXP = pygame.mixer.Sound('PEW.wav')
		POP = pygame.mixer.Sound('pling.wav')

		class player(object):
			def __init__(self, x, y, w, h):
				self.x = x
				self.y = y
				self.w = w
				self.h = h
				self.left = False
				self.right = False
				self.vel = 10
				self.walkCount = 0
				self.jump_nyc = 0
				self.jump_change = 3
				self.jumping = False
				self.xplat = [730]
				self.plat_below = []
				self.targ_plat = 730
				self.hasBomb = 3
				self.score = 0
				self.superjumpcount = 0
				self.superjumping = False

			def move_left(self):
				self.left = True
				self.right = False
				self.x -= self.vel

			def move_right(self):
				self.left = False
				self.right = True
				self.x += self.vel

			def falling(self):
				#check if falling
				if self.y != (self.targ_plat - 100) and not self.jumping:
					self.jumping = True
					self.jump_nyc = 0
					self.jump()

					print(self.y)
					print(self.targ_plat + 100)

			def jump(self):
				#check platforms at same x
				self.xplat = [730]
				if ((self.x + 13) >= plat_1.x) and ((self.x + 13) <= (plat_1.x + plat_1.w)):
					self.xplat.append(plat_1.y)

				if ((self.x + 13) >= plat_2.x) and ((self.x + 13) <= (plat_2.x + plat_2.w)):
					self.xplat.append(plat_2.y)

				if ((self.x + 13) >= plat_3.x) and ((self.x + 13) <= (plat_3.x + plat_3.w)):
					self.xplat.append(plat_3.y)

				if ((self.x + 13) >= plat_4.x) and ((self.x + 13) <= (plat_4.x + plat_4.w)):
					self.xplat.append(plat_4.y)

				if ((self.x + 13) >= plat_5.x) and ((self.x + 13) <= (plat_5.x + plat_5.w)):
					self.xplat.append(plat_5.y)

				self.plat_below = []
				for plat_val in self.xplat:
					if plat_val > (self.y + 99):
						self.plat_below.append(plat_val)
					
				#find nearst platform under player
				self.targ_plat = 1000
				for plat_val2 in self.plat_below:
					if self.targ_plat > plat_val2 :
						self.targ_plat = plat_val2

				if self.y != (self.targ_plat - 100) and not self.jumping:
					self.jumping = True
					self.jump_nyc = 0

				#check if about to land
				if self.jumping:
					if (self.y + 99) - self.jump_nyc > self.targ_plat:
						self.y = self.targ_plat - 100
						self.jumping = False
						self.superjumping = False

					if self.jumping == True:
						self.y -= self.jump_nyc
						self.jump_nyc -= self.jump_change

		#init players
		red = player(50, 600, 26, 100)

		class bomb(object):
			def __init__(self, x, y):
				self.x = x
				self.y = y
				self.nyc = 0
				self.fall_speed = 2
				self.explode = True
				self.exploding = 20

			def fall(self):
				#make bomb fall
				if self.y < 1000 and self.explode == False:
					self.y -= self.nyc
					self.nyc -= self.fall_speed

					#expload on floor
					if (self.y + self.nyc) > 727:
						self.y = 727
						
						EXP.play()

						self.explode = True
						self.exploding = 0

				if self.exploding >= 16 and self.explode == True:
					self.rand()

			def draw(self, win):
				#draw bomb
				if self.explode == False:
					win.blit(BM, (self.x - 50, self.y - 50))

				#draw explosion
				if self.explode == True and self.exploding < 16:
					win.blit(BME[self.exploding//2], (self.x - 50,self.y - 50))

					self.exploding += 1

			def hit(self):

				#expload bomb if hit red player
				if self.x >= red.x - 37 and self.x <= red.x + 62 and self.y >= red.y + 25 and self.y <= red.y + 99 and self.explode == False:
					self.explode = True
					red.score += 1
					freeze = True
					POP.play()
					EXP.play()	

			def rand(self):
				self.x = random.randint(25, 725)
				self.y = random.randint(25, 100) * -1

				self.nyc = 0

				self.exploding = 0
				self.explode = False

		#init freeze
		freeze = False
		freeze_count = 0

		#init red and blue bomb
		bomb1 = bomb(0, 1001)
		bomb2 = bomb(0, 1001)
		bomb3 = bomb(0, 1001)

		plat_change = 1999
		set_plat_change = 320

		class plat(object):
			def __init__(self, x, y, w, h):
				self.x = x
				self.y = y
				self.w = w
				self.h = h
				self.place = 0
				self.colour = (0, 0, 0)

			def random(self):
				#randomize platfoarm locations
				self.place = random.randint(1, 5)
				
				if self.place == 1:
					self.x = 50
					self.y = 600

				if self.place == 2:
					self.x = 500
					self.y = 600

				if self.place == 3:
					self.x = 275
					self.y = 450

				if self.place == 4:
					self.x = 50
					self.y = 300

				if self.place == 5:
					self.x = 500
					self.y = 300

			def create(self, win):
				#draw platforms
				pygame.draw.rect(win, self.colour, (self.x, self.y, self.w, self.h))

		#init platforms
		plat_main = plat(0, 730, 750, 20)
		plat_1 = plat(0, 0, 200, 10)
		plat_2 = plat(0, 0, 200, 10)
		plat_3 = plat(0, 0, 200, 10)
		plat_4 = plat(0, 0, 200, 10)
		plat_5 = plat(0, 0, 200, 10)

		font_name = pygame.font.match_font('impact')
		#draw scores
		def red_text(surf, text, size, x, y, colour):
			font = pygame.font.Font(font_name, size)
			text_surface = font.render(text, True, (colour))
			text_rect = text_surface.get_rect()
			text_rect.topleft = (x, y)
			surf.blit(text_surface, text_rect)

		def blue_text(surf, text, size, x, y, colour):
			font = pygame.font.Font(font_name, size)
			text_surface = font.render(text, True, (colour))
			text_rect = text_surface.get_rect()
			text_rect.topright = (x, y)
			surf.blit(text_surface, text_rect)

		def score_text(surf, text, size, x, y, colour):
			font = pygame.font.Font(font_name, size)
			text_surface = font.render(text, True, (colour))
			text_rect = text_surface.get_rect()
			text_rect.midtop = (x, y)
			surf.blit(text_surface, text_rect)

		newpower = True

		def draw():
			if second >= 0:
				pygame.draw.rect(win, (255, 255, 255), (0, 0, 750, 750))

				#draw background
				if newpower == False:
					win.blit(BG, (0,0))
				else:
					win.blit(BG_power, (0,0))

				#red walk animation
				if red.walkCount + 1 >= 16:
						red.walkCount = 0

				if red.left and red.superjumping == False:
					win.blit(RL[red.walkCount//2], (red.x - 37,red.y))
					red.walkCount += 1

				elif red.right and red.superjumping == False:
					win.blit(RR[red.walkCount//2], (red.x - 37,red.y))
					red.walkCount += 1

				else:
					win.blit(RI, (red.x - 37,red.y))

					if red.superjumpcount >= 96:
						red.score += 1
						red.superjumpcount = 0
						EXP.play()

				#draw platforms
				plat_main.create(win)
				if (plat_change >= (set_plat_change - 4) and plat_change <= (set_plat_change - 2)) or (plat_change >= (set_plat_change - 10) and plat_change <= (set_plat_change - 7)) or (plat_change >= (set_plat_change - 18) and plat_change <= (set_plat_change - 14)) or (plat_change >= (set_plat_change - 28) and plat_change <= (set_plat_change - 23)) or (plat_change >= (set_plat_change - 40) and plat_change <= (set_plat_change - 34)) or (plat_change >= (set_plat_change - 54) and plat_change <= (set_plat_change - 47)) or (plat_change <= (set_plat_change - 62)):
					plat_1.create(win)
					plat_2.create(win)
					plat_3.create(win)
					plat_4.create(win)
					plat_5.create(win)

				#draw bombs
				bomb1.draw(win)
				bomb2.draw(win)
				bomb3.draw(win)

				#draw scores
				red_text(win, str(red.score), 40, 5, 5, (255, 0, 0))
				# red_text(win, str(red.hasBomb), 20, 5, 35, (255, 0, 0))

				blue_text(win, str(second), 40, 745, 5, (0, 0, 255))

			if second < 0:
				red.x = -1000
				if red.score == 1:
					print_score = ("You got hit " + str(red.score) + " time.")
				else:
					print_score = ("You got hit " + str(red.score) + " times.")

				win.blit(SBG, (0,0))
				score_text(win, str(print_score), 50, 375, 275, (255, 0, 0))

			pygame.display.update()

		second = 60
		tick = 0

		#main game loop
		loop = True
		while loop:
			#set fps
			clock.tick(32)

			tick += 1
			if tick == 32:
				second -= 1
				tick = 0

			#exit
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()

			keys = pygame.key.get_pressed()

			if freeze == False:

				if keys[pygame.K_b]:
					loop = False

				#move red
				if keys[pygame.K_a] and keys[pygame.K_d]:
					red.left = False
					red.right = False

				else:	
					if keys[pygame.K_a] and red.x >= red.vel:
						red.move_left()
						red.superjumpcount = 0

					elif keys[pygame.K_d] and (red.x + red.w) <= (750 - red.vel):
						red.move_right()
						red.superjumpcount = 0

					else:
						red.left = False
						red.right = False

						if red.y == 630:
							red.superjumpcount += 1

						else:
							red.superjumpcount = 0

				#red jump
				if (not red.jumping) and keys[pygame.K_w]:
					red.jumping = True
					red.jump_nyc = 30

				red.jump()

				if red.y == 35 and newpower == True:
					# red.y = 630
					if red.score >= 1:
						red.score -= 1
					elif red.score > 0:
						red.score = 0

					newpower = False

				#randomize platforms
				plat_change += 1
				if plat_change >= set_plat_change:
					plat_1.random()
					plat_2.random()
					plat_3.random()
					plat_4.random()
					plat_5.random()

					plat_change = 0

					newpower = True

				#makes bombs fall
				bomb1.fall()
				bomb2.fall()
				bomb3.fall()

				bomb1.hit()
				bomb2.hit()
				bomb3.hit()

			#freeze game if bomb hit player
			if freeze == True:
				freeze_count += 1

				if freeze_count == 32:
					freeze = False
					freeze_count = 0

					red.y = 600
					blue.y = 600
					red.x = 50
					blue.x = 674

					blue.jump_nyc = 0
					red.jump_nyc = 0

			#draw game
			draw()

#exit
pygame.quit()