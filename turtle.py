import sys, pygame
import math
import time

WINDOWX    = 500
WINDOWY    = 500

#TURTLE PROPERTIES
TURTLE_WIDTH = 25
TURTLE_HEIGHT = 25
NOSEANGLE  = 15

class Turtle:

	def __init__(self,mainx,mainy):
		self.x 			 = mainx/2
		self.y 			 = mainy/2
		self.angle = 0
		self.angleRad = 0
		self.pointStart     = []
		self.pointEnd      = []
		self.isPenUp      = False
		self.isVisible     = True


		"""
		
		self.baseX 		 = self.x + WIDTH*math.cos(self.orientation)
		self.baseY 		 = self.y + WIDTH*math.sin(self.orientation)
		self.leftX       = self.x - HYPOTENUSE*math.cos(self.orientation - NOSEANGLE)
		self.leftY       = self.y - HYPOTENUSE*math.sin(self.orientation - NOSEANGLE)
		self.rightX      = self.x - HYPOTENUSE*math.cos(self.orientation + NOSEANGLE)
		self.rightY      = self.y - HYPOTENUSE*math.sin(self.orientation + NOSEANGLE)

		self.spineLine   = Line(Point(self.x,self.y), Point(self.baseX , self.baseY))
		self.baseLine    = Line(Point(self.leftX,self.leftY),Point(self.rightX,self.rightY))
		self.leftLine    = Line(Point(self.x, self.y), Point(self.leftX, self.leftY))
		self.rightLine   = Line(Point(self.x, self.y), Point(self.rightX, self.rightY))
		"""


	def hideTurtle(self):
		self.isVisible = False
	def showTurtle(self):
		self.isVisible = True
	def penUp(self):
		self.isPenUp = True
	def penDown(self):
		self.isPenUp = False

	def updatePos(self):
		"""
		self.baseX 		 = self.x + WIDTH*math.cos(self.orientation)
		self.baseY 		 = self.y + WIDTH*math.sin(self.orientation)
		self.leftX       = self.x - HYPOTENUSE*math.cos(self.orientation - NOSEANGLE)
		self.leftY       = self.y - HYPOTENUSE*math.sin(self.orientation - NOSEANGLE)
		self.rightX      = self.x - HYPOTENUSE*math.cos(self.orientation + NOSEANGLE)
		self.rightY      = self.y - HYPOTENUSE*math.sin(self.orientation + NOSEANGLE)

		self.spineLine   = Line(Point(self.x,self.y), Point(self.baseX , self.baseY))
		self.baseLine    = Line(Point(self.leftX,self.leftY),Point(self.rightX,self.rightY))
		self.leftLine    = Line(Point(self.x, self.y), Point(self.leftX, self.leftY))
		"""

	def draw(self, screen):
		"""
		self.spineLine.draw(mainWindow)
		self.baseLine.draw(mainWindow)
		self.leftLine.draw(mainWindow)
		self.rightLine.draw(mainWindow)
		"""
		if self.isVisible:
			screen.blit(self.image, self.imageRect)
		if self.pointStart is not None:
			for px,py in zip(self.pointStart, self.pointEnd):
				pygame.draw.line(screen, (255,0,0), px, py, 2)

	def spin(self):
		for i in range(0,90):
			self.spineLine.move(20,0)
	def getImage(self, image):
		self.image = image
		#self.image = pygame.transform.scale(self.image, (TURTLE_WIDTH, TURTLE_HEIGHT))
		self.imageSave = self.image
		self.imageRect = image.get_rect()
		#self.x = WINDOWX/2 - TURTLE_WIDTH/2
		#self.y = WINDOWY/2 - TURTLE_HEIGHT/2
		self.imageRect = self.imageRect.move([self.x , self.y ])
		#self.x += TURTLE_WIDTH/2
		#self.y += TURTLE_HEIGHT/2
		self.x = self.imageRect.centerx
		self.y = self.imageRect.centery
		print self.x , self.y

	def rotate(self, angle):
		self.angle += angle
		self.angleRad = math.radians(self.angle)
		self.image = rot_center(self.imageSave, self.image,self.angle)

	def mvForward(self, distance, screen):
		if self.isPenUp == False:
			self.pointStart.append((self.x, self.y))
		#self.pointEnd.append((int(self.x + distance * math.cos(self.angleRad)),int(self.y - distance * math.sin(self.angleRad))))
		#print self.points
		#self.x = int(self.x + distance * math.cos(self.angleRad))
		#self.y = int(self.y - distance * math.sin(self.angleRad))
		self.imageRect = self.imageRect.move([int(distance * math.cos(self.angleRad)), int(-distance * math.sin(self.angleRad))])
		self.x = self.imageRect.centerx
		self.y = self.imageRect.centery
		if self.isPenUp == False:
			self.pointEnd.append((self.x,self.y))
		print self.imageRect
	def mvBackward(self, distance, screen):
		if self.isPenUp == False:
			self.pointStart.append((self.x, self.y))
		#self.pointEnd.append((int(self.x + distance * math.cos(self.angleRad)),int(self.y - distance * math.sin(self.angleRad))))
		#print self.points
		#self.x = int(self.x + distance * math.cos(self.angleRad))
		#self.y = int(self.y - distance * math.sin(self.angleRad))
		self.imageRect = self.imageRect.move([-int(distance * math.cos(self.angleRad)), int(distance * math.sin(self.angleRad))])
		self.x = self.imageRect.centerx
		self.y = self.imageRect.centery
		if self.isPenUp == False:
			self.pointEnd.append((self.x,self.y))
		print self.imageRect


def rot_center(orig_image, image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(orig_image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

