# INITIALIZATION
import pygame, math, sys
from pygame.locals import *

BLACK = (0,0,0)
WHITE = (255, 255, 255)
COLUMNS = 16
ROWS = 21
TREASURES = 10
WALLS = 30
MONSTERS = 3
TILE_SIZE = 48
DIRECTIONS = ['north', 'south', 'east', 'west']
ALL_TREASURES = {
	"hat": "Quite cunning",
	"sqord": "Knock-off sword. Probably from Ikea",
	"book": "What the hell are you going to do with this?",
	"rainbow": "Joy in a box."
}
LONG_STRING = "X" * 50

class Treasure(object):
	''' Not implemented yet.
	'''
	def __init__(self):
		k = ALL_TREASURES.keys()
		r = random.randint(0, ALL_TREASURES.keys().__len__()-1)
		self.title = ALL_TREASURES.keys()[r]
		self.description = ALL_TREASURES[self.title]

class Map(object):
	def __init__(self):
		self.map = []
		for i in range(ROWS):
			row = []
			for j in range(COLUMNS):
				row.append(0)
			self.map.append(row)
	
	def clear_block(self, position):
		x, y = position
		column = x//50
		row = y//50
		print("Column %s, Row %s" % (str(column), str(row)))
		self.map[column][row] = 1
		
	def print_ascii_map(self):
		for row in self.map:
			print(row)
			
class Game(object):
	def __init__(self):
		self.screen = pygame.display.set_mode((1024, 768))
		self.player = pygame.image.load('dude.png')
		self.bg = pygame.image.load('rainbowbg.png')
		self.clock = pygame.time.Clock()
		self.direction = 0
		self.position = (300, 300)
		self.map = Map()
		self.map.clear_block(self.position)
		self.run()
		
	def draw_darkness(self):
		print(self.map.map.__len__())
		for row in range(ROWS):
			for col in range(COLUMNS):
				if self.map.map[row][col] == 0:
					pygame.draw.rect(self.screen, BLACK, (row*50, col*50, 50, 50))
	
	def move(self, hor, vert):
		x, y = self.position
		x = x + hor
		y = y + vert
		if x > ROWS * 50 or x < 0 or y > COLUMNS * 50 or y < 0:
			return
		self.position = (x, y)
		self.map.clear_block(self.position)
		self.screen.blit(self.bg, (0, 0))
		self.draw_darkness()
		self.screen.blit(self.player, self.position)
		pygame.display.flip()
		
	def run(self):
		while 1:
			self.clock.tick(30)
			hor = 0
			vert = 0
			for event in pygame.event.get():
				if not hasattr(event, 'key'): continue
				if event.key == K_ESCAPE: sys.exit(0)
				if event.key == K_LEFT: hor = -25
				if event.key == K_RIGHT: hor = 25
				if event.key == K_UP: vert = -25
				if event.key == K_DOWN: vert = 25
				self.move(hor, vert)
				self.map.print_ascii_map()

	def draw_alert(self, alert, color=WHITE):
		''' Draws the alert box at the bottom
		''' 
		self.alert = self.font.render(LONG_STRING, True, BLACK, BLACK)
		self.screen.blit(self.alert, (0, 790))
		try:
			pygame.display.flip()
		except:
			pass
		self.alert = self.font.render(alert, True, color, BLACK)
				
				
def main():
	while 1:
		game = Game()

if __name__ == "__main__":
	main()