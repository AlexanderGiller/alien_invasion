import pygame

class Ship:
	'''A class that manages the ship´s different characteristics'''

	def __init__(self, ai_game):
		'''Initialize the ship'''
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		#Load the ship´s image and get its rect
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		#Start each new ship on the bottom center of the screen
		self.rect.midbottom = self.screen_rect.midbottom

		#Store a decimal for the horizontal position of the ship
		self.x = float(self.rect.x)

		#Movement flag
		self.moving_right = False
		self.moving_left = False


	def update(self):
		'''Update the ships position based on the movement flag'''
		#Update the ships x value, not the rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		elif self.moving_left and self.rect.left > 0: 
			self.x -= self.settings.ship_speed

		#Update rect object to from self.x.
		self.rect.x = self.x


	def center_ship(self):
		'''Center the ship on the screen'''
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)


		
	def blitme(self):
		'''Draw the ship at its current location'''
		self.screen.blit(self.image, self.rect)

			


